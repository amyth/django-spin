from django.db import models
from django.utils.translation import ugettext as _

class Category(models.Model):

    LEVELS = (
        (0, 'Top Level'),
        (1, 'Sub Category'),
        (3, 'Category')
    )

    name = models.CharField(max_length=140)
    parent = models.ForeignKey('self', blank=True, null=True,
            related_name='children')
    level = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.level)


class Product(models.Model):
    """
    Represents a product object. This will contain all the
    basic product information.
    """

    sku = models.CharField(_('SKU'), max_length=30)
    title = models.CharField(_('title'), max_length=140)
    description = models.TextField(_('description'))
    price = models.BigIntegerField(_('price'))
    category = models.ForeignKey(Category,
            related_name=_('products'))

    def __unicode__(self):
        return u'%s' % self.title


class Variant(models.Model):
    """
    Represents a product variant.
    """

    product = models.ForeignKey(Product, related_name=_('variants'))
    price = models.BigIntegerField(_('price'), blank=True, null=True)
    stores = models.ManyToManyField('home.Store')
    quantity = models.BigIntegerField(default=0)
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % self.product.title


class VariantImage(models.Model):
    """
    Represents a variant image.
    """

    variant = models.ForeignKey(Variant)
    image = models.ImageField(upload_to="media/images/products/")


class ProductProperty(models.Model):
    """
    Represents a product object.
    """

    class Meta:
        verbose_name_plural = _('Product Properties')

    PT_SINGLE_VALUE = 0

    PROPERTY_TYPES = (
        (PT_SINGLE_VALUE, 'Single Value'),
    )

    name = models.CharField(_('name'), max_length=40)
    product = models.ForeignKey(Product, related_name=_('properties'))
    property_type = models.IntegerField(_('property type'),
            default=PT_SINGLE_VALUE, choices=PROPERTY_TYPES)

    def __unicode__(self):
        return u'%s' % self.name


class VariantProperties(models.Model):
    product_property = models.ForeignKey(ProductProperty)
    value = models.CharField(_('value'), max_length=100)

    def __unicode__(self):
        return u'%s' % self.product_property.name


class Subscription(models.Model):
    """
    Represents the subscription object.
    """

    name = models.CharField(_('name'), max_length=140)
    products = models.ManyToManyField(Product, related_name=_('subscriptions'))
    price = models.BigIntegerField(_('price'))
    deliveries = models.IntegerField()
    valid_for_days = models.IntegerField(default=7)
