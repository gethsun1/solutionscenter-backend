from django.urls import path, include
from rest_framework.routers import DefaultRouter  # Add this import
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.solution_views import SolutionViewSet
from .views.auth_views import RegisterView, LoginView
from .views.password_reset_views import PasswordResetView, PasswordResetConfirmView

# Registering viewsets with router
router = DefaultRouter()
router.register(r'solutions', SolutionViewSet)

# Define the URL patterns
urlpatterns = [
    # Solution endpoints
    path('', include(router.urls)),

    # Auth endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    # Token JWT Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Password Reset endpoints
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
