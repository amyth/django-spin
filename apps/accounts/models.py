from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext as _


class Account(AbstractBaseUser):
    """
    Represents an account model. This model contains
    all the information related to an account.
    """

    identifier = models.CharField(_('identifier'), max_length=40, unique=True)
    phone = models.CharField(_('phone'), max_length=14)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @property
    def primary_email(self):
        return self.emails.filter(primary=True).first()


class Email(models.Model):
    """
    Represents an email address model.
    """

    email = models.EmailField(_('email'), unique=True)
    account = models.ForeignKey(Account, related_name=_('emails'))
    primary = models.BooleanField(_('primary'), default=False)
    verified = models.BooleanField(_('verified'), default=False)

    def __unicode__(self):
        return u'%s' % self.email

    def save(self, *args, **kwargs):
        return super(Email, self).save(*args, **kwargs)


class Address(models.Model):
    """
    Represents an address object.
    """

    address_line_1 = models.CharField(_('address line 1'), max_length=150)
    address_line_2 = models.CharField(_('address line 2'), max_length=150, blank=True)
    city = models.CharField(_('city'), max_length=150)
    state = models.CharField(_('state'), max_length=150)
    pin_code = models.CharField(_('pin code'), max_length=7)
    primary = models.BooleanField(_('primary'), default=False)
    account = models.ForeignKey(Account, related_name='addresses')
