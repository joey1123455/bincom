
from django.urls import path, include

from . views import *


urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/update/', UpdateProfileView.as_view(), name='update-profile'),
]