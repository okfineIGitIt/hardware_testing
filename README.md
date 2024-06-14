#  Hardware Testing Design Challenge

## Pre-requisites
- Machine running Windows operating system
    - Windows 11 used for testing (Windows 10 should also work)
- Python installed on above machine
    - Make sure the python executable path is added to the Windows PATH
        environment variable.
    - Exact version used for testing: python-3.11.2
    - Version 3.8 and above will likely work, but not gauranteed
- Git installed on above machine
    - Version used for testing: Git-2.42.0.2

## Development/Testing

### Setup
Clone repository into directory of your choosing:

`local_folder>git clone https://github.com/okfineIGitIt/hardware_testing.git`

A folder called "hardware_testing" should now be in your directory.


### Testing
To run the test suite, open a terminal in the "hardware_testing" folder above.

Run the following command from the terminal:

`.../hardware_testing>python DeviceA_Test_Suite.py`

This should produce some output in the terminal showing device operations and
test statuses.