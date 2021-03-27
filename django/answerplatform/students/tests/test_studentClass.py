from django.test import TestCase
from ..models import StudentClass
import json


class StudentClassTest(TestCase):
    def setUp(self) -> None:
        StudentClass.objects.create(studentName = 'testname', studentId = '12345',
                                    studentEmail = '123@qq.com', lessonId = '001')
        StudentClass.objects.create(studentName = 'testname2', studentId = '12346',
                                    studentEmail = '124@qq.com', lessonId = '002')

    
    def test_model(self):
        test1 = StudentClass.objects.filter(studentId = '12345').filter().first()
        self.assertEqual(test1.studentEmail, '123@qq.com')
        self.assertEqual(test1.studentName, 'testname')
        test2 = StudentClass.objects.filter(studentId = '12346').filter().first()
        self.assertEqual(test2.lessonId, '002')


class MethodTest(TestCase):
    def setUp(self) -> None:
        StudentClass.objects.create(studentName = 'testname', studentId = '12345',
                                    studentEmail = '123@qq.com', lessonId = '001')


    def test_addTeacher(self):
        #输入信息不完全导致添加失败
        parameters = {
            'lessonId': '002',
            'studentId': '',
            'studentName': '',
            'studentEmail': ''
        }
        url = '/studentClass/addStudent/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')


        #该学生已经加入该课程导致添加失败
        parameters = {
            'lessonId': '001',
            'studentId': '12345',
            'studentName': 'testname',
            'studentEmail': '123@qq.com'
        }
        url = '/studentClass/addStudent/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #添加学生成功
        parameters = {
            'lessonId': '002',
            'studentId': '12346',
            'studentName': 'testname2',
            'studentEmail': '124@qq.com'
        }
        url = '/studentClass/addStudent/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')
