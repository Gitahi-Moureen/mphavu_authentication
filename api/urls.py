

from django.urls import path
from django.contrib import admin
from user.views import RegisterUser, LoginUser, ResetPasswordView, DeleteUser, UserListView, UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserListView.as_view(), name='user_list'),  
    path('user/<int:id>/', UserDetailView.as_view(), name='user_detail'),
    path('user/register/', RegisterUser.as_view(), name='register'),
    path('user/login/', LoginUser.as_view(), name='login'), 
    path('user/reset_password/', ResetPasswordView.as_view(), name='reset_password'), 
    path('api/user/', UserListView.as_view(), name='user-list'),
]
