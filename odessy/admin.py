from django.contrib import admin
from odessy.models import ody 
from odessy.models import hell
from odessy.models import od

class ali(admin.ModelAdmin):
    list_display = ['eno1','eno2','eno3','eno4','eno5','eno6','eno7','eno8','eno9' ]
admin.site.register(ody,ali)


class al(admin.ModelAdmin):
    list_display = ['en']
admin.site.register(hell,al)

class lk(admin.ModelAdmin):
    list_display = ['en1','en2','en3','en4','en5','en6','en7','en8','en9','en10' ]
admin.site.register(od,lk)




# Register your models here.
