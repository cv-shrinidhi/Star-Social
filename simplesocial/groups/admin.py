from django.contrib import admin
from groups import models

# Register your models here.

# the GroupMember model is included as tabular inline
# this allows us to utilize the admin interface with ability to edit models on the same page as the parent model
# that means that including GroupMember model in tabular inline will allow Group model to be seen on admin page
# the admin page will show Group and on clicking it will show GroupMember and we can edit those as well
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
