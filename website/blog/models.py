from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    #tags = models. Como colocar tags
    date_added = models.DateTimeField(  auto_now_add=True)

    def __str__(self):
        return self.title
    
    #???
    class Meta():
        ordering = ['-date_added']

    
