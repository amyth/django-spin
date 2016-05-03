from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext as _


class AccountManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not phone:
            raise ValueError("Users must have a phone number")

        user = self.model(email=email, phone=phone)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone, password):
        user = self.create_user(email, phone, password=password)
        user.is_admin = True
        user.save(using=self._db)

        return user

class Account(AbstractBaseUser):
    """
    Represents an account model. This model contains
    all the information related to an account.
    """

    email = models.EmailField(_('email'), max_length=255, unique=True)
    phone = models.CharField(_('phone'), max_length=14)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = AccountManager()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

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
