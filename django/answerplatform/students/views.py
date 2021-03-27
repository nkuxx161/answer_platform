import re
from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .models import Teacher
from .models import TeachingAdmin
from .models import Lesson
from .models import TeacherClass
from .models import StudentClass
from .models import Chatting
from .models import WaitLine
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import TeachingAdminSerializer
from .serializers import LessonSerializer
from .serializers import TeacherClassSerializer
from .serializers import StudentClassSerializer
from .serializers import ChattingSerializer
from .serializers import WaitLineSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(methods = ['post'], detail = False)
    def register(self, request, pk=None):
        studentName = request.data['studentName']
        studentId = request.data['studentId']
        studentEmail = request.data['studentEmail']
        studentPassword = request.data['studentPassword']
        if (Student.objects.filter(studentId = studentId).first()
            or Student.objects.filter(studentEmail = studentEmail).first()):
            return Response({'code': 'false'})
        else:
            Student.objects.create(studentName = studentName, studentId = studentId,
                                   studentEmail = studentEmail, studentPassword = studentPassword)
            return Response({'code': 'true'})

    @action(methods = ['post'], detail = False)
    def login(self,request,pk = None):
        studentEmail = request.data['studentEmail']
        studentPassword = request.data['studentPassword']
        try:
            dbStudentPassword = Student.objects.get(studentEmail = studentEmail).studentPassword
        except:
            return Response({'code': 'false'})
        if (studentPassword == dbStudentPassword):
            data = {}
            student = Student.objects.get(studentEmail = studentEmail)
            data['code'] = 'true'
            data['studentInfor'] = {'studentId': student.studentId, 'studentName': student.studentName}
            return Response(data)
        else:
            return Response({'code': 'false'})
    
    @action(methods = ['post'], detail = False)
    def checkLesson(self, request, pk = None):
        lessonData = []
        studentId = request.data['studentId']
        lessonSet = StudentClass.objects.filter(studentId = studentId)
        for lessonItem in lessonSet:
            lessonItemInfo = Lesson.objects.values().get(lessonId = lessonItem.lessonId)
            lessonData.append(lessonItemInfo)
        return Response(lessonData)

    @action(methods = ['post'], detail = False)
    def changePassword(self, request, pk = None):
        studentId = request.data['studentId']
        studentPassword = request.data['studentPassword']
        if (not Student.objects.filter(studentId = studentId).first()):
            return Response({'code': 'false'})
        else:
            student = Student.objects.filter(studentId = studentId).first()
            student.studentPassword = studentPassword
            student.save()
            return Response({'code': 'true'})

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @action(methods = ['post'], detail = False)
    def register(self, request, pk=None):
        teacherName = request.data['teacherName']
        teacherId = request.data['teacherId']
        teacherEmail = request.data['teacherEmail']
        teacherPassword = request.data['teacherPassword']
        if (teacherName == '' or teacherId == '' or teacherEmail == '' or teacherPassword == ''):
            return Response({'code': 'lack'})
        if (Teacher.objects.filter(teacherEmail = teacherEmail).first()
            or Teacher.objects.filter(teacherId = teacherId).first()):
            return Response({'code': 'exist'})
        else:
            Teacher.objects.create(teacherName = teacherName, teacherId = teacherId,
            teacherEmail = teacherEmail, teacherPassword = teacherPassword)
            return Response({'code': 'success'})

    @action(methods = ['post'], detail = False)
    def login(self,request,pk = None):
        teacherEmail = request.data['teacherEmail']
        teacherPassword = request.data['teacherPassword']
        try:
            dbTeacherPassword = Teacher.objects.get(teacherEmail = teacherEmail).teacherPassword
        except:
            return Response({'code': 'false'})
        if (teacherPassword == dbTeacherPassword):
            data = {}
            teacher = Teacher.objects.get(teacherEmail = teacherEmail)
            data['code'] = 'true'
            data['teacherInfor'] = {'teacherId': teacher.teacherId, 'teacherName': teacher.teacherName}
            return Response(data)
        else:
            return Response({'code': 'false'})

    @action(methods = ['post'], detail = False)
    def checkLesson(self, request, pk = None):
        lessonData = []
        teacherId = request.data['teacherId']
        lessonSet = TeacherClass.objects.filter(teacherId = teacherId)
        for lessonItem in lessonSet:
            lessonItemInfo = Lesson.objects.values().get(lessonId = lessonItem.lessonId)
            lessonData.append(lessonItemInfo)
        return Response(lessonData)

    @action(methods = ['post'], detail = False)
    def changePassword(self, request, pk = None):
        teacherId = request.data['teacherId']
        teacherPassword = request.data['teacherPassword']
        if (not Teacher.objects.filter(teacherId = teacherId).first()):
            return Response({'code': 'false'})
        else:
            teacher = Teacher.objects.filter(teacherId = teacherId).first()
            teacher.teacherPassword = teacherPassword
            teacher.save()
            return Response({'code': 'true'})

