from django.shortcuts import render
from .models import ProjectManager, Employee


# Create your views here.

# Lazy Eager loading
def project_manager(request):
    query = ProjectManager.objects
    context = {'pm': query}
    return render(request, context)


def employee(request):
    query = Employee.objects
    return render(request, query)
