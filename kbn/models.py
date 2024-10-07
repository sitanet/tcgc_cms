from django.db import models

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('ST', 'Student'),
        ('CA', 'Career'),
        ('BU', 'Business'),
    ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
  
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='ST',
    )

    def __str__(self):
        return self.title





class YouTubeVideo(models.Model):
    CATEGORY_CHOICES = [
        ('ST', 'Student'),
        ('CA', 'Career'),
        ('BU', 'Business'),
    ]
        
    title = models.CharField(max_length=255)
    link = models.URLField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='ST',
    )

    def __str__(self):
        return self.title
