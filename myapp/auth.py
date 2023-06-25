from myapp.models import MyUser


class MyAuthBackend:
    def get_user(self, user_id):
        return MyUser.objects.select_related().get(id=user_id)
