from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    
    class Meta:
        db_table = 'categories'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['id']


class producto(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='producto/', blank=True)
    excerpt = models.TextField(max_length=200, verbose_name='Extracto')
    detail = models.TextField(max_length=1000, verbose_name='informacion del producto')
    price = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'producto'
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['id']



        
