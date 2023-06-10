from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('about', views.about, name='about'),
	path('create/', views.create_2, name="create_2"),
	path('auth/', include('Auth.urls')),
	path('feedback/', views.feedback, name="feedback"),
	path('reviews/', views.table, name="reviews"),

]
