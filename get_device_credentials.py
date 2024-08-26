from pyhiveapi import Hive, SMS_REQUIRED
from getpass import getpass

#get the hive username and password
username = input("Enter the hive username: ")
password = getpass("Enter the hive password: ")

#perform initial authentication
session = Hive(username=username, password=password)
login = session.login()

#catch the SMS challenge and prompt for the 2FA code
if login.get("ChallengeName") == SMS_REQUIRED:
    code = input("Enter 2FA code: ")
    session.sms2fa(code, login)

#Prompt for a device name and register it
device_name = input("Enter a name for the device: ")
session.auth.device_registration(device_name=device_name)

#get the device credentials and output them:
deviceData = session.auth.get_device_data()
#print(deviceData)
print("Device Group Key: "+session.auth.device_group_key)
print("Device Key: "+session.auth.device_key)
print("Device Password: "+session.auth.device_password)
