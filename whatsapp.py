from twilio.rest import Client 
 
account_sid = 'AC09bd4e98ec4222ddfb4a2c32b975b945' 
auth_token = '2a90466c8f32d8ba7f78690a10831acb' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+56998019951'
                              , body='hola webong',      
                              to='whatsapp:+56988032319' 
                          ) 
 
print(message.sid)