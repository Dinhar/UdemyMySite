from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"
    
class Post(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True, null=False, db_index=True)
    image_name = models.CharField(max_length=30, null=True)
    date = models.DateField(auto_now=True)
    excerpt = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"
    