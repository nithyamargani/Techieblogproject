from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostModelTests(TestCase):

    def test_str_representation(self):
        post = Post(title="Test title", body="Test body")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        post = Post(title="Test title", body="Test body")
        self.assertEqual(f"{post.title}", "Test title")
        self.assertEqual(f"{post.body}", "Test body")

class PostListViewTests(TestCase):

    def setUp(self):
        Post.objects.create(title='Test title 1', body='Test body 1')
        Post.objects.create(title='Test title 2', body='Test body 2')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('post_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('post_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/post_list.html')
