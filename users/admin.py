from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserOTPs


class CustomUserAdmin(UserAdmin):
  """Define admin model for custom User model with no username field."""
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (('Personal info'), {'fields': ('first_name', 'last_name', 'image_url')}),
    (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                  'groups', 'user_permissions')}),
    (('Important dates'), {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'password1', 'password2'),
    }),
  )
  list_display = ('email', 'id', 'first_name', 'last_name', 'is_staff')
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserOTPs)
