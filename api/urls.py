from django.urls import path
from .views import ItemList, ItemDetail, LocationList, LocationDetail

urlpatterns = [
    path('item/', ItemList.as_view(), name='item-list'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('location/', LocationList.as_view(), name='location-list'),
    path('location/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
]