from django.test import TestCase
from ..models import Chatting
import json


class ChattingTest(TestCase):
    def setUp(self) -> None:
        Chatting.objects.create(chatName = 'testname', chatContent = 'testcontent', lessonId = '001')
        Chatting.objects.create(chatName = 'testname2', chatContent = 'testcontent2', lessonId = '001')
        Chatting.objects.create(chatName = 'testname3', chatContent = 'testcontent3', lessonId = '002')


    def test_model(self):
        chatting1 = Chatting.objects.filter(lessonId = '001')
        self.assertEqual(chatting1[0].chatName, 'testname')
        self.assertEqual(chatting1[0].chatContent, 'testcontent')
        self.assertEqual(chatting1[1].chatName, 'testname2')
        self.assertEqual(chatting1[1].chatContent, 'testcontent2')
        chatting2 = Chatting.objects.filter(lessonId = '002')
        self.assertEqual(chatting2[0].chatName, 'testname3')
        self.assertEqual(chatting2[0].chatContent, 'testcontent3')


class MethodTest(TestCase):
    def setUp(self) -> None:
        Chatting.objects.create(chatName = 'testname', chatContent = 'testcontent', lessonId = '001')
        Chatting.objects.create(chatName = 'testname2', chatContent = 'testcontent2', lessonId = '001')
        Chatting.objects.create(chatName = 'testname3', chatContent = 'testcontent3', lessonId = '002')


    def test_makeNote(self):
        parameters = {
            'chatName': 'testname4',
            'chatContent': 'testContent',
            'lessonId': '001'
        }
        url = '/chatting/makeNote/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    def test_checkNote(self):
        #获取聊天记录的房间号不存在，获取失败
        parameters = {
            'lessonId': '003'
        }
        url = '/chatting/checkNote/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #成功获取聊天记录
        parameters = {
            'lessonId': '001'
        }
        url = '/chatting/checkNote/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')
        parameters = {
            'lessonId': '002'
        }
        url = '/chatting/checkNote/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')
