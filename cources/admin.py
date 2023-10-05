from django.contrib import admin
from .models import Product, Lesson, LessonView

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_link', 'duration_seconds',)

@admin.register(LessonView)
class LessonViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'view_time_seconds', 'is_completed',)
