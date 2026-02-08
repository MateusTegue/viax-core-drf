import uuid
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

# Function to determine the upload path for blog post thumbnails
def blog_thumbnail_directory(instance, filename):
    return "blog/{0}:{1}".format(instance.title, filename)

# Function to determine the upload path for category thumbnails
def category_thumbnail_directory(instance, filename):
    return "blog_category/{0}:{1}".format(instance.name, filename)

# Model for blog post categories
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(max_length=256, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=category_thumbnail_directory)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

# Model for blog posts
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    status_options = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    content = CKEditor5Field('Content',config_name='default')
    thumbnail = models.ImageField(upload_to=blog_thumbnail_directory)
    keywords = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=status_options, default='draft')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()  
    postObjects = PostObjects()  
    class Meta:
        ordering = ("status","-created_at")

    def __str__(self):
        return self.title
    
# Model for headings within a blog post
class Heading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='headings')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    level = models.IntegerField(
        choices=(
            (1, 'H1'), 
            (2, 'H2'), 
            (3, 'H3'), 
            (4, 'H4'), 
            (5, 'H5'), 
            (6, 'H6'),
        )
    )
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def __str__(self):
        return self.title
       
       