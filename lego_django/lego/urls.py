from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # path("files/", views.files, name="files"),
    # path('upload/', views.fileupload, name="upload"),
    # path('upload_image/', views.upload_image, name="upload_image")
]

if settings.DEBUG:  # media URL for debug purpose
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
