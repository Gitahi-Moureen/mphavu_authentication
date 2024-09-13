


from django.contrib import admin
from django.urls import path, include
from api.views import RegisterUser, LoginUser, ResetPasswordView, UserListView, UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UserListView.as_view(), name='user_list'),  # Handles /api/user/ for listing users
    path('api/user/<int:id>/', UserDetailView.as_view(), name='user_detail'),  # Handles /api/user/<id>/ for user details
    path('api/user/register/', RegisterUser.as_view(), name='register'),  # Handles /api/user/register/ for registration
    path('api/user/login/', LoginUser.as_view(), name='login'),  # Handles /api/user/login/ for login
    path('api/user/reset_password/', ResetPasswordView.as_view(), name='reset_password'),  # Handles /api/user/reset_password/ for password reset
    path('accounts/', include('allauth.urls')),  # Ensure allauth is properly configured
    path('auth/', include('authentication.urls')),  # Ensure authentication URLs are properly configured
]
