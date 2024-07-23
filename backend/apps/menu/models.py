from django.db import models

nb = dict(null=True, blank=True)


class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self',
        **nb,
        related_name='children'
    )

    def __str__(self):
        return self.name