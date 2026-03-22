from django.urls import path
from .views import home, job_list, add_job, apply_job

urlpatterns = [
    path('', home, name='home'),
    path('jobs/', job_list, name='job_list'),
    path('add-job/', add_job, name='add_job'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
]