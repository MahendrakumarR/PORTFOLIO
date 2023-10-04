from django.urls import path
from.import views

urlpatterns=[
    path("", views.new, name="new"),
    path("msc/", views.msc, name="msc"),
    path("bsc/", views.bsc, name="bsc") 
]