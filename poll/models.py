from django.db import models
from django.utils import timezone
from accounts.models import User


class Poll(models.Model):
    question = models.CharField(verbose_name='سوال', max_length=30)
    active = models.BooleanField(verbose_name='فعال / غیرفعال', default=False)
    create = models.DateTimeField(verbose_name='زمان ساخت', default=timezone.now)

    class Meta:
        verbose_name = 'نظرسنجی'
        verbose_name_plural = '1. نظرسنجی ها'
        ordering = ('-create',)

    def __str__(self):
        return self.question

    @property
    def all_count(self):
        return Poll.objects.count()


class PollOptions(models.Model):
    poll = models.ForeignKey(Poll, verbose_name='برای نظرسنجی', on_delete=models.CASCADE, related_name='poll_option')
    option = models.CharField(verbose_name='گزینه', max_length=30)
    voters = models.ManyToManyField(User, verbose_name='رای دهندگان', blank=True)
    
    class Meta:
        verbose_name = 'گزینه'
        verbose_name_plural = '2. گزینه ها'

    def __str__(self):
        return self.option
