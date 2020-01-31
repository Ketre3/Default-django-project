from django.urls import path

from .views import (
    RegisterView,
    Login,
    Logout,
    confirm_account,
    UserInfo
)

app_name = 'account'
urlpatterns = [
    path('', UserInfo.as_view(), name='info'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('confirm/<int:pk>', confirm_account, name='confirm'),
]
