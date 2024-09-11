from django.urls import path
from bio  import views

urlpatterns = [
    path('bios/',views.BioList.as_view()),
    path('bios/<int:pk>',views.BioDetail.as_view()),
]
