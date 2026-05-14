### https://dashboard.stripe.com/

### terminal 1: [uv run] uvicorn main:app --reload 
### terminal 2: stripe listen --forward-to localhost:8000/webhook
### terminal 3: stripe trigger payment_intent.succeeded

Require environment vars STRIPE_SECRET_KEY and WEBHOOK_SECRET
where WEBHOOK_SECRET will be revealed (left empty) when running "stripe listen"
