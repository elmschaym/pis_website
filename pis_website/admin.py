from django.contrib import admin
from pis_website.models import *
from django.db import models
from django import forms


# from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    # list_display = ['description']

    class Media:
        js = ('ckeditor/ckeditor.js',)

class AttendanceAndBehaviour_Admin(admin.ModelAdmin):
	list_display = ['student', 'date', 'time_start', 'time_end', 'remarks']

admin.site.register(Events, EntryAdmin)
admin.site.register(AttendanceAndBehaviour, AttendanceAndBehaviour_Admin)
admin.site.register(EventImages)
