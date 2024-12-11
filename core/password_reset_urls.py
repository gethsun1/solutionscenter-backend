from django.urls import path
from .views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('request/', PasswordResetView.as_view(), name='password-reset-request'),
    path('confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
