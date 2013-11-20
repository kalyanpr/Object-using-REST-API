import requests

consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CUSTOMER_SECRET"
username = "YOUR_USER_NAME"
password = "YOUR_PASSWORD"
security_token = "YOUR_SECURITY_TOKEN"
 
payload = {
    'grant_type': 'password',
    'client_id': consumer_key,
    'client_secret': consumer_secret,
    'username': username,
    'password': password + security_token
}
 
r = requests.post("https://login.salesforce.com/services/oauth2/token", 
    headers={"Content-Type":"application/x-www-form-urlencoded"},
    data=payload)
 
print r.content