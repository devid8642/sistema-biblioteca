from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('livro/<int:id>/', views.livro, name = 'livro')
]