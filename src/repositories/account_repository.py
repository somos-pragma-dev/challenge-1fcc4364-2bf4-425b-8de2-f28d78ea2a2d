from sqlalchemy.orm import Session
from src.models.account import Account

class AccountRepository:
    def create_account(self, db: Session, account: Account):
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

    def get_account(self, db: Session, account_id: int):
        return db.query(Account).filter(Account.id == account_id).first()

    def update_account(self, db: Session, account_id: int, account_data: dict):
        db_account = db.query(Account).filter(Account.id == account_id).first()
        if db_account is None:
            return None
        for key, value in account_data.items():
            setattr(db_account, key, value)
        db.commit()
        db.refresh(db_account)
        return db_account

    def delete_account(self, db: Session, account_id: int):
        db_account = db.query(Account).filter(Account.id == account_id).first()
        if db_account is None:
            return False
        db.delete(db_account)
        db.commit()
        return True