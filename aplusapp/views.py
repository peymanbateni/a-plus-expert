from django.shortcuts import render, redirect
from aplusapp.forms import *
from aplusapp.models import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from datetime import datetime
from datetime import date
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# handles main page
def homeHanlder(request):
    return render(request, 'aplus-expert-home.html',
        context={'page': 'Home'})

# handles the about page
def aboutHanlder(request):
    return render(request, 'aplus-expert-about.html',
        context={'page': 'About'})

# handles the contact page
def contactHanlder(request):
    return render(request, 'aplus-expert-contact.html',
        context={'page': 'Contact'})

# handles the free consultation page
def freeConsultationHandler(request):
    return render(request, 'aplus-expert-free-consultation.html',
        context={'page': 'Free Consultation'})

# handles form completion requests
def completeRequestHanlder(request):
    if request.method == "POST":
        if request.POST.get('subscribe-to-news-letter') == "":
            subcription_form = NewsLetterForm(request.POST)
            if subcription_form.is_valid():
                subcription_form_data = subcription_form.cleaned_data
                NewsLetterSubscription.objects.create(email=subcription_form_data['email'])

                msg_html = render_to_string('subscribe-welcome-email.html', {'email': subcription_form_data['email']})

                send_mail(
                    'Thank You for Subscribing to Our Newsletter',
                    'Thank You for Subscribing to Our Newsletter',
                    'A+ Expert <info@aplus-expert.com>',
                    [subcription_form_data['email'],],
                    html_message=msg_html,
                )

                return render(request, 'aplus-expert-complete-request.html', context={'title': 'Thank You for Subscribing to Our News Letter',
                    'text': "Now, you will be recieving our updates right away!"})

            else:
                return error_404(request)

        if request.POST.get("request-free-consultation") == "":
            free_consultation_form = FreeConsultationRequestForm(request.POST)
            if free_consultation_form.is_valid():
                free_consultation_form_data = free_consultation_form.cleaned_data
                FreeConsultationRequest.objects.create(name=free_consultation_form_data['name'],
                    email=free_consultation_form_data['email'], phone=free_consultation_form_data['phone'],
                    school=free_consultation_form_data['school'], address=free_consultation_form_data['address'],
                    subjects=free_consultation_form_data['subjects'], grade=free_consultation_form_data['grade'],
                    details=free_consultation_form_data['details'])

                msg_html = render_to_string('free-consultation-email.html', {'name': free_consultation_form_data['name']})

                send_mail(
                    'Free Consultation',
                    'Free Consultation',
                    'A+ Expert <info@aplus-expert.com>',
                    [free_consultation_form_data['email'],],
                    html_message=msg_html,
                )

                msg_html = render_to_string('consultation-internal-email.html', {'name': free_consultation_form_data['name'],
                    'email': free_consultation_form_data['email'], 'phone': free_consultation_form_data['phone'],
                    'school': free_consultation_form_data['school'], 'address': free_consultation_form_data['address'],
                    'subjects': free_consultation_form_data['subjects'], 'grade': free_consultation_form_data['grade'],
                    'details': free_consultation_form_data['details']})

                send_mail(
                    'New Free Consultation Request',
                    'New Free Consultation Request',
                    'A+ Expert <info@aplus-expert.com>',
                    ['info@aplus-expert.com',],
                    html_message=msg_html,
                )

                return render(request, 'aplus-expert-complete-request.html', context={'title': 'Your Free Consultation Request Has Been Submitted',
                    'text': "We will be following up with you in 1-2 business days."})

        if request.POST.get("send-contact-message") == "":
            contact_form = ContactRequestForm(request.POST)
            if contact_form.is_valid():
                contact_form_data = contact_form.cleaned_data
                FreeConsultationRequest.objects.create(name=contact_form_data['name'],
                    email=contact_form_data['email'], phone=contact_form_data['phone'],
                    details=contact_form_data['details'])

                msg_html = render_to_string('contact-email.html', {'name': contact_form_data['name']})

                send_mail(
                    'Thank You for Your Message',
                    'Thank You for Your Message',
                    'A+ Expert <info@aplus-expert.com>',
                    [contact_form_data['email'],],
                    html_message=msg_html,
                )

                msg_html = render_to_string('contact-internal-email.html', {'name': contact_form_data['name'],
                    'email': contact_form_data['email'], 'phone': contact_form_data['phone'],
                    'details': contact_form_data['details']})

                send_mail(
                    'New Contact Message',
                    'New Contact Message',
                    'A+ Expert <info@aplus-expert.com>',
                    ['info@aplus-expert.com',],
                    html_message=msg_html,
                )

                return render(request, 'aplus-expert-complete-request.html', context={'title': 'Your Message Has Been Submitted',
                    'text': "We will be contacting you in 1-2 business days."})

            else:
                return error_404(request)

    # else
    return redirect('/home/')

#error handlers
def error_404(request, exception):
        data = {}
        return render(request,'aplus-expert-404.html', data)
def error_500(request):
        data = {}
        return render(request,'aplus-expert-500.html', data)

