from django.urls import path
from . import views

app_name = 'selecao'
urlpatterns = [
    path('home/', views.show_home, name='show_home'),
    path('create/', views.create_message, name='create_message'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('create_p/', views.create_post, name='create-post'),
]

