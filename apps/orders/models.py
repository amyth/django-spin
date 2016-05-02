from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _


class Order(models.Model):
    """
    Represents an order model.
    """

    STATUSES = (
        (0, 'Received'),
        (1, 'Processing'),
        (2, 'Shipped'),
        (3, 'Delivered')
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    recurring = models.BooleanField(_('recurring'), default=False)
    subscriptions = models.ManyToManyField('catalog.Subscription',
            related_name='subscription_orders')
    products = models.ManyToManyField('catalog.Variant',
            related_name='product_orders')
    customer = models.ForeignKey('accounts.Account', related_name=_('orders'))
    shipped_to = models.ForeignKey('accounts.Address', )

    @property
    def order_id(self):
        return "%s%s" % (settings.ORDER_PREFIX, self.id)
