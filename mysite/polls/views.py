from urllib import request


from django.shortcuts import render, redirect
from .models import Feedback, Comment


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'polls/index.html', data)


def about(request):
    return render(request, 'polls/about.html')


def feedback(request):
    return render(request, 'polls/feedback.html')


def create_2(request):

    feedback = Feedback()
    feedback.name = request.POST.get("name")
    feedback.surname = request.POST.get("surname")
    feedback.email = request.POST.get("email")
    feedback.message = request.POST.get("message")
    feedback.save()
    return redirect('/')


def table(request):
    table = Feedback.objects.all()
    table2 = Comment.objects.all()
    context = {'table': table,
             'table2': table2}
    return render(request, 'polls/reviews.html', context)

# Create your views here.