class TeachingAdminView(viewsets.ModelViewSet):
    queryset = TeachingAdmin.objects.all()
    serializer_class = TeachingAdminSerializer

    @action(methods = ['post'], detail = False)
    def login(self,request,pk = None):
        adminName = request.data['adminName']
        adminPassword = request.data['adminPassword']
        try:
            dbAdminPassword = TeachingAdmin.objects.get(adminName = adminName).adminPassword
        except:
            return Response({'code': 'false'})
        if (adminPassword == dbAdminPassword):
            return Response({'code': 'true'})
        else:
            return Response({'code': 'false'})

    @action(methods = ['post'], detail = False)
    def deleteLesson(self, request, pk = None):
        lessonId = request.data['lessonId']
        if (not Lesson.objects.filter(lessonId = lessonId).first()):
            return Response({'code': 'false'})
        else:
            Lesson.objects.filter(lessonId = lessonId).delete()
            TeacherClass.objects.filter(lessonId = lessonId).delete()
            StudentClass.objects.filter(lessonId = lessonId).delete()
            Chatting.objects.filter(lessonId = lessonId).delete()
            WaitLine.objects.filter(lessonId = lessonId).delete()
            return Response({'code': 'true'})

class LessonView(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    @action(methods = ['post'], detail = False)
    def checkNotice(self, request, pk = None):
        try:
            lessonInformation = Lesson.objects.get(lessonId = request.data['lessonId'])
        except:
            data = {'code': 'false', 'lessonNotice': '未找到对应的答疑公告'}
            return Response(data)
        data = {'code': 'true', 'lessonNotice': lessonInformation.lessonNotice}
        return Response(data)

    @action(methods = ['post'], detail = False)
    def changeNotice(self, request, pk = None):
        lessonId = request.data['lessonId']
        lessonNotice = request.data['lessonNotice']
        try:
            dbLessonInformation = Lesson.objects.get(lessonId = lessonId)
        except:
            data = {'code': 'false'}
            return Response(data)
        dbLessonInformation.lessonNotice = lessonNotice
        dbLessonInformation.save()
        data = {'code': 'true', 'lessonNotice': dbLessonInformation.lessonNotice}
        return Response(data)

    @action(methods = ['post'], detail = False)
    def updateCode(self, request, pk = None):
        lessonId = request.data['lessonId']
        codeContent = request.data['codeContent']
        if (not Lesson.objects.filter(lessonId = lessonId).first()):
            return Response({'code': 'false'})
        else:
            lesson = Lesson.objects.filter(lessonId = lessonId).first()
            lesson.codeContent = codeContent
            lesson.save()
            data = {}
            data['code'] = 'true'
            data['codeContent'] = lesson.codeContent
            return Response(data)

    @action(methods = ['post'], detail = False)
    def getCode(self, request, pk = None):
        lessonId = request.data['lessonId']
        if (not Lesson.objects.filter(lessonId = lessonId).first()):
            return Response({'code': 'false'})
        else:
            lesson = Lesson.objects.filter(lessonId = lessonId).first()
            data = {}
            data['code'] = 'true'
            data['codeContent'] = lesson.codeContent
            return Response(data)

    @action(methods = ['post'], detail = False)
    def addLesson(self, request, pk = None):
        lessonId = request.data['lessonId']
        lessonName = request.data['lessonName']
        lessonNotice = request.data['lessonNotice']
        if (lessonId == '' or lessonName == ''):
            return Response({'code': 'lack'})
        if (Lesson.objects.filter(lessonId = lessonId).first()):
            return Response({'code': 'exist'})
        Lesson.objects.create(lessonId = lessonId, lessonName = lessonName, lessonNotice = lessonNotice)
        return Response({'code': 'success'})


class TeacherClassView(viewsets.ModelViewSet):
    queryset = TeacherClass.objects.all()
    serializer_class = TeacherClassSerializer

    @action(methods = ['post'], detail = False)
    def addTeacher(self, request, pk = None):
        lessonId = request.data['lessonId']
        teacherEmail = request.data['teacherEmail']
        teacherId = request.data['teacherId']
        teacherName = request.data['teacherName']
        if (lessonId == '' or teacherEmail == '' or teacherId == '' or teacherName == ''):
            return Response({'code': 'false'})
        elif (not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", teacherEmail)):
            return Response({'code': 'error'})
        elif (TeacherClass.objects.filter(teacherEmail = teacherEmail, lessonId = lessonId).first()
              or TeacherClass.objects.filter(teacherId = teacherId, lessonId = lessonId).first()):
            return Response({'code': 'false'})
        TeacherClass.objects.create(lessonId = lessonId, teacherEmail = teacherEmail,
                                    teacherId = teacherId, teacherName = teacherName)
        return Response({'code': 'true'})

    @action(methods = ['post'], detail = False)
    def getTeacher(self, request, pk = None):
        lessonId = request.data['lessonId']
        if (not TeacherClass.objects.filter(lessonId = lessonId)):
            return Response({'code': 'false'})
        else:
            data = {}
            data['code'] = 'true'
            infor = TeacherClass.objects.values().filter(lessonId = lessonId)
            data['teacherList'] = list(infor)
            return Response(data)

    @action(methods = ['post'], detail = False)
    def deleteTeacher(self, request, pk = None):
        teacherId = request.data['teacherId']
        lessonId = request.data['lessonId']
        if (not TeacherClass.objects.filter(teacherId = teacherId, lessonId = lessonId)):
            return Response({'code': 'false'})
        else:
            TeacherClass.objects.filter(teacherId = teacherId, lessonId = lessonId).delete()
            return Response({'code': 'true'})    

class StudentClassView(viewsets.ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer

    @action(methods = ['post'], detail = False)
    def addStudent(self, request, pk = None):
        lessonId = request.data['lessonId']
        studentEmail = request.data['studentEmail']
        studentId = request.data['studentId']
        studentName = request.data['studentName']
        if (lessonId == '' or studentEmail == '' or studentId == '' or studentName == ''):
            return Response({'code': 'false'})
        elif (not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", studentEmail)):
            return Response({'code': 'error'})
        elif (StudentClass.objects.filter(studentEmail = studentEmail, lessonId = lessonId).first()
              or StudentClass.objects.filter(studentId = studentId, lessonId = lessonId).first()):
            return Response({'code': 'false'})
        StudentClass.objects.create(lessonId = lessonId, studentEmail = studentEmail,
                                    studentId = studentId, studentName = studentName)
        return Response({'code': 'true'})

    @action(methods = ['post'], detail = False)
    def getStudent(self, request, pk = None):
        lessonId = request.data['lessonId']
        if (not StudentClass.objects.filter(lessonId = lessonId)):
            return Response({'code': 'false'})
        else:
            data = {}
            data['code'] = 'true'
            infor = StudentClass.objects.values().filter(lessonId = lessonId)
            data['studentList'] = list(infor)
            return Response(data)

    @action(methods = ['post'], detail = False)
    def deleteStudent(self, request, pk = None):
        studentId = request.data['studentId']
        lessonId = request.data['lessonId']
        if (not StudentClass.objects.filter(studentId = studentId, lessonId = lessonId)):
            return Response({'code': 'false'})
        else:
            StudentClass.objects.filter(studentId = studentId, lessonId = lessonId).delete()
            WaitLine.objects.filter(studentId = studentId, lessonId = lessonId).delete()
            return Response({'code': 'true'})   

class ChattingView(viewsets.ModelViewSet):
    queryset = Chatting.objects.all()
    serializer_class = ChattingSerializer

    @action(methods = ['post'], detail = False)
    def makeNote(self, request, pk = None):
        chatName = request.data['chatName']
        chatContent = request.data['chatContent']
        lessonId = request.data['lessonId']
        personId = request.data['personId']
        Chatting.objects.create(chatName = chatName, chatContent = chatContent, lessonId = lessonId, personId = personId)
        return Response()

    @action(methods = ['post'], detail = False)
    def checkNote(self, request, pk = None):
        data = {}
        lessonIdData = request.data['lessonId']
        if (not Chatting.objects.filter(lessonId = lessonIdData).first()):
            data['code'] = 'false'
            return Response(data)
        else:
            chatRecords = Chatting.objects.values().filter(lessonId = lessonIdData)
            data['code'] = 'true'
            data['recordList'] = list(chatRecords)
            return Response(data)

class WaitLineView(viewsets.ModelViewSet):
    queryset = WaitLine.objects.all()
    serializer_class = WaitLineSerializer

    @action(methods = ['post'], detail = False)
    def getLine(self, request, pk = None):
        lessonId = request.data['lessonId']
        if (not WaitLine.objects.filter(lessonId = lessonId).first()):
            return Response({'code': 'false'})
        else:
            data = {'code': 'true'}
            lineData = WaitLine.objects.values().filter(lessonId = lessonId)
            data['lineList'] = list(lineData)
            return Response(data)

    @action(methods = ['post'], detail = False)
    def joinLine(self, request, pk = None):
        lessonId = request.data['lessonId']
        studentId = request.data['studentId']
        studentName = request.data['studentName']
        if (lessonId == '' or studentId == '' or studentName == ''):
            return Response({'code': 'false'})
        elif (not StudentClass.objects.filter(studentId = studentId, lessonId = lessonId).first()):
            return Response({'code': 'false'})
        elif (WaitLine.objects.filter(studentId = studentId, lessonId = lessonId).first()):
            return Response({'code': 'false'})
        WaitLine.objects.create(lessonId = lessonId, studentId = studentId, studentName = studentName)
        data = {'code': 'true'}
        lineData = WaitLine.objects.values().filter(lessonId = lessonId)
        data['lineList'] = list(lineData)
        return Response(data)

    @action(methods = ['post'], detail = False)    
    def quitLine(self, request, pk = None):
        deleteId = request.data['id']
        lessonId = request.data['lessonId']
        if (not WaitLine.objects.filter(id = deleteId).first()):
            return Response({'code': 'false'})
        else:
            WaitLine.objects.get(id = deleteId).delete()
            data = {'code': 'true'}
            lineData = WaitLine.objects.values().filter(lessonId = lessonId)
            data['lineList'] = list(lineData)
            return Response(data)
