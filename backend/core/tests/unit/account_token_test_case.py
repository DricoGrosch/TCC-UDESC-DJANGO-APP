from datetime import timedelta

from decouple import config
from django.test import TestCase

from backend.core.models import AccountCreationToken


class AccountTokenTestCase(TestCase):
    def setUp(self) -> None:
        self.token = AccountCreationToken.objects.create(email=config('EMAIL_HOST_USER'))

    def test_account_token_already_used_validation(self):
        self.token.use()
        self.assertFalse(self.token.is_valid())

    def test_account_token_use(self):
        self.assertFalse(self.token.used)
        self.token.use()
        self.assertTrue(self.token.used)

    def test_account_token_time_validation(self):
        self.token.created_at = self.token.created_at - timedelta(minutes=10)
        self.token.save()
        self.assertFalse(self.token.is_valid())

    def test_valid_email(self):
        self.assertTrue(AccountCreationToken.is_email_allowed(config('EMAIL_HOST_USER')))

    def test_invalid_email(self):
        self.assertFalse(AccountCreationToken.is_email_allowed('adriangrosch15@gmail.com'))
