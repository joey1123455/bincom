from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Song(models.Model):
    title= models.CharField(max_length=100)
    artist= models.TextField()
    image= models.ImageField(upload_to='uploads/music/thumb_nail',blank=True,null=True)
    audio_file = models.FileField(upload_to='uploads/music/song',blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title