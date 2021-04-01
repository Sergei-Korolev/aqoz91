from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dynamic_input_form.urls')),
    path('admin/', admin.site.urls),
]
