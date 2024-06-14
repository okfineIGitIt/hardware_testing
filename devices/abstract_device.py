"""
Contains AbstractDevice class, which should be used as a parent class to 
create Device classes.
"""

from abc import ABC, abstractmethod


class AbstractDevice(ABC):
    @abstractmethod
    def Initialize(self):
        pass

    @abstractmethod
    def Shutdown(self):
        pass

    @abstractmethod
    def SendCommand(self, command_str):
        pass

    @abstractmethod
    def ReceiveCommand(self):
        pass