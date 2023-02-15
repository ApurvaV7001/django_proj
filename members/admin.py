from django.contrib import admin
from .models import Member, Student

# Register your models here.
# admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "mobile_no", "joined_date",)

class StudentAdmin(admin.ModelAdmin):  
  list_display = ("firstname", "lastname", "Rollno", "created_by",)


admin.site.register(Member, MemberAdmin)

admin.site.register(Student, StudentAdmin)