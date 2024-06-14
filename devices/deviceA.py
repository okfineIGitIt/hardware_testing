from devices.abstract_device import AbstractDevice
from drivers.abstract_driver import AbstractDriver

"""
Some improvements to be made on the Device level:
- Better error handling: Implement "enums" for different types of device errors
    that could occur

- State tracking: same vein as above, should have defined states for device
    and way to query those states
"""
class DeviceA(AbstractDevice):
    def __init__(self, driver: AbstractDriver, device_address):
        if not isinstance(driver, AbstractDriver):
            raise TypeError(f"driver object passed into {self.__class__} object must be derived from AbstractDriver class")
        
        self._driver = driver
        self._device_address = device_address

    def Initialize(self):
        self._driver.Connect()
        print("Initialized Device A")

    def Shutdown(self):
        self._driver.Disconnect()
        print("Device A shut down")

    def SendCommand(self, command_str):
        self._driver.Send(command_str)
    
    def ReceiveCommand(self):
        return self._driver.Receive()
