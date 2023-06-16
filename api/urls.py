from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views as api_view

app_name = "api"
router = DefaultRouter()

router.register('user_api', api_view.UserViewSet, basename='user_api')
router.register('login_api', api_view.UserLoginViewSet, basename='login_api')
router.register('logout_api', api_view.UserLogoutViewSet,
                basename='logout_api')


urlpatterns = [
    path('', include(router.urls)),
]
