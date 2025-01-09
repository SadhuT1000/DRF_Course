from rest_framework.routers import SimpleRouter
from config import settings
from users.apps import UsersConfig
from django.conf.urls.static import static
from django.urls import path
from users.views import UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"", UserViewSet, basename="users")

urlpatterns = [
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
