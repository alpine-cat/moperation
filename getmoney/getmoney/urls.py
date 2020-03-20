from rest_framework import routers
from rest_framework.authtoken import views
from .views import AdvViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'advertisements', AdvViewSet)
