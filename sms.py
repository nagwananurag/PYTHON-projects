from twilio.rest import Client


account_sid = "YOUR_ACCOUNT_SID"

auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    
    body="Hello via Python!,nice to meet you ",
    from_="+919034233114",   
    to="+91620379191392"     
)

print("Message sent:", message.sid)
