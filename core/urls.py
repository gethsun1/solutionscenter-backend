from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.solution_views import SolutionViewSet  # Fix the import path here
from .views.auth_views import RegisterView, LoginView  # Corrected imports for other views
from .views.password_reset_views import PasswordResetView, PasswordResetConfirmView  # Corrected imports

router = DefaultRouter()
router.register(r'solutions', SolutionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
