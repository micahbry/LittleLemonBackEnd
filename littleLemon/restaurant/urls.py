from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, MenuItemView, SingleMenuItemView, BookingViewSet
# Import obtain_auth_token
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'menus', MenuViewSet)
router.register('api/menus', MenuViewSet, basename='menu')
router.register('api/bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('menu/items/', MenuItemView.as_view(), name='menu-list-create'),
    path('menu/items/<int:pk>/', SingleMenuItemView.as_view(),
         name='menu-retrieve-update-delete'),
    path('api-token-auth/', obtain_auth_token),
]
