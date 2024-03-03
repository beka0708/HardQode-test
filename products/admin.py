from django.contrib import admin
from .models import Product, User, AccessStudents, Group, Lesson

admin.site.register(User)
admin.site.register(Product)
admin.site.register(AccessStudents)
admin.site.register(Group)
admin.site.register(Lesson)
