from django.contrib import admin


from .models import (
    Category,
    Product,
    Variant,
    VariantProperties,
    ProductProperty,
    Subscription,
)


class CategoryAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class ProductPropertyAdmin(admin.ModelAdmin):
    pass

class VariantAdmin(admin.ModelAdmin):
    pass

class VariantPropertiesAdmin(admin.ModelAdmin):
    pass

class SubscriptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductProperty, ProductPropertyAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(VariantProperties, VariantPropertiesAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
