from django.urls import path

from . import views

urlpatterns = [
    path("", views.greet, name="greet"),
    path("search", views.search, name="search"),
]
