from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class ChatToAllianceStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Message"] = self.readString()
        print(fields["Message"])
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)        
        if fields["Message"] == "/full":
            for i in range(54):
                playerData["OwnedBrawlers"][f"{i}"]["Trophies"] = 1250
                playerData["OwnedBrawlers"][f"{i}"]["HighestTrophies"] = 1250
            playerData["OwnedBrawlers"][f"54"]["Trophies"] = 0
            playerData["OwnedBrawlers"][f"54"]["HighestTrophies"] = 1250
            playerData["Trophies"] = 1250
            playerData["ClubMessage"] = "Это секретно!"
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})
        elif fields["Message"] == "/help":
            playerData["ClubMessage"] = "Команды, доступные для тебя:\n/Пока-что нету"
        else:
            playerData["ClubMessage"] = fields["Message"]
        playerData["TickMessage"] = playerData["TickMessage"] + 1
        print(playerData["TickMessage"])
        db_instance.updatePlayerData(playerData, calling_instance)
        Messaging.sendMessage(24311, fields, calling_instance.player)

    def getMessageType(self):
        return 14315

    def getMessageVersion(self):
        return self.messageVersion