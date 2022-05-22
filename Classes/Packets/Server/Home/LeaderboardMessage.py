from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class LeaderboardMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("UA")

        self.writeVInt(1)

        for i in [player.Name]:

            self.writeVInt(0)
            self.writeVInt(1)

            self.writeVInt(1)
            self.writeVInt(player.Trophies) # Trophies

            self.writeVInt(1)
            self.writeString("<c3f00ff>L<c7f00ff>W<cbf00ff> <cff00ff>B<cff00bf>r<cff007f>a<cff003f>w<cff0000>l</c>")

            self.writeString(i)
            self.writeVInt(0)
            self.writeVInt(28000000 + player.Thumbnail)
            self.writeVInt(43000000 + player.Namecolor)
            self.writeVInt(46000000)
            self.writeVInt(0) #UNK

        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("UA")

        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24403

    def getMessageVersion(self):
        return self.messageVersion