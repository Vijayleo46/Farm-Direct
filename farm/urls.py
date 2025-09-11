from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from farm import settings

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('shop/',include('shop.urls'))
=======
    path('',include('shop.urls'))
>>>>>>> 3528a25 (Add requirements.txt)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
