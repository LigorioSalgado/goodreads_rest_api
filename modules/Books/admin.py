from django.contrib import admin
from .models import Book, Comments
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Comments, CommentsAdmin)
