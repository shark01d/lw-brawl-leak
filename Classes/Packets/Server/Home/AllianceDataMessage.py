from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class AllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):

        self.writeBoolean(False)

        self.writeLong(0, 1) # hlid
        self.writeString("<c3f00ff>L<c7f00ff>W<cbf00ff> <cff00ff>B<cff00bf>r<cff007f>a<cff003f>w<cff0000>l</c>") # Name
        self.writeDataReference(8, 19) # Badge
        self.writeVInt(3) # Type
        self.writeVInt(1)  # Total Members
        self.writeVInt(50000)  # Total Trophies
        self.writeVInt(0)  # Trophies Required
        self.writeDataReference(0)
        self.writeString("UA")  # Region
        self.writeVInt(0)
        self.writeBoolean(True)  # Family Friendly
        self.writeVInt(0)

        self.writeString("Добро пожаловать!\nНаш телеграм: @lwbrawl\nНаш дискорд: https://discord.gg/StWwEc9Jtj") # Description

        self.writeVInt(1) # Members Count
        for i in range(1):
            self.writeLong(player.ID[0], player.ID[1])
            self.writeVInt(2) # Role
            self.writeVInt(player.Trophies) # Trophies
            self.writeVInt(0) # Player State TODO: Members state
            self.writeVInt(0) # State Timer

            # whatIsThat = 5
            self.writeVInt(1)
            self.writeVInt(1) # idk
            self.writeVInt(19) # Power League Rank
            self.writeBoolean(False) # DoNotDisturb TODO: Do not disturb sync

            self.writeString(player.Name) # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000) # Player Thumbnail
            self.writeVInt(43000000) # Player Name Color
            self.writeVInt(46000001) # Color Gradients

            self.writeVInt(-1)
            self.writeBoolean(False)

            self.writeVInt(0) # Club Leauge?
        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24301

    def getMessageVersion(self):
        return self.messageVersion