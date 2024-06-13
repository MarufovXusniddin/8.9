from django.db import models

# Create your models here.


class Lesson(models.Model):
    description = models.TextField()
    lesson_number = models.CharField(max_length=1000)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lesson_number}  |  {self.date}"