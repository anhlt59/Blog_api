from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'),
            {
                'fields': (
                    'name',
                    ),
            }
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'),
            {'fields':
                (
                    'last_login',
                )
            }
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('name', 'email',)


class PostAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['title', 'slug', 'author', 'status', 'created_at']
    fieldsets = (
        (None, {'fields': ('author',)}),
        (_('Post Info'),
            {
                'fields': (
                    'title',
                    'slug',
                    # 'tags',
                    ),
            }
        ),
        (
            _('Content'),
            {
                'fields': (
                    'content',
                )
            }
        ),
        (_('Status'),
            {'fields':
                (
                    'status',
                )
            }
        ),
    )
    list_filter = ("status",)#, "tags")
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
