from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.schemas.account import AccountCreate, AccountUpdate
from src.services.account_service import AccountService

app = FastAPI()

@app.post('/accounts/', response_model=AccountCreate)
async def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    try:
        return await account_service.create_account(db, account)
    except IntegrityError:
        raise HTTPException(status_code=400, detail='Account already exists')

@app.get('/accounts/{account_id}', response_model=AccountCreate)
async def read_account(account_id: int, db: Session = Depends(get_db)):
    account = await account_service.get_account(db, account_id)
    if account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return account

@app.put('/accounts/{account_id}', response_model=AccountCreate)
async def update_account(account_id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    updated_account = await account_service.update_account(db, account_id, account)
    if updated_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return updated_account

@app.delete('/accounts/{account_id}')
async def delete_account(account_id: int, db: Session = Depends(get_db)):
    success = await account_service.delete_account(db, account_id)
    if not success:
        raise HTTPException(status_code=404, detail='Account not found')
    return {'detail': 'Account deleted'}