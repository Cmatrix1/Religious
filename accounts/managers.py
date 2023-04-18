from django.contrib.auth.models import BaseUserManager
from django.db.models import QuerySet



class AdminManager(QuerySet):
    def create_user(self, phone_number, password, email=None):
        if not phone_number:
            raise ValueError('User must have phone number')
        if not password:
            raise ValueError('User must have password')
        user = self.model(
            phone_number=phone_number, email=BaseUserManager.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, phone_number, password, email):
        if not email:
            raise ValueError('User must have email')
        user = self.create_user(phone_number, password, email)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, email):
        user = self.create_admin(phone_number, password, email)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserManager(AdminManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)