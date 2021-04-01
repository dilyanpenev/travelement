from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm


class PostFormTest(TestCase):

    def test_user_cannot_have_two_posts_with_same_name(self):
        client = User.objects.create_user(username='test')
        p1 = Post(title='A', user=client, description="abc")
        p1.save()
        form = PostForm(
            data={'title': 'A', 'description': 'bcd'}, user=client)
        self.assertFalse(form.is_valid())

    def test_different_users_can_have_posts_with_same_name(self):
        client1 = User.objects.create_user(username='test1')
        client2 = User.objects.create_user(username='test2')
        p1 = Post(title='A', user=client1, description="abc")
        p1.save()
        form = PostForm(
            data={'title': 'A', 'description': 'bcd'}, user=client2)
        self.assertTrue(form.is_valid())

    def test_title_is_required(self):
        client = User.objects.create_user(username='test')
        form = PostForm(
            data={'title': '', 'description': 'bcd'}, user=client)
        self.assertFalse(form.is_valid())

    def test_long_title_is_invalid(self):
        client = User.objects.create_user(username='test')
        long_string = 'NrhqDu6WiO1yhsN8McGCVSNXRHwbEgT6IKoEDLINLd5GTXQu5kOtGtLq9Lfvo'
        form = PostForm(
            data={'title': long_string, 'description': 'bcd'}, user=client)
        self.assertFalse(form.is_valid())

    def test_description_is_required(self):
        client = User.objects.create_user(username='test')
        form = PostForm(
            data={'title': 'A', 'description': ''}, user=client)
        self.assertFalse(form.is_valid())

    def test_long_description_is_invalid(self):
        client = User.objects.create_user(username='test')
        long_string = """ whI3lb0nTp8tpvd1Hqo1IpyBbFL7mGMzCf1dSipIRkFbRpjcW4gb5k4AhX
        PtFFuQzWU95JbOg8My9NygFdusi3PiimiZiKmyqL6StmshH4RNsCqJMBeaEe9u3Dmua3UHgvkub0
        mngeY9a1ODWb0mgdEzpz82f3XXfTKeye9oaMwUMpZe7ceaw79puGRKqlPaNlRqmqAl2thbZ0Qbco
        qv14LAKEen0LctH8vHqHu3ooDVpKN0WIz0RnKBVPVGbqRJxT3SmwXSNJzwAaafPfxzPwKxaLUrHJ2
        aPLof2ksaPfREj4o2z80Uot1C4roBJXCqgrI53fEzg8zeywKtAk0cOdlrFKTL4GrPiukGl8168Ue
        wDTwoAtUUeWhsjculKhXRnIzDoh8NemmM5xd0yQUfgMAVCW9nMpbTirlNAjucQEeJ33UMNRWEyNL
        B40wtSgK2lx3H4sU4wz2OrKlVvUhmRigCNKb4rEmlugGZRcTL6zsCSFA0c3PT3MDY2hKGvOwR4qO
        AtRzFlAWsgMYvJJs2BsElj9dTe9WFv5uyb1Qdl9CCQFAN5PC49Y55OUlyMWjYCZ8Y7GhQTJAWU3E
        OmpYhu17KG """
        form = PostForm(
            data={'title': 'A', 'description': long_string}, user=client)
        self.assertFalse(form.is_valid())
