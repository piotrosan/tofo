from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from base.models import BaseMixin
from user.managers import UserManager
from userprofile.models import Profile


class User(AbstractBaseUser, PermissionsMixin, BaseMixin):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True, unique=True,)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    profile = models.ForeignKey(
        Profile, null=True, blank=True,
        related_name='profile', on_delete=models.CASCADE)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def get_full_name(self):
        return '%s %s'.format(self.first_name, self.last_name).strip()


