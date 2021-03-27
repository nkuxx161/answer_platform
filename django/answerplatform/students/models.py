from django.db import models

# Create your models here.
class Student(models.Model):
    studentName = models.TextField(blank = False)
    studentId = models.TextField(blank = False, unique = True)
    studentEmail = models.TextField(blank = False, unique = True)
    studentPassword = models.TextField(blank = False)

class Teacher(models.Model):
    teacherName = models.TextField(blank = False)
    teacherId = models.TextField(blank = False, unique = True)
    teacherEmail = models.TextField(blank = False, unique = True)
    teacherPassword = models.TextField(blank = False)

class TeachingAdmin(models.Model):
    adminName = models.TextField(blank = False, unique = True)
    adminPassword = models.TextField(blank = False)

class Lesson(models.Model):
    lessonId = models.TextField(blank = False, unique = True)
    lessonName = models.TextField(blank = False)
    lessonNotice = models.TextField(blank = True)
    codeContent = models.TextField(blank = True)

class TeacherClass(models.Model):
    teacherEmail = models.TextField(blank = False)
    teacherName = models.TextField(blank = False)
    teacherId = models.TextField(blank = False)
    lessonId = models.TextField(blank = False)

class StudentClass(models.Model):
    studentEmail = models.TextField(blank = False)
    studentName = models.TextField(blank = False)
    studentId = models.TextField(blank = False)
    lessonId = models.TextField(blank = False)

class Chatting(models.Model):
    chatName = models.TextField(blank = False)
    chatTime = models.DateTimeField(blank = False, auto_now_add = True)
    chatContent = models.TextField(blank = True)
    lessonId = models.TextField(blank = False)
    personId = models.TextField(blank = True)

class WaitLine(models.Model):
    lessonId = models.TextField(blank = False)
    studentId = models.TextField(blank = False)
    studentName = models.TextField(blank = False)
