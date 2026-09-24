from django.urls import path
from .views import cartView,AddToCartView,UpdateCartItemView,RemoveCartItemView

urlpatterns=[
    path(cartView.as_view()),
    path('add/',AddToCartView.as_view()),
    path('update/',UpdateCartItemView.as_view()),
    path('remove/',RemoveCartItemView.as_view())
]