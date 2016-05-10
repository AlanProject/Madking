from django.contrib import admin
from asset.user_models import UserProfile
from asset.user_admin import UserAdmin,Group
# Register your models here.
admin.site.register(UserProfile,UserAdmin)


admin.site.unregister(Group)