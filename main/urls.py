from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('portfolio.urls')),  # ✅ ONLY THIS
    path('admin/', admin.site.urls),
]