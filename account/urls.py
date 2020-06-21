from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path('', views.accountOverview, name='account-overview'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.accountRegister, name="account-register"),
    path('update/<int:pk>', views.accountUpdate, name='account-update'),
    path('user/<int:pk>', views.accountUserDetail,
         name='account-user-detail'),
    path('users', views.accountUsers, name='account-user'),
    path('password_reset/', include('django_rest_passwordreset.urls',
                                    namespace='password_reset')),
]
