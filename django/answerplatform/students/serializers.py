from rest_framework import serializers
from .models import Student
from .models import Teacher
from .models import TeachingAdmin
from .models import Lesson
from .models import TeacherClass
from .models import StudentClass
from .models import Chatting
from .models import WaitLine

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'studentName', 'studentId', 'studentEmail', 'studentPassword')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'teacherName', 'teacherId', 'teacherEmail', 'teacherPassword')

class TeachingAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingAdmin
        fields = ('id', 'adminName', 'adminPassword')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'lessonName', 'lessonId', 'lessonNotice', 'codeContent')

class TeacherClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClass
        fields = ('id', 'teacherEmail', 'teacherName', 'teacherId', 'lessonId')

class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ('id', 'studentEmail', 'studentName', 'studentId', 'lessonId')

class ChattingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatting
        fields = ('id', 'chatName', 'chatTime', 'chatContent', 'lessonId', 'personId')

class WaitLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitLine
        fields = ('id', 'lessonId', 'studentId', 'studentName')
