from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class AskForAllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        self.readInt()
        self.readInt()
        self.readBoolean()
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24301, fields, calling_instance.player)

    def getMessageType(self):
        return 14302

    def getMessageVersion(self):
        return self.messageVersion