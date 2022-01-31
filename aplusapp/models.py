from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django_resized import ResizedImageField
import os

# define a aplus user manager
class APlusUserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

# defines a beam user
class APlusUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    profile_picture = ResizedImageField(default=settings.DEFAULT_PROFILE_PICTURE, size=[500, 500])
    phone_number = models.CharField(null=True, blank=True, max_length=17)
    is_a_tutor = models.BooleanField(default=False)
    is_an_exec = models.BooleanField(default=False)
    is_a_student = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = APlusUserManager()

    def set_pic_to_default(self):
        if (self.profile_picture.name != settings.DEFAULT_PROFILE_PICTURE):
            self.profile_picture.delete()
        self.profile_picture = settings.DEFAULT_PROFILE_PICTURE
        self.save()

    def __str__(self):
        return self.email

# defines a subscription email
class NewsLetterSubscription(models.Model):
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.email

# defines a free consultation entry
class FreeConsultationRequest(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(null=True, blank=True, max_length=17)
    school = models.CharField(null=True, blank=True, max_length=250)
    address = models.CharField(null=True, blank=True, max_length=350)
    subjects = models.CharField(null=True, blank=True, max_length=350)
    grade = models.CharField(null=True, blank=True, max_length=50)
    details = models.CharField(null=True, blank=True, max_length=5000)

    def __str__(self):
        return self.name

# defines a contact entry
class ContactRequest(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(null=True, blank=True, max_length=17)
    details = models.CharField(null=True, blank=True, max_length=5000)

    def __str__(self):
        return self.name

# defines a tutor
class Tutor(models.Model):
    user = models.ForeignKey(APlusUser, on_delete=models.CASCADE)
    subjects_tutoring = models.CharField(max_length=1000, blank=True, null=True)
    hours_tutored = models.FloatField(default=0)
    hours_tutored_this_month = models.FloatField(default=0)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

# defines a client
class Student(models.Model):
    user = models.ForeignKey(APlusUser, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField(max_length=250)
    phone = models.CharField(null=True, blank=True, max_length=17)
    school = models.CharField(null=True, blank=True, max_length=250)
    grade = models.CharField(null=True, blank=True, max_length=50)
    aplus_id = models.CharField(max_length=250)
    sessional_hours = models.FloatField(default=0)
    hours_of_tutoring_used_this_month = models.FloatField(default=0)
    hourly_charge = models.FloatField(default=0)

    def __str__(self):
       return self.first_name + " " + self.last_name

# defines a tutor student relationship
class StudentTutoredByTutor(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor_rate = models.FloatField(default=0)

    def __str__(self):
        return self.tutor.user.first_name + " " + self.tutor.user.last_name + " - Student: " + self.student.first_name + " " + self.student.last_name

# defines a report object
class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    date_added = models.DateField(null=True, blank=True)
    number_of_hours = models.FloatField(validators=[
            MaxValueValidator(24),
            MinValueValidator(0)
        ])
    details = models.CharField(null=True, blank=True, max_length=5000)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name + " - " + self.tutor.user.first_name + " " + self.tutor.user.last_name + " - " + str(self.date) + " - " + str(self.number_of_hours)

class Receipt(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    date = models.DateField(null=True, blank=True)
    amount = models.FloatField(validators=[
            MinValueValidator(0)
        ])

    def __str__(self):
        return self.name + " - " + str(self.email) + " - Amount: " + str(self.amount)