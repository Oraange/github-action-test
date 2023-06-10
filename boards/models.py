from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()

    class Meta:
        db_table = "board"
