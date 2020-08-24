from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phone_field import PhoneField

from .managers import CustomUserManager


class CustomUser(AbstractUser):

    COURSE_COORDINATOR = 1
    PROGRAM_COORDINATOR = 2
    TEACHER = 3
    STUDENT = 4

    ROLE_CHOICES = (
        (COURSE_COORDINATOR, 'Course coordintor'),
        (PROGRAM_COORDINATOR, 'Program coordinator'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student')
    )

    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = PhoneField(_("phone"))
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
