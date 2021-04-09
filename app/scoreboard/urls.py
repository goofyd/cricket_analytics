from django.urls import path
from .views import scorecard

urlpatterns = [
    path('<int:id>', scorecard, name='scorecard')
]