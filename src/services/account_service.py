from sqlalchemy.orm import Session
from src.models.account import Account
from src.schemas.account import AccountCreate, AccountUpdate

class AccountService:
    async def create_account(self, db: Session, account: AccountCreate):
        db_account = Account(**account.dict())
        db.add(db_account)
        await db.commit()
        await db.refresh(db_account)
        return db_account

    async def get_account(self, db: Session, account_id: int):
        return db.query(Account).filter(Account.id == account_id).first()

    async def update_account(self, db: Session, account_id: int, account: AccountUpdate):
        db_account = db.query(Account).filter(Account.id == account_id).first()
        if db_account is None:
            return None
        for key, value in account.dict().items():
            setattr(db_account, key, value)
        await db.commit()
        await db.refresh(db_account)
        return db_account

    async def delete_account(self, db: Session, account_id: int):
        db_account = db.query(Account).filter(Account.id == account_id).first()
        if db_account is None:
            return False
        db.delete(db_account)
        await db.commit()
        return True