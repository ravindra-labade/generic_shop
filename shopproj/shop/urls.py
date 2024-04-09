from django.urls import path
from .views import Add_shop, List_shop, Detail_shop, Update_shop, Delete_shop

urlpatterns = [
    path('add/', Add_shop.as_view()),
    path('list/', List_shop.as_view()),
    path('detail/<int:pk>/', Detail_shop.as_view()),
    path('update/<int:pk>/', Update_shop.as_view()),
    path('delete/<int:pk>/', Delete_shop.as_view()),
]
