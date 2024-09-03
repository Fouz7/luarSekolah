from django.urls import path
from api.views.users_views import UserListCreateAPIView
from api.views.categories_views import CategoryListAPIView
from api.views.login_views import LoginAPIView
from api.views.roles_views import RoleListAPIView
from api.views.datapelatihan_views import DataPelatihanListCreateAPIView, PurchaseDataPelatihanAPIView
from api.views.pelatihanku_views import PelatihanKuListAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('roles/', RoleListAPIView.as_view(), name='role-list'),
    path('datapelatihan/', DataPelatihanListCreateAPIView.as_view(), name='datapelatihan-list-create'),
    path('purchase/', PurchaseDataPelatihanAPIView.as_view(), name='purchase'),
    path('pelatihanku/', PelatihanKuListAPIView.as_view(), name='pelatihanku-list'),
]