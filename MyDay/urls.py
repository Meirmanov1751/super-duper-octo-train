from rest_framework.routers import DefaultRouter
from .routers import router
from django.contrib import admin
from django.urls import path,include

router = DefaultRouter()
router.registry.extend(router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('MyDay.routers')),
]
