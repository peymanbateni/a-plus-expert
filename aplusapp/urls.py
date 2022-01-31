"""aplusexpert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from aplusapp.views import *
from django.conf.urls import handler404, handler500
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^login/$', user_login),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
        name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
        name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
        name='password_reset_complete'),
    path('about/', aboutHanlder),
    path('', homeHanlder),
    path('home/', homeHanlder),
    path('contact/', contactHanlder),
    path('free-consultation/', freeConsultationHandler),
    path('complete-request/', completeRequestHanlder),
    path('dashboard/', dashboardProfileHanlder),
    path('dashboard/profile/', dashboardProfileHanlder),
    path('dashboard/report/', dashboardReportHandler),
    path('dashboard/student-overview/', dashboardStudentOverviewHandler),
    path('dashboard/tutor-overview/', dashboardTutorOverviewHandler),
    path('dashboard/payments/', dashboardPaymentHandler),
    path('dashboard/profits/', dashboardProfits),
    path('dashboard/your-sessions/', dashboardYourSessionsHandler),
    ]

# Error hanlders
handler404 = error_404
handler500 = error_500