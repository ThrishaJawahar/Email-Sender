from django.contrib import admin
from django.urls import path
from Emailapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_email/', views.send_email, name='send_email'),
]
