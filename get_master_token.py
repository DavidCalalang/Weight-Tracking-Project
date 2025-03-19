import gpsoauth
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('email')
password = os.getenv('password')
android_id = '0123456789abcdef'
device_country = "us"
operator_country = "us"
app = "com.google.android.gsf"
api_version = "3"

master_token = gpsoauth.perform_master_login(
            email,
            password,
            android_id,
            device_country,
            operator_country,
            app,
            api_version,
        )

print(master_token)


"""
master_response = gpsoauth.perform_master_login(email, password, android_id)
master_token = master_response['Token']

auth_response = get_master_token.perform_oauth(
    email, master_token, android_id,
    service='sj', app='com.google.android.gsf',
    client_sig='...')
token = auth_response['Auth']"
"""