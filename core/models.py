from django.db import models



class Source(models.Model):
    name = models.CharField(max_length=100, blank =True, null=True,verbose_name="name")
    logo = models.CharField(max_length=100, blank =True, null=True,verbose_name="logo")
    link = models.CharField(max_length=100, blank =True, null=True,verbose_name="link")
    feed_link=models.CharField(max_length=100, blank =True, null=True,verbose_name="Feed link")
    laste_updted=models.DateTimeField(null=True,blank=True)

    class Meta:
        verbose_name = "Source"

    def __str__(self):
        return str(self.name)


class Publication(models.Model):

    source = models.ForeignKey(Source,on_delete=models.CASCADE)
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

