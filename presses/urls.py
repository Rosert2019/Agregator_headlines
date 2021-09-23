from django.urls import path

from .views import press_view
  
urlpatterns = [
    path('', press_view, name='press_view' ),
]