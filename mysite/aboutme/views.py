from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'index.html', {})

def education(request):
    return render(request, 'education.html', {})

def work(request):
    return render(request, 'work.html', {})
