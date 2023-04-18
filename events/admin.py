from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from .models import Event
from jdatetime import datetime as jalali_datetime


@admin.register(Event)
class EventAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
	list_display = ['name', 'get_created_jalali']

	def get_created_jalali(self, obj):
		return jalali_datetime.fromgregorian(datetime=obj.date).strftime('%y/%m/%d')
	
	get_created_jalali.short_description = 'تاریخ ایجاد'
	get_created_jalali.admin_order_field = 'created'