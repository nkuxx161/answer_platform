from django.test import TestCase

class ModelTestCase(TestCase):
    def test_Model(self):
        self.assertEqual(1 + 1, 2)
