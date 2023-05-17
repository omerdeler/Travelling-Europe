from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug =models.SlugField(null=False,blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Blog(models.Model):
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Ulkeler")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug =models.SlugField(blank=True, unique=True, db_index=True, editable=False)   #blank=True   admin de bu alanı doldurmak zorunlu olmaz, editable=False yazınca bu alan görünmez
    # category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)   #bire cok iliski
    categories = models.ManyToManyField(Category, blank=True)      #coka cok iliski, blank=True demek illaki bu iliskiyi kurmak zorunda degilsin demek

    def __str__(self):
        return f"{self.title}"
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    


class BlogCity(models.Model):
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Ulkeler")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug =models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)   #blank=True   admin de bu alanı doldurmak zorunlu olmaz, editable=False yazınca bu alan görünmez
    category_ulke= models.ForeignKey(Blog, default=1, on_delete=models.CASCADE)   #bire cok iliski
    
    def __str__(self):
        return f"{self.title}"
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)





class TripCity(models.Model):
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Ulkeler")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug =models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)   #blank=True   admin de bu alanı doldurmak zorunlu olmaz, editable=False yazınca bu alan görünmez
    category_city= models.ForeignKey(BlogCity, default=1, on_delete=models.CASCADE)   #bire cok iliski
    
    def __str__(self):
        return f"{self.title}"
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

