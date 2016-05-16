from django.contrib import admin

from .models import (
    Featured,
    Store
)


class StoreAdmin(admin.ModelAdmin):
    pass


class FeaturedAdmin(admin.ModelAdmin):
    pass


admin.site.register(Store, StoreAdmin)
admin.site.register(Featured, FeaturedAdmin)
