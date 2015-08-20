from django.contrib import admin
from member.models import *
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'create_date')
    search_fields = ('title','content')


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'url')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketCategory)
admin.site.register(Answer)
admin.site.register(UserDetails, UserDetailAdmin)