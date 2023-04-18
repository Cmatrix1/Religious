from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class User(AbstractUser):
    email = models.EmailField(max_length=199, unique=True, verbose_name=('ایمیل'))
    phone_number = models.CharField(max_length=18, unique=True, verbose_name=('شماره تلفن'))
    is_admin = models.BooleanField(default=False, verbose_name=('ادمین بودن کاربر'))
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='accounts_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='accounts_user_permissions',
    )
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        verbose_name = ('User')
        verbose_name_plural = ('Users')

    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin
