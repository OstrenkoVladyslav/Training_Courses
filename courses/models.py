from django.db import models

from coaches.models import Coach

class Course(models.Model):
    """Course class"""
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description =  models.TextField()
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')

    def __str__(self):
        return self.name

class Lesson(models.Model):
    """Lesson class"""
    subject = models.CharField(max_length=255)
    description =  models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject
