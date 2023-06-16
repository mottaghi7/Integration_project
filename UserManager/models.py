from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from activity_log.models import UserMixin as UserActivityLogMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        if not email:
            raise ValueError('ایمیل برای کاربر باید وارد شود.')
        if not first_name:
            raise ValueError('نام برای کاربر باید وارد شود.')
        if not last_name:
            raise ValueError('نام خانوادگی برای کاربر باید وارد شود.')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, **extra_fields)


class User(AbstractUser, UserActivityLogMixin):
    username = None
    email = models.EmailField(_('ایمیل'), unique=True)
    phone = models.IntegerField(_('شماره تلفن'), blank=True, null=True)
    avatar = models.ImageField(_('تصویر'), upload_to='user/avatar', blank=True, null=True)
    student_id = models.IntegerField(_('شماره دانشجویی'), unique=True, blank=True, null=True)
    is_email_confirm = models.BooleanField(_('ایمیل تایید شده'), default=False)
    is_student_id_confirm = models.BooleanField(_('شماره دانشجویی تایید شده'), default=False)
    is_phone_confirm = models.BooleanField(_('شماره تلفن تایید شده'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()
