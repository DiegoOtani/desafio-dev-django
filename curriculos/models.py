from django.db import models

class PersonalInfo(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  birth_date = models.DateField()

  class Meta:
    ordering = ['id']

class ContactInfo(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, related_name='contact_info', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    address = models.TextField()
    linkedin = models.CharField(max_length=100)

class WorkExperience(models.Model):
  position = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  start_date = models.DateField()
  end_date = models.DateField(null=True, blank=True)
  description = models.TextField()
  personal_info = models.ForeignKey(PersonalInfo, related_name='work_experience', on_delete=models.CASCADE)

class AcademicTraining(models.Model):
  institution = models.CharField(max_length=60)
  course = models.CharField(max_length=60)
  start_date = models.DateField()
  end_date = models.DateField(null=True, blank=True)
  personal_info = models.ForeignKey(PersonalInfo, related_name='academic_training', on_delete=models.CASCADE)