from django.test import TestCase
from ..models import TeachingAdmin
import json


class TeachingAdminTest(TestCase):
    def setUp(self) -> None:
        TeachingAdmin.objects.create(adminName = 'admin', adminPassword = '123456')
    

    def test_model(self):
        teachingAdmin = TeachingAdmin.objects.filter(adminName = 'admin').first()
        self.assertEqual(teachingAdmin.adminPassword, '123456')


class MethodTest(TestCase):
    def setUp(self) -> None:
        TeachingAdmin.objects.create(adminName = 'admin', adminPassword = '123456')

    
    def test_login(self):
        #管理员账号不存在，登陆失败
        parameters = {
            'adminName': 'test',
            'adminPassword': '12345'
        }
        url = '/teachingAdmin/login/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #管理员密码错误，登陆失败
        parameters = {
            'adminName': 'admin',
            'adminPassword': '12345'
        }
        url = '/teachingAdmin/login/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'false')

        #管理员登陆成功
        parameters = {
            'adminName': 'admin',
            'adminPassword': '123456'
        }
        url = '/teachingAdmin/login/'
        response = self.client.post(url, parameters, content_type = 'application/json')
        dataDict = json.loads(response.content)
        self.assertEqual(dataDict['code'], 'true')
