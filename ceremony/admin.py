from django.contrib import admin
from .models import Ceremony, Participant
from jalali_date.admin import ModelAdminJalaliMixin
from jdatetime import datetime as jalali_datetime


class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 0


@admin.register(Ceremony)
class CeremonyAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    inlines = [ParticipantInline]
    list_display = ['title', 'get_date_jalali', 'location']
    search_fields = ['title', 'location']

    def get_date_jalali(self, obj):
        return jalali_datetime.fromgregorian(datetime=obj.date).strftime('%y/%m/%d')
	
    get_date_jalali.short_description = 'تاریخ ایجاد'
    get_date_jalali.admin_order_field = 'date'


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'ceremony', 'user']
    list_filter = ['ceremony']
    search_fields = ['name', 'user']
