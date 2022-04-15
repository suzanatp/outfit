from django.urls import reverse

from tests.base.main_test_case import MainTestCase


class CreateOutfitViewTest(MainTestCase):
    def test_createOutfitGet_whenLoggedIn_shouldRenderTemplate(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create outfit'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'web/outfit/create_outfit.html')
