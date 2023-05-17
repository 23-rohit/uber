from django.contrib import admin

# Register your models here.
from users.models import (Students,)
admin.site.register(Students)

from users.models import(Orders,)
admin.site.register(Orders)
