from devices.deviceA import DeviceA
from drivers.rs422_driver import RS422Driver

"""
Future considerations should include:
- Test manager class could be useful for assigning and naming device objects for better
    organisation. Could be useful for running tests for multiple devices at the
    same time.

- If many devices are being tested simultaneously or if test is running for a
    long time, might need tests running in separate threads.

- Ability for operators running tests to monitor, stop, rerun tests in an
    intuitive way.

- Inclusion of config files for tracking device parameters, test parameters, etc.

- Logging of results
"""
def run_quick_test():
    test_successful = True
    command = "QUICK"
    expected_response = "QUICK"

    driver = RS422Driver()
    device = DeviceA(driver, "172.168.10.10")

    device.Initialize()

    # check to ensure init worked

    device.SendCommand(command)

    # Check here to see if send was successful.
    # Check telemetry from device as well for indication
    # of successful operation

    response = device.ReceiveCommand()

    try:
        assert(response == expected_response)
    except AssertionError as ae:
        test_successful = False
        print(ae)

    if test_successful:
        print("Quick test successful")
    else:
        print("Quick test unsuccessful")

    # Teardown
    # In testing frameworks like pytest there would be a teardown method
    # (and test function decorators and helpers) which would always be
    # executed after a test is complete regardless of success or failure,
    # keeping this example minimal.
    # However a proper test framework of some sort is required for more extensive/formal
    # testing.
    device.Shutdown()


def run_full_test():
    test_successful = True
    command = "FULL"
    expected_response = "FULL"

    driver = RS422Driver()
    device = DeviceA(driver, "172.168.10.10")

    device.Initialize()

    # maybe do check to ensure init worked

    device.SendCommand(command)

    # maybe check here to see if send was successful
    # check telemetry from device as well for indication
    # of successful operation

    response = device.ReceiveCommand()

    try:
        assert(response == expected_response)
    except AssertionError as ae:
        test_successful = False
        print(ae)

    if test_successful:
        print("Full test successful")
    else:
        print("Full test unsuccessful")

    device.Shutdown()


if __name__ == "__main__":
    run_quick_test()
    run_full_test()
    print("Tests complete!")