from django.db import models


class Publication(models.Model):
    soouce = models.CharField(max_length=100, blank =True, null=True,verbose_name="Source")
    author = models.CharField(max_length=100, blank =True, null=True,verbose_name="Author")
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Title")
    description = models.CharField(max_length=100, blank =True, null=True,verbose_name="Description")
    image = models.CharField(max_length=100, blank =True, null=True,verbose_name="Image")
    content=models.TextField(max_length=100, blank =True, null=True,verbose_name="Content")
    link= models.CharField(max_length=100, blank =True, null=True,verbose_name="Link")
    date_published=models.DateTimeField(null=True)

    class Meta:
        verbose_name = "Publication"

    def __str__(self):
        return str(self.title)
