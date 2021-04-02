from django.contrib import admin
from .models import Article,Tutor, Student, Subject, Bill, Sessions, Ratings

admin.site.register(Article)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Bill)
admin.site.register(Sessions)
admin.site.register(Ratings)
