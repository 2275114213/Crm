from django.contrib import admin

# Register your models here.


from app01.models import *
class UserInfoconfig(admin.ModelAdmin):
        list_display = ['tel','gender']
        search_fields = ['tel','gender']
        list_filter = ['gender']
admin.site.register(UserInfo,UserInfoconfig)
admin.site.register(ClassList)
admin.site.register(Customer)
admin.site.register(Campuses)
admin.site.register(ConsultRecord)