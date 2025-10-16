from django.contrib import admin

from usefulthings.models import Wont


@admin.register(Wont)
class WontAdmin(admin.ModelAdmin):
    """Класс описания административной панели"""

    list_display = ("id", "action", "is_pleasant", "owner", "is_published")
    list_filter = ("action", "is_pleasant", "owner")
    search_fields = ("action", "is_pleasant", "owner")
