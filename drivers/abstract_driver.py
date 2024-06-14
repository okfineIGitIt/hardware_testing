"""
Contains AbstractDriver class, which should be used as a parent class to 
create Driver classes.
"""
from abc import ABC, abstractmethod


class AbstractDriver(ABC):
    @abstractmethod
    def Connect(self):
        pass

    @abstractmethod
    def Disconnect(self):
        pass

    @abstractmethod
    def Send(self, message):
        pass

    @abstractmethod
    def Receive(self) -> str:
        pass