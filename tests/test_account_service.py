from unittest import Isolate
from src.services.account_service import AccountService
from src.schemas.account import AccountCreate, AccountUpdate

class TestAccountService(Isolate):
    def setUp(self):
        self.account_service = AccountService()
        self.account_data = AccountCreate(account_number='1234567890', balance=100.0, account_type='savings', client_id=1)

    def test_create_account(self):
        account = self.account_service.create_account(self.account_data)
        self.assertEqual(account.account_number, self.account_data.account_number)
        self.assertEqual(account.balance, self.account_data.balance)
        self.assertEqual(account.account_type, self.account_data.account_type)
        self.assertEqual(account.client_id, self.account_data.client_id)

    def test_get_account(self):
        account = self.account_service.get_account(1)
        self.assertIsNotNone(account)

    def test_update_account(self):
        account_update = AccountUpdate(balance=200.0, account_type='checking')
        updated_account = self.account_service.update_account(1, account_update)
        self.assertEqual(updated_account.balance, account_update.balance)
        self.assertEqual(updated_account.account_type, account_update.account_type)

    def test_delete_account(self):
        success = self.account_service.delete_account(1)
        self.assertTrue(success)