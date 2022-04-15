from django.urls import reverse

from tests.base.main_test_case import MainTestCase


class LoginViewTest(MainTestCase):
    def test_loginSuccess_shouldRedirectToDashboard(self):
        response = self.client.post(reverse('login user'), data={'username': 'test', 'password': 'qHgbyRTQGphce3m'})
        self.assertEqual(302, response.status_code)
        self.assertEqual('/dashboard/', response.headers['location'])

    # def test_wrong_username(self):
    #     response = self.client.post(reverse('login user'), data={'username': 'wrong', 'password': 'qHgbyRTQGphce3m'})
    #     self.assertEqual(200, response.status_code)
    #     errors = response.context_data['form'].get('errors')
    #     default_error = 'Please enter a correct email and password. Note that both fields may be case-sensitive.'
    #     self.assertIn(default_error, errors)
    #
    # def test_wrong_password(self):
    #     response = self.client.post(reverse('login user'), {'username': 'test', 'password': 'wrong'})
    #     self.assertEqual(200, response.status_code)
    #     errors = response.context_data['form'].errors['password']
    #     default_error = 'Please enter a correct email and password. Note that both fields may be case-sensitive.'
    #     self.assertIn(default_error, errors)