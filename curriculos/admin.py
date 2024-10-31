from django.contrib import admin
from .models import PersonalInfo, ContactInfo, WorkExperience, AcademicTraining

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('personal_info', 'email', 'phone')
    search_fields = ('email',)

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date')
    search_fields = ('position', 'company')

@admin.register(AcademicTraining)
class AcademicTrainingAdmin(admin.ModelAdmin):
    list_display = ('institution', 'course', 'start_date', 'end_date')
    search_fields = ('institution', 'course')
