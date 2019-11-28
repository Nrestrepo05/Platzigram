from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'phone_number', 'website', 'profile_picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'profile_picture')

    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'phone_number')
    list_filter = ('created', 'modified')

    fieldsets = (
        ('Profile', {
            'fields' : (('user', 'profile_picture'),),
        }),
        ('Extra Info', {
            'fields' : (
                ('website', 'phone_number'),
                ('bio')
            )
        }),
        ('Dates', {
            'fields' : (
                ('birth_date'),
                ('created'),
                ('modified'),
            )
        })
    )

    readonly_fields = ('created', 'modified', 'user')


class ProfileInline(admin.StackedInline):
    
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    
    inlines =(ProfileInline,)


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
