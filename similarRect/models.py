from django.db import models
from django.db.models.expressions import Window


class Rectangle(models.Model):
    id = models.AutoField(primary_key=True)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    time_created = models.DateTimeField()
    included = models.BooleanField(default=False)
    main = models.BooleanField(default=False)

    def __str__(self):
        s = {"x": -1, "y": -1, "width": 5, "height": 4 , "time": self.time_created.strftime("%d/%m/%y %-H:%-M")}
        return str(s) 