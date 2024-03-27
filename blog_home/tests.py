from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Testuser",
            email="testuser@gmail.com",
            password="testsecrettestuser"
        )

        self.post = Post.objects.create(
            title="Newpost",
            text="LoremIpsum, hddsj kaer",
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title="Newpost")
        self.assertEqual(str(Post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Newpost")
        self.assertEqual(f"{self.post.author}", "Testuser")
        self.assertEqual(f"{self.post.text}", "LoremIpsum, hddsj kaer")

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "LoremIpsum, hddsj kaer")
        self.assertTemplateUsed(response, "blog_home.html")

    def test_post_detail_view(self):
        response = self.client.get("/post/1/")
        no_response = self.client.get("/post/100000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Newpost")
        self.assertTemplateUsed(response, "post_detail.html")
