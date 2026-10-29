from django.test import TestCase
from ..models import Tarea


class TareaTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tarea = Tarea.objects.create(titulo = "Tarea de ejemplo")


    def test_tarea_contenido(self):
        self.assertEqual(self.tarea.titulo,'Tarea de ejemplo')
        self.assertEqual(self.tarea.completed,False)
        self.assertNotEqual(self.tarea.created_at,'')