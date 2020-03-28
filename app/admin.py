from django.contrib import admin
from .models import Scholarship , Case , Country ,Categories, License
# Register your models here.
admin.site.register(Categories)
admin.site.register(Country)
admin.site.register(Scholarship)
admin.site.register(Case)
admin.site.register(License)