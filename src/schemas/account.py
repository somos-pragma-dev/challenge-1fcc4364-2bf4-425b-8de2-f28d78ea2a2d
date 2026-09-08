from pydantic import BaseModel

class AccountCreate(BaseModel):
    account_number: str
    balance: float
    account_type: str
    client_id: int

class AccountUpdate(BaseModel):
    balance: float
    account_type: str