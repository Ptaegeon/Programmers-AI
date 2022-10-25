from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path("", views.index),
    path("coffee/", views.coffee_view, name = 'coffee'),
    path("coffee/<int:question_id>/", views.detail, name = 'detail'),
    ]
