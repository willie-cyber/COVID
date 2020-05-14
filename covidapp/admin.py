from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from datetime import datetime

class CovidAdmin(admin.ModelAdmin):
	fieldsets = [
		('Información: ', {'fields': ['date', 'name', 'lastname', 'age', 'country', 'gender', 'status']}),
	]
	list_display = ('__str__', 'status')
	list_filter = ('status', 'country')
	search_fields = ['name', 'country']

admin.site.register([Covid], CovidAdmin)
admin.site.site_header = "COVID19 ONLINE"
admin.site.site_title = "Ingeniería en Sistemas"
admin.site.index_title = "Universidad Mariano Galvez"