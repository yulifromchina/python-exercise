from django.contrib import admin
from sign.models import Event,Guest

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['name','status','start_time','id']  # dmin管理后台显示字段
    search_fields = ['name']   # 搜索框按nam搜索
    list_filter = ['status']   # 过滤器按status过滤


class GuestAmdin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']
    search_fields = ['realname','phone']
    list_filter = ['sign']


admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAmdin)

