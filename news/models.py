from django.db import models

class SearchNews(models.Model):
    title = models.CharField(max_length = 200)
    link = models.URLField()
    img = models.URLField(null=True)
    content = models.TextField(max_length=300)
    etc = models.CharField(max_length = 150)

    def __str__(self):
        return str(self.title)