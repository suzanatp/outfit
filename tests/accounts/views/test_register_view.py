from django.test import TestCase
from django.urls import reverse

from outfit.accounts.forms import CreateProfileForm
from tests.base.main_test_case import MainTestCase


class SignUpViewTest(TestCase):
    def test_getSignUp_shouldRenderTemplateAndForm(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/registration_page.html')
        self.assertIsInstance(response.context_data['form'], CreateProfileForm)

    def test_register_whenFormValid_shouldRenderNeededHtml(self):
        response = self.client.post(reverse('register'), data={
            'email': MainTestCase.USERNAME,
            'password1': MainTestCase.PASSWORD,
            'password2': MainTestCase.PASSWORD,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/registration_page.html')

    def test_signUp_whenWrongPassword2_shouldReturnFormInvalid(self):
        response = self.client.post(reverse('register'), data={
            'username': MainTestCase.USERNAME,
            'password1': MainTestCase.PASSWORD,
            'password2': 'wrong pass2',
        })
        is_valid = response.context_data['form'].is_valid()
        self.assertFalse(is_valid)
        errors = response.context_data['form'].errors['password2']
        self.assertIn('The two password fields didn’t match.', errors)


