from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name="home"),
    path('increment/', views.increment_counter, name='increment_counter'),
    path('generate-image/', views.generate_image, name='generate_image'),
]