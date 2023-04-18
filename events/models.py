from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام رویداد')
    date = models.DateField(verbose_name='تاریخ')
    description = models.TextField(blank=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = 'رویدادها'

    def __str__(self):
        return self.name