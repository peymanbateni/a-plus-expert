# define all forms here
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# limit image size
class RestrictedImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        self.max_upload_size = kwargs.pop('max_upload_size', None)
        if not self.max_upload_size:
            self.max_upload_size = settings.MAX_UPLOAD_SIZE
        super(RestrictedImageField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(RestrictedImageField, self).clean(*args, **kwargs)
        try:
            if data.size > self.max_upload_size:
                raise forms.ValidationError(_('File size must be under %s. Current file size is %s.') % (filesizeformat(self.max_upload_size), filesizeformat(data.size)))
        except AttributeError:
            pass

        return data

class NewsLetterForm(forms.Form):
    email = forms.EmailField(max_length=250, required=True)

class FreeConsultationRequestForm(forms.Form):
    name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250,required=True)
    phone = forms.CharField(required=False, max_length=17)
    school = forms.CharField(required=False, max_length=250)
    address = forms.CharField(required=False, max_length=350)
    subjects = forms.CharField(required=False, max_length=350)
    grade = forms.CharField(required=False, max_length=50)
    details = forms.CharField(required=False, max_length=5000)

class ContactRequestForm(forms.Form):
    name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250,required=True)
    phone = forms.CharField(required=False, max_length=17)
    details = forms.CharField(required=False, max_length=5000)

# forms should be added here
class EmailChangeForm(forms.Form):
    old_email = forms.EmailField(max_length = 100, required = True)
    new_email = forms.EmailField(max_length = 100, required = True)
    new_email_conf = forms.EmailField(max_length = 100, required = True)

class AccountDetailsForm(forms.Form):
    first_name = forms.CharField(max_length = 30, required = True)
    last_name = forms.CharField(max_length = 150, required = True)
    phone_number = forms.CharField(max_length=17, required = False)
    profile_picture = RestrictedImageField(required = False)
    clear_profile_picture = forms.BooleanField(required = False)

class ReportDetailsForm(forms.Form):
    student_id = forms.CharField(required=True)
    date = forms.DateField(required=True)
    hours = forms.FloatField(required=True, validators=[
            MinValueValidator(0),
            MaxValueValidator(24)
        ])
    session_comments = forms.CharField(required=True, max_length=5000)

class ReceiptForm(forms.Form):
    name = forms.CharField(required=True, max_length=250)
    email = forms.EmailField(required=True)
    date = forms.DateField(required=False)
    amount = forms.FloatField(required=True, validators=[
            MinValueValidator(0)
        ])

class ProfitCalculatorForm(forms.Form):
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)
