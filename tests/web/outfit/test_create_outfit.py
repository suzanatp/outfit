from django.urls import reverse

from outfit.web.models import Outfit
from tests.base.main_test_case import MainTestCase


class CreateRecipeViewTest(MainTestCase):
    def test_createOutfitGet_whenLoggedIn_shouldRenderTemplate(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create outfit'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'web/outfit/create_outfit.html')

    # def test_createRecipePost_shouldCreateRecipe(self):
    #     self.client.force_login(self.user)
    #     self.client.post(
    #         reverse('create outfit'),
    #         data={
    #             'user': self.user,
    #             'name': 'test name',
    #             'category': 'Casual',
    #             'season': 'summer',
    #             'weather': 'Sunny',
    #         }
    #     )
    #     outfit = Outfit.objects.first()
    #     self.assertNotEqual(None, outfit)
