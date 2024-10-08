# get_device_credentials.py #
This utility is for the Hive Home heating system from British Gas.  It will register the current device as a known device and display the device credentials.  The device credentials can then be used to authenticate without SMS 2FA.

It prompts the user to enter their username, password and then performs an authentication.  The authentication journey will issue a 2FA code via SMS which must then be supplied to complete the login.

Once the 2FA authentication is complete, the user is prompted to enter a name for the device.  The device is saved as a known device and will then be visible via the Hive app.

The script will then output the device credentials which can then be used to perform a device authentication, thereby removing the need for an SMS 2FA.

The check_device_auth1.py script allows you to test device credentials.

## Credits ##
This script leverages the [pyhiveapi library](https://github.com/Pyhass/Pyhiveapi).

## Usage ##
The pyhiveapi must be pip installed before the script will work.  It would be best to do this in a [python virtual environment](https://docs.python.org/3/tutorial/venv.html):

    python3 -m venv .venv
    . ./.venv/bin/activate
    pip install pyhiveapi

Then clone this repo and run the script:

    git clone git@github.com:srsplunk/hive-get-device-credentials.git
    cd hive-get-device-credentials
    python3 get_device_credentials.py

## Check Device ##
Once the script has been run successfully, the device should be listed in the Hive App:
* From Home select Manage
* Scroll down and select Account Security
* Select Your Trusted Devices
* Check your new device is listed

## check_device_auth1.py ##

This script allows you to test device credentials.  It prompts for the hive username, password, device key, device group key and device password.  If successful it will then output all the devices found that can output a current temperature.
