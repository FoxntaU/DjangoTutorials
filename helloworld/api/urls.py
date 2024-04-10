from django.urls import path
from .views import ProductList, CommentList

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('comments/', CommentList.as_view(), name='comment-list'),
]