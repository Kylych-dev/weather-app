from django.db import models

nb = dict(null=True, blank=True)


class Menu(models.Model):
    name = models.CharField(max_length=50)
    menu_name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        **nb,
        related_name='children',
        on_delete=models.PROTECT
    )
    url = models.CharField(
        max_length=200,
        **nb,
        verbose_name='url'
    )
    named_url = models.CharField(
        max_length=50,
        **nb,
        verbose_name='named_url'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' > '.join(full_path[::-1])

