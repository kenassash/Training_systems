from rest_framework import generics
from .models import Product, Lesson, LessonView
from .serializers import ProductSerializer, LessonSerializer, LessonViewSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonViewListCreateView(generics.ListCreateAPIView):
    queryset = LessonView.objects.all()
    serializer_class = LessonViewSerializer

    def perform_create(self, serializer):
        # Сохранение объекта LessonView
        instance = serializer.save()

        # Вызов метода set_status_on_percentage для установки статуса is_completed
        instance.set_status_on_percentage()

