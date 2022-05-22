from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler

class AskForBattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Result"] = self.readVInt()
        fields["Unk1"] = self.readVInt()
        fields["Rank"] = self.readVInt()
        fields["MapID"] = self.readDataReference()
        fields["HeroesCount"] = self.readVInt()
        


        fields["Heroes"] = []
        for i in range(fields["HeroesCount"]): fields["Heroes"].append({"Brawler": {"ID": self.readDataReference(), "SkinID": self.readDataReference()}, "Team": self.readVInt(), "IsPlayer": self.readBoolean(), "PlayerName": self.readString(), "Result": fields["Result"]})
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)
        playerData["Trophies"] = playerData["Trophies"] + 8
        brawler = fields["Heroes"][0]["Brawler"]["ID"][1]
        print(playerData["OwnedBrawlers"]["0"])
        playerData["OwnedBrawlers"][f"{brawler}"]["Trophies"] = playerData["OwnedBrawlers"][f"{brawler}"]["Trophies"] + 8
        playerData["OwnedBrawlers"][f"{brawler}"]["HighestTrophies"] = playerData["OwnedBrawlers"][f"{brawler}"]["HighestTrophies"] + 8    
        if playerData["power_rank"] != 19:
            playerData["power_rank"] = playerData["power_rank"] + 1
        playerData["match_played"] = playerData["match_played"] + 1             
        db_instance.updatePlayerData(playerData, calling_instance)
        Messaging.sendMessage(23456, fields, calling_instance.player)

    def getMessageType(self):
        return 14110

    def getMessageVersion(self):
        return self.messageVersion
