from django.test import TestCase
from ..models import WaitLine, StudentClass
import json


class WaitLineTest(TestCase):
    def setUp(self) -> None:
        WaitLine.objects.create(lessonId = '001', studentId = '1810001', studentName = 'testname')
        WaitLine.objects.create(lessonId = '001', studentId = '1810002', studentName = 'testname2')


    def test_model(self):
        students = WaitLine.objects.filter(lessonId = '001')
        self.assertEqual(students[0].studentId, '1810001')
        self.assertEqual(students[0].studentName, 'testname')
        self.assertEqual(students[1].studentId, '1810002')
        self.assertEqual(students[1].studentName, 'testname2')


class MethodTest(TestCase):
    def setUp(self) -> None:
        WaitLine.objects.create(lessonId = '001', studentId = '1810001', studentName = 'testname')
        WaitLine.objects.create(lessonId = '001', studentId = '1810002', studentName = 'testname2')
        StudentClass.objects.create(lessonId = '001', studentId = '1810001', studentName = 'testname', studentEmail = '123@qq.com')
        StudentClass.objects.create(lessonId = '001', studentId = '1810002', studentName = 'testname2', studentEmail = '124@qq.com')
        StudentClass.objects.create(lessonId = '001', studentId = '1810003', studentName = 'testname3', studentEmail = '125@qq.com')

    def test_getLine(self):
        #房间号不存在，获取排队列表失败
        parameters = {
            'lessonId': '002'
        }
        url = '/waitLine/getLine/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #获取排队列表成功
        parameters = {
            'lessonId': '001'
        }
        url = '/waitLine/getLine/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')    


    def test_joinLine(self):
        #输入的参数信息不完整
        parameters = {
            'lessonId': '001',
            'studentId': '',
            'studentName': ''
        }
        url = '/waitLine/joinLine/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #该学生未在答疑教室中，将排队失败
        parameters = {
            'lessonId': '001',
            'studentId': '1810004',
            'studentName': 'testname4'
        }
        url = '/waitLine/joinLine/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #该学生已经在排队列表中了，将排队失败
        parameters = {
            'lessonId': '001',
            'studentId': '1810001',
            'studentName': 'testname'
        }
        url = '/waitLine/joinLine/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #学生排队成功
        parameters = {
            'lessonId': '001',
            'studentId': '1810003',
            'studentName': 'testname3'
        }
        url = '/waitLine/joinLine/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')


    def test_quitLine(self):
        #未在排队列表中退出失败
        parameters = {
            'lessonId': '001',
            'id': '100'
        }
        url = '/waitLine/quitLine/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #从排队列表中成功退出
        parameters = {
            'lessonId': '001',
            'id': WaitLine.objects.filter(studentId = '1810001').first().id
        }
        url = '/waitLine/quitLine/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')
