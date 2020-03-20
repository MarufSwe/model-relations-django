from django.db import models


class ProjectManager(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=25)
    project_manager = models.ForeignKey(ProjectManager, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ManyToManyField(Teacher)

    def teachers(self):
        teacher_list = []
        for teacher in self.teacher.all():
            teacher_list.append(teacher.name)

        return ','.join(teacher_list)

    def __str__(self):
        return self.name
