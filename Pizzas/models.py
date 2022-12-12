from django.db import models

# Create your models here.
class Pizza(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Toppings'
    


    def __str__(self):
        return f"{self.text[:50]}...."




#Testing Comments:
class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True,blank=True)

    class Meta: 
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.text[:200]}"



class Image(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')