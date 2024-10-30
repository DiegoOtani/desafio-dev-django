from rest_framework import viewsets
from .models import PersonalInfo, WorkExperience, AcademicTraining, ContactInfo
from .serializers import PersonalInfoSerializer, WorkExperienceSerializer, AcademicTrainingSerializer, ContactInfoSerializer
from .pagination import PersonalInfoPagination

class PersonalInfoViewSet(viewsets.ModelViewSet):
  queryset = PersonalInfo.objects.all()
  serializer_class = PersonalInfoSerializer
  pagination_class = PersonalInfoPagination

class ContactInfoViewSet(viewsets.ModelViewSet):
  queryset = ContactInfo.objects.all()
  serializer_class = ContactInfoSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
  queryset = WorkExperience.objects.all()
  serializer_class = WorkExperienceSerializer

class AcademicTrainingViewSet(viewsets.ModelViewSet):
  queryset = AcademicTraining.objects.all()
  serializer_class = AcademicTrainingSerializer