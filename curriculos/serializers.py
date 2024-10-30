from rest_framework import serializers
from .models import PersonalInfo, WorkExperience, AcademicTraining

class WorkExperienceSerializer(serializers.ModelSerializer):
  class Meta:
    model = WorkExperience
    fields = '__all__'

class AcademicTrainingSerializer(serializers.ModelSerializer):
  class Meta:
    model = AcademicTraining
    fields = '__all__'

class PersonalInfoSerializer(serializers.ModelSerializer):
  work_experience = WorkExperienceSerializer(many=True, read_only=True)
  academic_training = AcademicTrainingSerializer(many=True, read_only=True)

  class Meta:
    model = PersonalInfo
    fields = '__all__'