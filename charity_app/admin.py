from django.contrib import admin
from django.contrib.auth.models import User

from charity_app.models import Institution, Category, Donation

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "type")
    list_editable = ("description", "type")


class DonationAdmin(admin.ModelAdmin):
    list_display = ("quantity", "institution", "address", "phone_number", "city", "zip_code", "pick_up_date", "pick_up_time", "pick_up_comment", "user")
    list_editable = ("institution", "address", "phone_number", "city", "zip_code", "pick_up_date", "pick_up_time", "pick_up_comment", "user")



admin.site.register(Institution ,InstitutionAdmin)
admin.site.register(Donation, DonationAdmin)

