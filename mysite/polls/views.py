from django.shortcuts import render


def index(request):
	data = {
		'title': 'Главная страница',
	}
	return render(request, 'polls/index.html', data)


def about(request):
	return render(request, 'polls/about.html')


def contacts(request):
	return render(request, 'polls/contacts.html')




# Create your views here.
