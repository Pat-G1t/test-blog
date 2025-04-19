from django.urls import path
from . import views

app_name = 'sondages'
urlpatterns = [ path('choice_json/', views.choice_json),]