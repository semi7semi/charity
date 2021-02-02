from django.contrib import admin
from django.contrib.auth.models import User

from charity_app.models import Institution, Category, Donation

# class InstitutionAdmin(admin.ModelAdmin):
#     list_display = ("name", "description", "type")
#     list_editable = ("description", "type")

class InstitutionAdmin(admin.ModelAdmin):
    fields = ["name", "type", "categories"]
    list_display = ("name", "type", "get_categories")

    def get_categories(self, obj):
        return "\n".join([p.name for p in obj.categories.all()])

# class DonationAdmin(admin.ModelAdmin):
#     list_display = ("user", "quantity", "institution", "address", "phone_number", "city", "zip_code", "pick_up_date", "pick_up_time", "pick_up_comment")
#     list_editable = ("institution", "address", "phone_number", "city", "zip_code", "pick_up_date", "pick_up_time", "pick_up_comment", "user")

class DonationAdmin(admin.ModelAdmin):
    fields = ["user", "categories", "quantity", "institution", "address", "phone_number", "city", "zip_code", "pick_up_date", "pick_up_time", "pick_up_comment"]
    list_display = ("user", "quantity", "get_categories", "institution", "address", "phone_number", "city", "zip_code", "pick_up_date", "pick_up_time", "pick_up_comment")


    def get_categories(self, obj):
        return "\n".join([p.name for p in obj.categories.all()])


admin.site.register(Institution ,InstitutionAdmin)
admin.site.register(Donation, DonationAdmin)

