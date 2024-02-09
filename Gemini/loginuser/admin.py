from django.contrib import admin
from loginuser.models import Emp,Position

class EmpAdmin(admin.ModelAdmin):
    list_display=('firstname','mobile','empcode','pos')

admin.site.register(Emp,EmpAdmin)


class PosAdmin(admin.ModelAdmin):
    list_display=('title',)
admin.site.register(Position,PosAdmin)
# Register your models here.
