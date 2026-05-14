from fastapi import FastAPI, Request
import stripe
import os
import uvicorn

app = FastAPI()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
endpoint_secret = os.getenv("WEBHOOK_SECRET")

@app.post('/webhook')
async def stripe_webhook(request: Request):
    payload = await request.body()
    print(payload)
    return {"status": "success"}


if __name__=='__main__':
    uvicorn.run('main:app',port=8000,reload=True)


