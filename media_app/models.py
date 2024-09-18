from django.db import models


class AudioManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(media_type='audio')


class VideoManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(media_type='video')


class ImageManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(media_type='image')


class Media(models.Model):
    MEDIA_CHOICES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('image', 'Image'),
    ]

    name = models.CharField(max_length=150, blank=False, null=False)
    media_type = models.CharField(
        max_length=10, choices=MEDIA_CHOICES, blank=False, null=False)
    format = models.CharField(max_length=10, blank=False, null=False)
    size_mb = models.IntegerField(blank=False, null=False)
    duration_secs = models.IntegerField(default=0, null=False)

    audio = AudioManager()
    video = VideoManager()
    image = ImageManager()

    def __str__(self) -> str:
        return f"{self.name}-{self.media_type}-{self.format}-{self.size_mb}-{self.duration_secs}"
