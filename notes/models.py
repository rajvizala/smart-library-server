from django.db import models

from server.settings import AUTH_USER_MODEL
# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default="",blank=True)
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="notes")
   
    last_edited = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"Note {self.title} by {self.user}"
