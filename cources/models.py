from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time_seconds = models.IntegerField()
    is_completed = models.BooleanField(default=False)

    def set_status_on_percentage(self):
        percentage = (self.view_time_seconds / self.lesson.duration_seconds) * 100
        if percentage >= 80:
            self.is_completed = True
        else:
            self.is_completed = False
        self.save()
