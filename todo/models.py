from django.db import models

class Todo(models.Model):
    #id is always created be django auto as pk
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title