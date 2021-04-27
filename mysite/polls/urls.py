from django.urls import path

from . import views
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('results/', results, name='results'),
]