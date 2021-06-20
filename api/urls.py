from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    PatientCreateListAPIView,
    PatientRetrieveUpdateAPIView,
    HealthOfficerRetrieveUpdateAPIView,
    HealthOfficerCreateListAPIView,
    MedicalRecordListCreateAPIView,
    MedicalRecordRetrieveUpdateAPIView,
    HospitalCreateListAPIView,
    HospitalRetrieveUpdateAPIView
)


urlpatterns = [
    path(
         'user/patients/',
         PatientCreateListAPIView.as_view(),
         name='patient-list-create'
    ),
    path(
         'user/patients/<str:uuid>/',
         PatientRetrieveUpdateAPIView.as_view(),
         name='patient-get-update'
    ),


    path(
         "user/health-officers/",
         HealthOfficerCreateListAPIView.as_view(),
         name="health-officer-list-create"
    ),
    path(
         "user/health-officers/<str:uuid>/",
         HealthOfficerRetrieveUpdateAPIView.as_view(),
         name="health-officer-get-update"
    ),

    path(
        'user/patients/<str:uuid>/records/',
         MedicalRecordListCreateAPIView.as_view(),
         name='medical-record-get-create'
    ),

    path(
        'user/patients/<str:uuid1>/records/<str:uuid2>/',
        MedicalRecordRetrieveUpdateAPIView.as_view(),
        name='medical-record-get-update'
    ),

    path(
        'user/hospitals/',
        HospitalCreateListAPIView.as_view(),
        name='hospital-list-create'
    ),

    path(
        'user/hospital/<str:uuid>/',
        HospitalRetrieveUpdateAPIView.as_view(),
        name='hospital-update'
    ),

    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
