from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class SmokeTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    # django uses resolve() to map a URL to the corresponding view function
    found = resolve('/')
    self.assertEqual(found.func, home_page)
