from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SolutionViewSet

router = DefaultRouter()
router.register(r'solutions', SolutionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
