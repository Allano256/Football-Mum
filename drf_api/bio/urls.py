from django.urls import path
from bio  import views

urlpatterns = [
    path('bios/',views.BioList.as_view()),
]
