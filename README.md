# get_device_credentials.py #
This utility is for the Hive Home heating system from British Gas.  It will register the current device as a known device and display the device credentials.  The device credentials can then be used to authenticate without SMS 2FA.

It prompts the user to enter their username, password and then performs an authentication.  The authentication journey will issue a 2FA code via SMS which must then be supplied to complete the login.

Once the 2FA authentication is complete, the user is prompted to enter a name for the device.  The device is saved as a known device and will then be visible via the Hive app.

The script will then output the device credentials which can then be used to perform a device authentication, thereby removing the need for an SMS 2FA.

## Credits ##
This script leverages the [pyhiveapi library](https://github.com/Pyhass/Pyhiveapi).

## Usage ##
The pyhiveapi must be pip installed before the script will work.  It would be best to do this in a [python virtual environment](https://docs.python.org/3/tutorial/venv.html).

    pytpip install pyhiveapi

