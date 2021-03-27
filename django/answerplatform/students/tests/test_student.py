from django.test import TestCase, override_settings
from ..models import Student, Lesson, StudentClass
import json


class StudentTest(TestCase):
    def setUp(self) -> None:
        Student.objects.create(studentName = '张三', studentId = '1813036', 
                               studentEmail = '1617358857@qq.com', studentPassword = '998abc')
    

    def test_model(self):
        student = Student.objects.filter(studentId = '1813036')[0]
        self.assertEqual(student.studentName, '张三')
        self.assertEqual(student.studentId, '1813036')
        self.assertEqual(student.studentPassword, '998abc')


class MethodTest(TestCase):
    def setUp(self) -> None:
        Student.objects.create(studentName = '李四', studentId = '1810001', 
                               studentEmail = '123456@qq.com', studentPassword = '123456')
        Lesson.objects.create(lessonId = '001', lessonName = 'c语言', lessonNotice = '无')
        Lesson.objects.create(lessonId = '002', lessonName = 'java', lessonNotice = '无')
        Lesson.objects.create(lessonId = '003', lessonName = '数据结构', lessonNotice = '无')
        StudentClass.objects.create(studentName = '李四', studentId = '1810001', 
                                    studentEmail = '123456@qq.com', lessonId = '001'),
        StudentClass.objects.create(studentName = '李四', studentId = '1810001', 
                                    studentEmail = '123456@qq.com', lessonId = '002'),
        StudentClass.objects.create(studentName = '李四', studentId = '1810001', 
                                    studentEmail = '123456@qq.com', lessonId = '003')

    def test_login(self):
        parameters = {
            'studentEmail': '123456@qq.com',
            'studentPassword': '123456'
        }
        url = '/student/login/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')

        parameters = {
            'studentEmail': '123456@qq.com',
            'studentPassword': '12345'
        }
        url = '/student/login/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        parameters = {
            'studentEmail': '123457@qq.com',
            'studentPassword': '123456'
        }
        url = '/student/login/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

    def test_register(self):
        parameters = {
            'studentName': '李四',
            'studentEmail': '123456@qq.com',
            'studentId': '1810001',
            'studentPassword': '123456'
        }
        url = '/student/register/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        parameters = {
            'studentName': '王五',
            'studentEmail': '123457@qq.com',
            'studentId': '1810002',
            'studentPassword': '123457'
        }
        url = '/student/register/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')        

    def test_checkLesson(self):
        parameters = {
            'studentId': '1810001'
        }
        url = '/student/checkLesson/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict[0]['lessonId'], '001')
        self.assertEqual(dataDict[1]['lessonId'], '002')
        self.assertEqual(dataDict[2]['lessonId'], '003')
