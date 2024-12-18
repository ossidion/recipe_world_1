from django.db import models

from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Recipe(models.Model):
    title = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=25, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="recipe_posts")
    updated_on = models.DateTimeField(auto_now=True)
    ingredients=models.TextField()
    recipe=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to = 'static/images/', height_field=0, width_field=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
