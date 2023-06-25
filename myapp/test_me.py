import gc
from unittest import TestCase

from django.test import Client

from myapp.models import Group, MyUser


def wrap(func):
    return lambda *args, **kwargs: func(*args, **kwargs)


class UpdateCustomProfileFieldTest(TestCase):
    @wrap
    @wrap
    @wrap
    @wrap
    @wrap
    @wrap
    @wrap
    @wrap
    @wrap
    def test_me(self):
        group, group_created = Group.objects.get_or_create(groupname="admin")
        user, user_created = MyUser.objects.get_or_create(username="admin", group=group)
        client = Client()
        client.force_login(user)
        client.post("/me")
        gc.freeze()
        for count in range(150, 250):
            print(count)
            gc.set_threshold(count, 0, 0)
            gc.collect()
            client.post("/me")
            client.post("/me")
