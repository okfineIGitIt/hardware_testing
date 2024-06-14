from enum import Enum

from devices.abstract_device import AbstractDevice
from drivers.abstract_driver import AbstractDriver


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

    def SendCommand(self, command_str) -> bool:
        self._driver.Send(command_str)
    
    def ReceiveCommand(self):
        return self._driver.Receive()
