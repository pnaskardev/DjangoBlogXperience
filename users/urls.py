from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r"register", views.UserViewSet)

urlpatterns = [
    path('register/', views.UserViewSet.as_view({'post': 'create'}), name="register"),
    path('me/', views.CurrentUserView.as_view(), name="me"),
    path('login/', TokenObtainPairView.as_view(), name="token-obtain"),
    path('refresh/', TokenRefreshView.as_view(), name="token-refresh"),
]