@login_required(login_url='/login/')
def dashboardProfileHanlder(request):
    if request.method == 'POST':
        
        if request.POST.get('update_info'):
            ADForm = AccountDetailsForm(request.POST, request.FILES)
            if ADForm.is_valid():
                cleaned_data = ADForm.cleaned_data
                user = request.user
                user.first_name = cleaned_data["first_name"]
                user.last_name = cleaned_data["last_name"]
                user.phone_number = cleaned_data["phone_number"]

                if cleaned_data["profile_picture"]:
                    if (user.profile_picture.name != settings.DEFAULT_PROFILE_PICTURE):
                        #osremove('media/' + user.profile_picture.name)
                        user.profile_picture.delete()
                    user.profile_picture = cleaned_data["profile_picture"]

                if cleaned_data["clear_profile_picture"]:
                    user.set_pic_to_default()

                user.save()

                return render(request, 'aplus-dashboard-profile.html', context={'ADMessage': 'Success', 'selected': 'profile'})
            else:
                return render(request, 'aplus-dashboard-profile.html', context={'account_info_form': ADForm, 'selected': 'profile'})
        
        elif request.POST.get('change_password'):
            PCForm = PasswordChangeForm(request.user, request.POST)
            if PCForm.is_valid():
                user = PCForm.save()
                update_session_auth_hash(request, user)  # Important!

                return render(request, 'aplus-dashboard-profile.html', context={'PCMessage': 'Success', 'selected': 'profile'})
            else:
                return render(request, 'aplus-dashboard-profile.html', context={'password_change_form': PCForm, 'selected': 'profile'})

        elif request.POST.get('change_email'):
            ECForm = EmailChangeForm(request.POST)
            if ECForm.is_valid():
                cleaned_data = ECForm.cleaned_data
                newEmail = cleaned_data["new_email"]
                newEmailConf = cleaned_data["new_email_conf"]
                if (newEmail != newEmailConf):
                    return render(request, 'aplus-dashboard-profile.html', context={'ECMessage': 'New email and its confirmation must match.', 'selected': 'profile'})
                elif CUser.objects.filter(email = newEmail).exists():
                    return render(request, 'aplus-dashboard-profile.html', context={'ECMessage': 'New email entered is assigned to a different account.', 'selected': 'profile'})
                else:
                    user = request.user
                    old_email = user.email
                    user.email = newEmail
                    user.save()

                    return render(request, 'aplus-dashboard-profile.html', context={'ECMessage': "Success", 'selected': 'profile'})
            else:
                return render(request, 'aplus-dashboard-profile.html', context={'ECMessage': "Make sure the provided emails are of the desired format.", 'selected': 'profile'})
               
    else:
        return render(request, 'aplus-dashboard-profile.html', context={'ACForm': AccountDetailsForm, 'selected': 'profile'})

@login_required(login_url='/login/')
def dashboardReportHandler(request):

    if request.method == 'POST':
        if request.POST.get('submit_report'):
            report_form = ReportDetailsForm(request.POST)
            if report_form.is_valid():
                report_form_clean = report_form.cleaned_data
                student_id = report_form_clean['student_id']
                tutored_student = Student.objects.filter(aplus_id=student_id).first()
                reports_tutor = Tutor.objects.filter(user=request.user).first()
                now = datetime.now()
                new_report = Report.objects.create(student=tutored_student, tutor=reports_tutor, date=report_form_clean['date'], date_added=now,
                    number_of_hours=report_form_clean['hours'], details=report_form_clean['session_comments'])

                reports_tutor.hours_tutored = reports_tutor.hours_tutored + report_form_clean['hours']
                reports_tutor.hours_tutored_this_month = reports_tutor.hours_tutored_this_month + report_form_clean['hours']
                reports_tutor.save()

                tutored_student.sessional_hours = tutored_student.sessional_hours - report_form_clean['hours']
                tutored_student.hours_of_tutoring_used_this_month = tutored_student.hours_of_tutoring_used_this_month + report_form_clean['hours']
                tutored_student.save()

                tutor = Tutor.objects.filter(user=request.user).first()
                students = StudentTutoredByTutor.objects.filter(tutor__user=request.user)
                reports = Report.objects.filter(tutor__user=request.user).order_by('-date')

                student_msg_html = render_to_string('report-student-template.html', {'report': new_report})

                send_mail(
                    'Tutoring Session Report',
                    'Tutoring Session Report',
                    'A+ Expert <info@aplus-expert.com>',
                    [tutored_student.email,],
                    html_message=student_msg_html,
                )

                tutor_msg_html = render_to_string('report-tutor-template.html', {'report': new_report})

                send_mail(
                    'Report Confirmation',
                    'Report Confirmation',
                    'A+ Expert <info@aplus-expert.com>',
                    [request.user.email,],
                    html_message=tutor_msg_html,
                )

                return render(request, 'aplus-dashboard-report.html', context={'selected': 'report',
                'students': students, 'reports': reports, 'ReportMessage': 'Success', 'tutor': tutor})

            tutor = Tutor.objects.filter(user=request.user).first()
            students = StudentTutoredByTutor.objects.filter(tutor__user=request.user)
            reports = Report.objects.filter(tutor__user=request.user).order_by('-date')

            return render(request, 'aplus-dashboard-report.html', context={'selected': 'report',
            'students': students, 'reports': reports, 'report_form': report_form, 'ReportMessage': 'Failed', 'tutor': tutor})

    tutor = Tutor.objects.filter(user=request.user).first()
    students = StudentTutoredByTutor.objects.filter(tutor__user=request.user)
    reports = Report.objects.filter(tutor__user=request.user).order_by('-date')

    return render(request, 'aplus-dashboard-report.html', context={'selected': 'report',
        'students': students, 'reports': reports, 'tutor': tutor})

