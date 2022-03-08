from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import profession
from .models import state
from .models import dist
from .models import User
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('name', 'email', 'phone', 'image', 'password', 'profession', 'state_name', 'dist_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


# Register your models here.
class professionAdmin(admin.ModelAdmin):
    list_display = ['name']

class stateAdmin(admin.ModelAdmin):
    list_display = ['name']

class distAdmin(admin.ModelAdmin):
    list_display = ['name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'reason', 'date_and_time', 'date_time', 'accepted', 'accepted_date']


admin.site.register(profession, professionAdmin)
admin.site.register(state, stateAdmin)
admin.site.register(dist, distAdmin)
#admin.site.register(cunsultant, cunsultantAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
