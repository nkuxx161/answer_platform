from django.test import TestCase
from ..models import TeacherClass
import json


class TeacherClassTest(TestCase):
    def setUp(self) -> None:
        TeacherClass.objects.create(teacherName = 'testname', teacherId = '12345',
                                    teacherEmail = '123@qq.com', lessonId = '001')
        TeacherClass.objects.create(teacherName = 'testname2', teacherId = '12346',
                                    teacherEmail = '124@qq.com', lessonId = '002')

    
    def test_model(self):
        test1 = TeacherClass.objects.filter(teacherId = '12345').filter().first()
        self.assertEqual(test1.teacherEmail, '123@qq.com')
        self.assertEqual(test1.teacherName, 'testname')
        test2 = TeacherClass.objects.filter(teacherId = '12346').filter().first()
        self.assertEqual(test2.lessonId, '002')


class MethodTest(TestCase):
    def setUp(self) -> None:
        TeacherClass.objects.create(teacherName = 'testname', teacherId = '12345',
                                    teacherEmail = '123@qq.com', lessonId = '001')


    def test_addTeacher(self):
        #输入信息不完全导致添加失败
        parameters = {
            'lessonId': '002',
            'teacherId': '',
            'teacherName': '',
            'teacherEmail': ''
        }
        url = '/teacherClass/addTeacher/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')


        #该老师已经加入该课程导致添加失败
        parameters = {
            'lessonId': '001',
            'teacherId': '12345',
            'teacherName': 'testname',
            'teacherEmail': '123@qq.com'
        }
        url = '/teacherClass/addTeacher/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #添加老师成功
        parameters = {
            'lessonId': '002',
            'teacherId': '12346',
            'teacherName': 'testname2',
            'teacherEmail': '124@qq.com'
        }
        url = '/teacherClass/addTeacher/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')
