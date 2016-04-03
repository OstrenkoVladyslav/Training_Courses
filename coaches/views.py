from django.shortcuts import render,  get_object_or_404
from django.views.generic.detail import DetailView
from coaches.models import Coach
from courses.models import Course

"""def list_view(request):
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id).order_by('id')
        selection = True
    except:
        students = models.Student.objects.all()
        selection = False

    return render(request, 'course_students.html', {'students': students,
        'selection': selection})
"""
"""
def detail(request, coach_id):
    coach = models.Coach.objects.get(id = coach_id)
    is_coach = []
    is_assistant = []
    for i in Course.objects.all():
        if i.coach == coach:
            is_coach.append(i)
        if i.assistant == coach:
            is_assistant.append(i)

    return render(request, 'coaches/detail.html', {
            "is_coach": is_coach,
            "is_assistant": is_assistant,
            "coach": coach
            })
"""

class CoachDetailView(DetailView):
    model = Coach
    print("START")
    is_coach = []
#    coach = models.Coach.objects.get(id = coach_id)
    print("Coach=")
    print(Coach)
    for i in Course.objects.all():
        print("i=")
        print(i)
        print("i.coach=")
        print(i.coach)
        if i.coach == object:
            is_coach.append(i)
            print(i)
        print(is_coach)
    def get_context_data(self, **kwargs):
        context = super(CoachDetailView, self).get_context_data(**kwargs)
        context['courses'] = is_coach
        return context

