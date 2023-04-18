
from django.db import models
from django.contrib.auth.models import User


class Ceremony(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    date = models.DateField(verbose_name='تاریخ')
    location = models.CharField(max_length=100, verbose_name='محل')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'مراسم'
        verbose_name_plural = 'مراسم‌ها'


class Participant(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    ceremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE, related_name='participants', verbose_name='مراسم')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='کاربر')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'شرکت کننده'
        verbose_name_plural = 'شرکت کنندگان'