@login_required(login_url='/login/')
def dashboardTutorOverviewHandler(request):
    if (not request.user.is_an_exec):
        return redirect('/dashboard/')

    tutors = Tutor.objects.all()
    return render(request, 'aplus-dashboard-tutor-overview.html', context={'selected': 'tutor-overview', 'tutors': tutors})

@login_required(login_url='/login/')
def dashboardStudentOverviewHandler(request):
    if (not request.user.is_an_exec):
        return redirect('/dashboard/')

    students = Student.objects.all()
    return render(request, 'aplus-dashboard-student-overview.html', context={'selected': 'student-overview', 'students': students})

@login_required(login_url='/login/')
def dashboardPaymentHandler(request):
    if (not request.user.is_an_exec):
        return redirect('/dashboard/')

    if request.method == "POST":
        if request.POST.get('send_receipt'):
            receipt_form = ReceiptForm(request.POST)
            if receipt_form.is_valid():
                receipt_form_data = receipt_form.cleaned_data
                new_receipt = Receipt.objects.create(name=receipt_form_data['name'], email=receipt_form_data['email'],
                    amount=receipt_form_data['amount'], date=receipt_form_data['date'])
            
                msg_html = render_to_string('payment-confirmation.html', {'receipt': new_receipt})

                send_mail(
                    'Payment Confirmation',
                    'Payment Confirmation',
                    'A+ Expert <info@aplus-expert.com>',
                    [receipt_form_data['email'],],
                    html_message=msg_html,
                )

                receipts = Receipt.objects.all()
                return render(request, 'aplus-dashboard-payment.html', context={'selected': 'payments',
                    'receipts': receipts})

            else:
                receipts = Receipt.objects.all()
                return render(request, 'aplus-dashboard-payment.html', context={'selected': 'payments',
                    'receipts': receipts, 'receipt_form': receipt_form})

    receipts = Receipt.objects.all()
    return render(request, 'aplus-dashboard-payment.html', context={'selected': 'payments',  'receipts': receipts})

@login_required(login_url='/login/')
def dashboardProfits(request):
    if request.method == "POST":

        if request.POST.get('profit_calculate'):
            profit_form = ProfitCalculatorForm(request.POST)

            if profit_form.is_valid():
                profit_form_data = profit_form.cleaned_data
                reports = Report.objects.filter(date__gte=profit_form_data['start_date'],
                                date__lte=profit_form_data['end_date'])

                amount = 0.0
                for report in reports:
                    tutor_rate = StudentTutoredByTutor.objects.filter(student=report.student, tutor=report.tutor).first().tutor_rate
                    student_price = Student.objects.filter(aplus_id = report.student.aplus_id).first().hourly_charge
                    profit_per_report = report.number_of_hours * (student_price - tutor_rate)

                    amount = amount + profit_per_report

                tutors = Tutor.objects.all()
                payment_list = []
                for the_tutor in tutors:
                    tutor_reports = Report.objects.filter(date__gte=profit_form_data['start_date'],
                        date__lte=profit_form_data['end_date'], tutor=the_tutor)
                    
                    tutor_amount = 0.0
                    for report in tutor_reports:
                        tutor_rate = StudentTutoredByTutor.objects.filter(student=report.student, tutor=report.tutor).first().tutor_rate
                        tutor_amount += report.number_of_hours * tutor_rate

                    tutor_name = the_tutor.user.first_name + " " + the_tutor.user.last_name
                    payment_list.append({'tutor_name': tutor_name, 'amount':tutor_amount})                

                return render(request, 'aplus-dashboard-profits.html', context={'selected': 'profits', 'amount': amount, 'payment_list': payment_list})

            return render(request, 'aplus-dashboard-profits.html', context={'selected': 'profits', 'profit_form': profit_form})

    return render(request, 'aplus-dashboard-profits.html', context={'selected': 'profits'})

@login_required(login_url='/login/')
def dashboardYourSessionsHandler(request):

    student = Student.objects.filter(user=request.user).first()
    reports = Report.objects.filter(student=student).order_by('-date')

    return render(request, 'aplus-dashboard-student-report.html', context={'selected': 'your-sessions',
        'student': student, 'reports': reports})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.clean()
            login(request, form.user_cache)
            if (form.user_cache.is_a_tutor):
                return redirect('/dashboard/report/')
            elif (form.user_cache.is_a_student):
                return redirect('/dashboard/your-sessions/')
    else:
        form = AuthenticationForm()

    return render(request, 'aplus-expert-login.html', {'form' : form})
