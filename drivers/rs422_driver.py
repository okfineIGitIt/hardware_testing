from drivers.abstract_driver import AbstractDriver


class RS422Driver(AbstractDriver):
    def __init__(self) -> None:
        self._is_connected = False
        self._last_message = ""
    
    def Connect(self):
        if not self._is_connected:
            # do something to connect to actual device here
            self._is_connected = True 

    def Disconnect(self):
        if self._is_connected:
            # do something to disconnect here
            self._is_connected = False

    def Send(self, message):
        # some code to send message
        self._last_message = message

    def Receive(self):
        # Since design mentions that "QUICK" and "FULL" command messages are
        # returned, will just return the last message sent through this protocol.
        message_to_send = self._last_message
        self._last_message = "" # assuming device has buffer which gets cleared
        
        return message_to_send
         