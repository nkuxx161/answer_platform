from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import TeachingAdmin
from .models import Lesson
from .models import TeacherClass
from .models import Chatting
from .models import StudentClass
from .models import WaitLine
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(TeachingAdmin)
admin.site.register(Lesson)
admin.site.register(TeacherClass)
admin.site.register(StudentClass)
admin.site.register(Chatting)
admin.site.register(WaitLine)
