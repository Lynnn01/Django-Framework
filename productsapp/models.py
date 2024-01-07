from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField(default = 0)
    isTrending = models.BooleanField(default = False)
    image = models.ImageField(upload_to="products", blank=True)
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Product_detail", kwargs={"pk": self.pk})
