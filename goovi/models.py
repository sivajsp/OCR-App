from django.db import models

class goovi_db(models.Model):
    name = models.CharField(max_length=50,primary_key = True)
    data = models.TextField()
    file = models.ImageField(upload_to='files')
