from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'phone_number')
    search_fields = ('user__username', 'user__email', 'position')

admin.site.register(Profile, ProfileAdmin)