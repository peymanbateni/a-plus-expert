from django.contrib import admin
from aplusapp.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
@admin.register(APlusUser)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',
                            'profile_picture', 'phone_number', 'is_a_tutor', 'is_a_student', 'is_an_exec')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(NewsLetterSubscription)
admin.site.register(FreeConsultationRequest)
admin.site.register(ContactRequest)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(StudentTutoredByTutor)
admin.site.register(Report)
admin.site.register(Receipt)