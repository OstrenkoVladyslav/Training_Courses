# -*- coding:UTF-8 -*-
from django.shortcuts import render,  get_object_or_404, redirect
from django.db import models
from django.core.paginator import Paginator
from django.views.generic.list import *
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from students.models import Student
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
import logging
logger=logging.getLogger('students')

class StudentListView(ListView):
    model = Student
    paginate_by = 5
    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id = course_id)
        return qs
    context_object_name = 'student_list'

class StudentDetailView(DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        logger.debug("Students detail view has been debugged")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        return super(StudentDetailView, self).get_context_data(**kwargs)

class StudentCreateView(CreateView):
    model = Student
    fields = ['name','surname','date_of_birth','email','phone','address','skype','courses']
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Student registration"
        return context

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','surname','date_of_birth','email','address','skype','courses']
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Student info update"
        return context
    success_url = reverse_lazy('students:list_view')

class StudentDeleteView(DeleteView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Student info suppression"
        return context
    success_url = reverse_lazy('students:list_view')
