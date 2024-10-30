from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalInfoViewSet, WorkExperienceViewSet, AcademicTrainingViewSet

router = DefaultRouter()
router.register(r'personal-info', PersonalInfoViewSet)
router.register(r'work-experience', WorkExperienceViewSet)
router.register(r'academic-training', AcademicTrainingViewSet)

urlpatterns = [
  path('', include(router.urls))
]