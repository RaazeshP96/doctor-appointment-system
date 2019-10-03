from django.urls import path
from .views import DoctorList, DoctorDetail

urlpatterns = [
    path('/', DoctorList.as_view(), name='Doctor-list'),
    path('/<int:id>', DoctorDetail.as_view(), name='Doctor-detail')
]
