from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views import UpdateUserInfoAPI, LoginAPI, LogoutAPI, ValidateResetPasswordTokenAPI, RegisterAPI, ResetPasswordByEmailAPI, ResetPasswordAPI, VerifyEmail


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('emailverify/', VerifyEmail.as_view(), name='emailverify'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('resetpasswordbyemail/', ResetPasswordByEmailAPI.as_view(),
         name='resetpasswordbyemail'),
    path('validateresetpasswordtoken/<uidb64>/<token>/',
         ValidateResetPasswordTokenAPI.as_view(), name='validateresetpasswordtoken'),
    path('resetpassword/', ResetPasswordAPI.as_view(), name='resetpassword'),
    path('updateuserinfo/<int:id>',
         UpdateUserInfoAPI.as_view(), name='updateuserinfo'),
]
