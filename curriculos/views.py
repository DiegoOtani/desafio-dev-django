from rest_framework import viewsets
from .models import PersonalInfo, WorkExperience, AcademicTraining
from .serializers import PersonalInfoSerializer, WorkExperienceSerializer, AcademicTrainingSerializer

class PersonalInfoViewSet(viewsets.ModelViewSet):
  queryset = PersonalInfo.objects.all()
  serializer_class = PersonalInfoSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
  queryset = WorkExperience.objects.all()
  serializer_class = WorkExperienceSerializer

class AcademicTrainingViewSet(viewsets.ModelViewSet):
  queryset = AcademicTraining.objects.all()
  serializer_class = AcademicTrainingSerializer