from django.urls import reverse

from tests.base.main_test_case import MainTestCase


class LoginViewTest(MainTestCase):
    def test_loginSuccess_shouldRedirectToDashboard(self):
        response = self.client.post(reverse('login user'), data={'username': 'test', 'password': 'qHgbyRTQGphce3m'})
        self.assertEqual(302, response.status_code)
        self.assertEqual('/dashboard/', response.headers['location'])

