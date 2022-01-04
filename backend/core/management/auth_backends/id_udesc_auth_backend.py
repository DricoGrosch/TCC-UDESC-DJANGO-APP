from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class IDUdescAuthBackend(BaseBackend):
    def remote_authentication(self, username, password):
        return True

    def create_user(self, username, password):
        user, created = get_user_model().objects.get_or_create(username=username)
        user.set_password(password)
        user.save()
        return user

    def authenticate(self, request, username=None, password=None):
        if self.remote_authentication(username, password):
            return self.create_user(username, password)
        return None
