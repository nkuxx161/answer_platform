from django.test import TestCase
from ..models import Teacher, Lesson, TeacherClass
import json


class TeacherTest(TestCase):
    def setUp(self) -> None:
        Teacher.objects.create(teacherName = '张三', teacherId = '1810000', 
                               teacherEmail = '1234@qq.com', teacherPassword = '123456')


    def test_model(self):
        teacher = Teacher.objects.filter(teacherId = '1810000').first()
        self.assertEqual(teacher.teacherName, '张三')
        self.assertEqual(teacher.teacherEmail, '1234@qq.com')
        self.assertEqual(teacher.teacherPassword, '123456')


class MethodTest(TestCase):
    def setUp(self) -> None:
        Teacher.objects.create(teacherName = '李四', teacherId = '1810001',
                               teacherEmail = '123456@qq.com', teacherPassword = '123456')
        Lesson.objects.create(lessonId = '001', lessonName = 'c语言', lessonNotice = '无')
        Lesson.objects.create(lessonId = '002', lessonName = 'java', lessonNotice = '无')
        Lesson.objects.create(lessonId = '003', lessonName = '数据结构', lessonNotice = '无')
        TeacherClass.objects.create(teacherName = '李四', teacherId = '1810001',
                                    teacherEmail = '123456@qq.com', lessonId = '001')
        TeacherClass.objects.create(teacherName = '李四', teacherId = '1810001',
                                    teacherEmail = '123456@qq.com', lessonId = '002')
        TeacherClass.objects.create(teacherName = '李四', teacherId = '1810001',
                                    teacherEmail = '123456@qq.com', lessonId = '003')


    def test_login(self):
        #账号密码正确
        parameters = {
            'teacherEmail': '123456@qq.com',
            'teacherPassword': '123456'
        }
        url = '/teacher/login/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')

        #密码错误
        parameters = {
            'teacherEmail': '123456@qq.com',
            'teacherPassword': '12345'
        }
        url = '/teacher/login/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #账号不存在
        parameters = {
            'teacherEmail': '123457@qq.com',
            'teacherPassword': '123456'
        }
        url = '/teacher/login/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

    def test_register(self):
        #输入信息不全
        parameters = {
            'teacherName': '李四',
            'teacherId': '',
            'teacherEmail': '',
            'teacherPassword': '123456'
        }
        url = '/teacher/register/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'lack')

        #账号已存在
        parameters = {
            'teacherName': '李四',
            'teacherId': '1810001',
            'teacherEmail': '123456@qq.com',
            'teacherPassword': '123456'
        }
        url = '/teacher/register/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'exist')

        #账号注册成功
        parameters = {
            'teacherName': '王五',
            'teacherId': '1810002',
            'teacherEmail': '123457@qq.com',
            'teacherPassword': '123457'
        }
        url = '/teacher/register/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'success')


    def test_checkLesson(self):
        parameters = {
            'teacherId': '1810001'
        }
        url = '/teacher/checkLesson/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict[0]['lessonId'], '001')
        self.assertEqual(dataDict[1]['lessonId'], '002')
        self.assertEqual(dataDict[2]['lessonId'], '003')
