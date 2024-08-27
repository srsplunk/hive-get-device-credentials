from pyhiveapi import Hive, SMS_REQUIRED
from getpass import getpass

#get the hive username and password
username = input("Enter the hive username: ")
password = getpass("Enter the hive password: ")

session = Hive(
  username=username,
  password=password)
  
device_group_key = input("Enter the device group key: ")
device_key = input("Enter the device key: ")
device_password = input("Enter the device password: ")

session.auth.device_group_key=device_group_key
session.auth.device_key=device_key
session.auth.device_password=device_password
session.deviceLogin()
devices = session.startSession()
print("Temperature devices found:")
for device in devices['sensor']:
  if device['hiveType'] == "Heating_Current_Temperature":
    print(device['hiveName'])