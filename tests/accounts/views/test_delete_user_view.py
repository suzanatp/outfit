from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.main_test_case import MainTestCase

UserModel = get_user_model()


class DeleteUserViewTest(MainTestCase):
    def test_deleteUserSuccess_shouldDeleteUserAndRedirectToIndex(self):
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.post(reverse('delete profile', args=(self.user.id, )))
        user = UserModel.objects.first()
        self.assertIsNone(user)
        self.assertEqual(302, response.status_code)
        self.assertEqual(reverse('index'), response.headers['location'])

    # def test_deleteUserCancel_shouldRedirectToUpdateProfile(self):
    #     self.client.login(username=self.EMAIL, password=self.PASSWORD)
    #     response = self.client.post(reverse('delete-user', args=(self.user.id, )), data={'cancel': 'cancel'})
    #     user = UserModel.objects.first()
    #     self.assertIsNotNone(user)
    #     self.assertEqual(302, response.status_code)
    #     self.assertEqual(reverse('update-profile'), response.headers['location'])