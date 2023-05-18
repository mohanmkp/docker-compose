from django.contrib import admin
from .models import User
# Register your models here.


admin.site.site_header = "Visiontrek Administration"
admin.site.site_title = "Visiontrek "
admin.site.index_title = "Visiontrek"

class user(admin.ModelAdmin):
    list_display = ["email", "mobile_number", "is_superuser", "is_staff", "is_active", "gender"]
    list_filter = ["is_superuser", "is_active"]
    search_fields = ["email"]


admin.site.register(User, user)



