from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    modified_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Category, self).save(*args, **kwargs)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField(max_length=50)
    due_date = models.DateTimeField(auto_now_add=True,null=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    modified_at = models.DateTimeField(auto_now_add=True,null=True) 

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Item, self).save(*args, **kwargs)
