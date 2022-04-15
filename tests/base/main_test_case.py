from django.contrib.auth import get_user_model
from django.test import TestCase

from outfit.web.models import Outfit, OutfitPhoto, Comment, Like, Dislike

UserModel = get_user_model()


class MainTestCase(TestCase):
    USERNAME = 'test'
    PASSWORD = 'qHgbyRTQGphce3m'

    def setUp(self):
        self.user = UserModel.objects.create_user(
            username=MainTestCase.USERNAME,
            password=MainTestCase.PASSWORD,
        )
        # self.user.is_active = True
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def create_new_user(self):
        self.new_user = UserModel.objects.create_user(
            username='newtest',
            password=MainTestCase.PASSWORD,
        )
        # self.new_user.is_active = True
        self.new_user.save()

    def create_outfit(self):
        self.outfit = Outfit.objects.create(
            user=self.user,
            name='test name',
            category='Casual',
            season='summer',
            weather='Sunny',
        )

    def create_photo(self):
        self.photo = OutfitPhoto.objects.create(
            photo=None,
            description='test description',
            price='$',
            outfit_id_id=self.outfit.id,
            user=self.user,
        )

    def create_comment(self):
        self.comment = Comment.objects.create(
            outfit=self.outfit,
            user=self.user,
            text='test text'
        )

    def create_like(self):
        self.like = Like.objects.create(
            photo=self.photo,
            user=self.user,
        )

    def create_dislike(self):
        self.dislike = Dislike.objects.create(
            photo=self.photo,
            user=self.user,
        )
