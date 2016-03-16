from django.contrib import admin
from pis_website.models import *
from student.models import *
from django.db import models
from django import forms


# from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    # list_display = ['description']

    class Media:
        js = ('ckeditor/ckeditor.js',)

class StudentBehavior_Admin(admin.ModelAdmin):
	list_display = ['student', 'date', 'remarks', 'school_year']

admin.site.register(Events, EntryAdmin)
admin.site.register(StudentBehavior, StudentBehavior_Admin)
admin.site.register(EventImages)
