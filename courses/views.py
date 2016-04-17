#-*-coding: utf-8-*-
from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.core.urlresolvers import reverse_lazy, reverse
from courses.models import Course, Lesson
from django import forms
import logging
logger = logging.getLogger('courses')

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'
    def get_context_data(self, **kwargs):
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        return super(CourseDetailView, self).get_context_data(**kwargs)

class CourseCreateView(CreateView):
    model = Course
    fields = ['name','short_description','description','coach']
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'course'
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Course creation"
        return context
    def form_valid(self, form):
        messages.success(self.request, u'Course %s has been successfully added.' %(form.instance.name))
        return super(CourseCreateView, self).form_valid(form)

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name','short_description','description','coach']
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Course update"
        return context
    template_name = 'courses/edit.html'
    context_object_name = 'course'
    def get_success_url(self, **kwargs):
        return reverse_lazy('index')
    def form_valid(self, form):
        messages.success(self.request, u'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

class CourseDeleteView(DeleteView):
    model = Course
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Course deletion"
        return context
    def delete(self, request, pk, *args, **kwargs):
        course = Course.objects.get(id=pk)
        messages.success(self.request, u'Course %s has been deleted.' %(course.name))
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    context_object_name = 'course'

class LessonCreateView(CreateView):
    model = Lesson
    fields = ['subject','description','course']
    success_url = reverse_lazy('index')
    template_name = 'courses/add_lesson.html'
    context_object_name = 'lesson'
    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Lesson creation"
        return context
    def form_valid(self, form):
        messages.success(self.request, u'Lesson %s has been successfully added.' %(form.instance.subject))
        return super(LessonCreateView, self).form_valid(form)

def add_lesson(request, course_id):
    if request.POST:
        form = LessonModelForm(request.POST)
        if form.is_valid():
            less = form.save()
            text = "Lesson {0} has been successfully added.".format(form.cleaned_data['subject'])
            messages.success(request, text)
            return redirect('courses:detail', less.course.id)
    else:
        cd = Course.objects.get(id=course_id)
        form = LessonModelForm(initial={'course': cd})
    return render(request, 'courses/add_lesson.html', {'form': form})
