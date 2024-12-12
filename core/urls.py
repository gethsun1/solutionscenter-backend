# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.solution_views import SolutionViewSet
from .views.auth_views import RegisterView, LoginView
from .views.password_reset_views import PasswordResetView, PasswordResetConfirmView

router = DefaultRouter()
router.register(r'solutions', SolutionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
