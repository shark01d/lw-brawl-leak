from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class AllianceStreamEntryMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(2) # Event
        self.writeVInt(0)
        self.writeVInt(0) # NumEvent
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeString("F1ash")
        self.writeVInt(2) # Role
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeString("Добро пожаловать!\nСпасибо что ты играешь на нашем сервере")
        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24312

    def getMessageVersion(self):
        return self.messageVersion