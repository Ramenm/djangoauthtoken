from django.urls import path
from .views import UserList, UserDetail
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('api-token-auth/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify')
]
