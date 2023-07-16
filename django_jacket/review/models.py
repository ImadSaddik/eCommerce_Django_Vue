from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    product = models.ForeignKey('product.Product', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)
        
    def __str__(self):
        return f'{self.product.slug}'
    
    def get_absolute_url(self):
        return f'/reviews/{self.product.slug}'
    