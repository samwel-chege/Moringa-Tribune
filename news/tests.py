from django.test import TestCase
from .models import Editor,tags,Article

# Create your tests here.
class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.sammie= Editor(first_name = 'Sammie',last_name= 'Sam',email = 'sammiesam@gmail.com')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sammie,Editor))   

    #testing save method
    def test_save_method(self):
        self.sammie.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)> 0)    