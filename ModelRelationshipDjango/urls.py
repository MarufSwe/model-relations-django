from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.project_manager),
    path('employee',views.employee),
]
