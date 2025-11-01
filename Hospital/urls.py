# Hospital/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views  # agar Hospital ke andar koi view hai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),   # home view ke liye
    path('signup/', views.signup_view, name='signup'),  # <-- ye hona chahiye
]
# Hospital/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Appointment.urls')),  # include correct app’s URL
]
