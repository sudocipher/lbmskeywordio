from django.contrib import admin
from .models import Book
# Register your models here to show it  in admin panel
class  BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')

admin.site.register(Book, BookAdmin)