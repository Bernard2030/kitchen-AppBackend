
from django.urls import path,include
from .models import RegisterView



urlpatterns = [
    path('register/', RegisterView.as_view()),

  
    

]
