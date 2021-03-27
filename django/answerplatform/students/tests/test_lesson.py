from django.test import TestCase
from ..models import Lesson
import json


class LessonTest(TestCase):
    def setUp(self) -> None:
        Lesson.objects.create(lessonId = '001', lessonName = '数据库基础', lessonNotice = '答疑时间改为7月12日下午')


    def test_model(self):
        lesson = Lesson.objects.filter(lessonId = '001').first()
        self.assertEqual(lesson.lessonName, '数据库基础')
        self.assertEqual(lesson.lessonNotice, '答疑时间改为7月12日下午')


class MethodTest(TestCase):
    def setUp(self) -> None:
        Lesson.objects.create(lessonId = '001', lessonName = '数据库基础', lessonNotice = '答疑时间改为7月12日下午')
    

    def test_checkNotice(self):
        #查询公告失败
        parameters = {
            'lessonId': '002'
        }
        url = '/lesson/checkNotice/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #查询公告成功
        parameters = {
            'lessonId': '001'
        }
        url = '/lesson/checkNotice/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')


    def test_changeNotice(self):
        #修改公告失败
        parameters = {
            'lessonId': '002',
            'lessonNotice': '答疑公告已改变'
        }
        url = '/lesson/changeNotice/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #修改公告成功
        parameters = {
            'lessonId': '001',
            'lessonNotice': '答疑公告已改变'
        }
        url = '/lesson/changeNotice/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')
        self.assertEqual(dataDict['lessonNotice'], '答疑公告已改变')


    def test_addLesson(self):
        #课程信息缺失
        parameters = {
            'lessonId': '002',
            'lessonName': '',
            'lessonNotice': ''
        }
        url = '/lesson/addLesson/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'lack')

        #课程已存在
        parameters = {
            'lessonId': '001',
            'lessonName': '数据库基础',
            'lessonNotice': '答疑时间改为7月12日下午'
        }
        url = '/lesson/addLesson/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'exist')

        #课程添加成功
        parameters = {
            'lessonId': '002',
            'lessonName': 'C语言',
            'lessonNotice': '答疑时间改为7月11日下午'
        }
        url = '/lesson/addLesson/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'success')
