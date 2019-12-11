from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):

    def setUp(self):
        """ This function will be ran first."""
        # simulate a client
        self.client = Client()

        # create new SUPERUSER and USER
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='password123'
        )
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='password123',
            name='Test User Full Name',
        )

        # simulate a client logged
        self.client.force_login(self.admin_user)


    def test_users_listed(self):
        """ Test that users are listed on the user page """
        # get url /admin/user/
        url = reverse('admin:core_user_changelist')
        # create get request
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """Test that the user edit page works"""
        # /admin/user/{self.user.id}
        url = reverse('admin:core_user_change', args=[self.user.id])
        # create request
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
