from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class MyAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1) #Online Members
        self.writeBoolean(True)
        self.writeDataReference(25, 2) # Role

        self.writeLong(0, 1) # Hid
        self.writeString("<c3f00ff>L<c7f00ff>W<cbf00ff> <cff00ff>B<cff00bf>r<cff007f>a<cff003f>w<cff0000>l</c>")
        self.writeDataReference(8, 19) # Badge
        self.writeVInt(3) # Type
        self.writeVInt(1) # Total Members
        self.writeVInt(50000) # Total Trophies
        self.writeVInt(0) # Trophies Required
        self.writeDataReference(0)
        self.writeString("UA") # Region
        self.writeVInt(0)
        self.writeBoolean(True) # Family Friendly
        self.writeVInt(0)

        self.writeBoolean(False)
        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24399

    def getMessageVersion(self):
        return self.messageVersion