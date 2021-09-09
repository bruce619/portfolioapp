from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=200)
    email = models.EmailField(verbose_name=_('Email'))
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15)
    subject = models.CharField(verbose_name=_('Subject'), max_length=300)
    message = models.TextField(verbose_name=_('Message'))


