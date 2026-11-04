from django.test import TestCase
from ..models import Tarea


class TareaTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tarea = Tarea.objects.create(titulo = "Tarea de ejemplo")


    #Este seria un ejemplo de un test innecesario
    # Ya que solamente está revisando si los datos se guardan. Pero Django siempre hace eso
    def test_tarea_contenido(self):
        self.assertEqual(self.tarea.titulo,'Tarea de ejemplo')
        self.assertFalse(self.tarea.completed)
        self.assertTrue(self.tarea.created_at)


    # Un test correctamente usado sería cuando se implemente una lógica unica
    # Cosas como sobrescribir alguna función, validaciones, etc
    