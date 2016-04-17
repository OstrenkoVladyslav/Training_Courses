from django.shortcuts import render,  get_object_or_404
from django.views.generic.detail import DetailView
from coaches.models import Coach
from courses.models import Course

class CoachDetailView(DetailView):
    model = Coach
    is_coach = []
    for i in Course.objects.all():
        if i.coach == object:
            is_coach.append(i)
    def get_context_data(self, **kwargs):
        context = super(CoachDetailView, self).get_context_data(**kwargs)
        context['courses'] = is_coach
        return context
