from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    LessonListCreateView, LessonDetailView,
    LessonViewListCreateView, LessonViewDetailView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('lessons/', LessonListCreateView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),

    path('lesson-views/', LessonViewListCreateView.as_view(), name='lesson-view-list'),
    path('lesson-views/<int:pk>/', LessonViewDetailView.as_view(), name='lesson-view-detail'),
]
