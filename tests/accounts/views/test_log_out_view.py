from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.main_test_case import MainTestCase

UserModel = get_user_model()


class LogOutViewTest(MainTestCase):
    def tearDown(self):
        self.user.delete()

    def test_signOutSuccess_shouldRedirectToIndex(self):
        is_logged_in = self.client.login(username=self.USERNAME, password=self.PASSWORD)
        self.assertTrue(is_logged_in)
        response = self.client.get(reverse('logout user'), follow=False)
        self.assertEqual(302, response.status_code)
        self.assertEqual(reverse('index'), response.headers['location'])