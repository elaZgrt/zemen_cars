from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from cars.views import CarViewSet
from users.views import UserCreateView

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/signup/', UserCreateView.as_view(), name='signup'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
