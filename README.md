#  Hardware Testing Design Challenge

## Pre-requisites
- Machine running Windows operating system
    - Windows 11 used for testing (Windows 10 should also work)
- Python installed on above machine
    - Make sure the python executable path is added to the Windows PATH
        environment variable
    - Exact version used for testing: python-3.11.2
    - Version 3.8 and above will likely work, but not gauranteed
- Git installed on above machine
    - Version used for testing: Git-2.42.0.2


## Setup
Clone repository into directory of your choosing:

`local_folder>git clone https://github.com/okfineIGitIt/hardware_testing.git`

A folder called "hardware_testing" should now be in your directory.


## Testing
To run the test suite, open a terminal in the "hardware_testing" folder above.

Run the following command from the terminal:

`.../hardware_testing>python DeviceA_Test_Suite.py`

This should produce some output in the terminal showing device operations and
test statuses.


## Development

The code in this repository is intended to be the basis of a hardware testing library.

There are 2 types of objects to facilitate this: devices and drivers.
Devices are the actual hardware devices that can be connected to, and the
drivers represent the communication protocols used to talk to said devices.

The devices are represented in code by the `AbstractDevice` class, located in
`hardware_testing/devices/abstract_device.py`, while the drivers are represented
by `AbstractDriver` located in `hardware_testing/drivers/abstract_driver.py`.

Device and driver classes created by developers should derive from these classes
to enforce a common interface among both object types.

Each device object will require a driver object to communicate with the target device.

An example of a device class `DeviceA` can be found in `hardware_testing/devices/deviceA.py`.
An example of a driver class `RS422Driver` can be found in `hardware_testing/drivers/rs422_driver.py`.

**Note**: For the purpose of this exercise, the `RS422Driver` will respond with
whatever command string it is instructed to send to the device.

## Testing
A sample script can be found in `hardware_testing/DeviceA_Test_Suite.py`.

To run the sample script, run the following command from the project repository:

`hardware_testing>python DeviceA_Test_Suite.py`