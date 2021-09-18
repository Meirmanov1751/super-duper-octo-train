from django.conf import settings
from rest_framework.routers import DefaultRouter

from django.urls import path,include
from django.conf.urls.static import static
from note.views import NoteVieset,NoticeVieset

router = DefaultRouter()

router.register(r'note',NoteVieset )
router.register(r'notice',NoticeVieset )

urlpatterns = [
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)