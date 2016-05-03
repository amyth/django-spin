from django.contrib import admin

from .models import Account, Email, Address


class AccountAdmin(admin.ModelAdmin):
    pass

class EmailAdmin(admin.ModelAdmin):
    pass

class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Account, AccountAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Address, AddressAdmin)
