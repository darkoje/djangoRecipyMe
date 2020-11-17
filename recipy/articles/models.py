from django.db import models

from tinymce.models import HTMLField

from django.utils.safestring import mark_safe


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    # body = models.TextField()
    body = HTMLField()
    # recipe = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    FEATURED_OPTIONS = (
        ('Y','Yes'),
        ('N','No'),
    )
    featured = models.CharField(max_length=1, choices=FEATURED_OPTIONS, default="N" )

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 65px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title
