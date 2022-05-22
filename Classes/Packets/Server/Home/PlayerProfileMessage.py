from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer([fields["HighID"], fields["LowID"]])


        self.writeVInt(fields["HighID"])
        self.writeVInt(fields["LowID"])
        self.writeBoolean(False)

        self.writeVInt(55)

        for i in range(54):
            self.writeDataReference(16, i)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(11)
        
        self.writeDataReference(16, 54)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(11)

        self.writeVInt(15)

        self.writeVInt(1)
        self.writeVInt(4444) # 3v3 Victories

        self.writeVInt(2)
        self.writeVInt(999999) # Experince

        self.writeVInt(3)
        self.writeVInt(50000) # Current Trophies

        self.writeVInt(4)
        self.writeVInt(50000) # Highest Trophies

        self.writeVInt(5)
        self.writeVInt(55)

        self.writeVInt(7)
        self.writeVInt(28000000 + playerData["Thumbnail"]) # Profile Icon

        self.writeVInt(8)
        self.writeVInt(4444) # Solo Victories

        self.writeVInt(9)
        self.writeVInt(21) # Highest Robo Rumble LVL Passed

        self.writeVInt(11)
        self.writeVInt(4444) # Duo Victories

        self.writeVInt(12)
        self.writeVInt(21) # Highest Boss Fight LVL Passed

        self.writeVInt(15)
        self.writeVInt(15) # Most Challenge Wins

        self.writeVInt(16)
        self.writeVInt(21) # Highest Rampage LVL Passed

        self.writeVInt(17)
        self.writeVInt(19) # Highest Team League

        self.writeVInt(18)
        self.writeVInt(19) # Highest Solo League

        self.writeVInt(19)
        self.writeVInt(19) # Highest Club League


        self.writeString(playerData["Name"])
        self.writeVInt(0)
        self.writeVInt(playerData["Thumbnail"] + 28000000)
        self.writeVInt(43000000 + playerData["Namecolor"])
        self.writeVInt(0)

        self.writeBoolean(True)  # Is in club

        self.writeInt(0)
        self.writeInt(1) # Club ID
        self.writeString("<c3f00ff>L<c7f00ff>W<cbf00ff> <cff00ff>B<cff00bf>r<cff007f>a<cff003f>w<cff0000>l</c>")  # Club name
        self.writeVInt(8)
        self.writeVInt(19)  # Club badgeID
        self.writeVInt(3)  # Club type | 1 = Open, 2 = invite only, 3 = closed
        self.writeVInt(1)  # Current members count
        self.writeVInt(0) # Club Trophies
        self.writeVInt(0)  # Trophy required
        self.writeVInt(0)  # Unknown
        self.writeString("UA")  # Location
        self.writeVInt(0)  # Unknown
        self.writeVInt(0) # Unknown
        self.writeVInt(25)
        self.writeVInt(2)
        

        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion