from django.shortcuts import render_to_response
from .models import Work
from .models import Education
from .models import About
import datetime


# Create your views here.
def main_page(request):
    aboutme = About.objects.all()
    return render_to_response('index.html', {'aboutme': aboutme})


def education(request):
    edu = Education.objects.all()
    return render_to_response('education.html', {'edu': edu})


def work(request):
    workplaces = Work.objects.all()
    return render_to_response('work.html', {'workplaces': workplaces})
