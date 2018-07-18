from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class SmokeTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    # django uses resolve() to map a URL to the corresponding view function
    found = resolve('/')
    self.assertEqual(found.func, home_page)


  def test_home_page_returns_correct_html(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home.html')






