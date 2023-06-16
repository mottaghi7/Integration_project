from django.urls import path, include
from UserManager import views as user_views

app_name = "UserManager"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signin/', user_views.LoginUserView.as_view(), name='signin'),
    path('signup/', user_views.SignUpUserView.as_view(), name='signup'),
]
