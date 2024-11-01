from rest_framework import serializers
from .models import PersonalInfo, WorkExperience, AcademicTraining, ContactInfo

class ContactInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactInfo
    fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
  class Meta:
    model = WorkExperience
    fields = '__all__'

  def validate(self, data):
    if data.get('end_date') and data.get('end_date') < data.get('start_date'):
      raise serializers.ValidationError("A data de término não pode ser anterior a data de início.")
    return data

class AcademicTrainingSerializer(serializers.ModelSerializer):
  class Meta:
    model = AcademicTraining
    fields = '__all__'

  def validate(self, data):
    if data.get('end_date') and data.get('end_date') < data.get('start_date'):
      raise serializers.ValidationError("A data de término não pode ser anterior a data de início.")
    return data

class PersonalInfoSerializer(serializers.ModelSerializer):
  contact_info = ContactInfoSerializer(read_only=True)
  work_experience = WorkExperienceSerializer(many=True, read_only=True)
  academic_training = AcademicTrainingSerializer(many=True, read_only=True)

  class Meta:
    model = PersonalInfo
    fields = '__all__'