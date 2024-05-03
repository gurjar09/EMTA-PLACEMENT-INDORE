
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('EMTA_APP.urls')),
    path('admin/', admin.site.urls),
]
