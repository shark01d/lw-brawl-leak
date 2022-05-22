import time
import random
import json

from Classes.Packets.PiranhaMessage import PiranhaMessage


class OwnHomeDataMessage(PiranhaMessage):
    events = json.loads(open("Events.json", 'r').read())
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        
    def encode(self, fields, player):
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVInt(int(time.time()))
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(player.Trophies) # Trophies
        self.writeVInt(player.HighestTrophies + 50000) # Highest Trophies
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(player.TrophyRoadTier)
        self.writeVInt(player.Experience) # Experience
        self.writeDataReference(28, player.Thumbnail) # Thumbnail
        self.writeDataReference(43, player.Namecolor) # Namecolor

        self.writeVInt(0)

        self.writeVInt(1) # Selected Skins
        self.writeDataReference(29, player.SelectedSkin)
        print(player.SelectedSkin)

        self.writeVInt(0) # Randomizer Skin Selected

        self.writeVInt(0) # Current Random Skin

        self.writeVInt(len(ownedSkins))

        for skinID in ownedSkins:
            self.writeDataReference(29, skinID)

        self.writeVInt(0) # Unlocked Skin Purchase Option

        self.writeVInt(0) # New Item State

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeBoolean(True)
        self.writeVInt(player.TokensDoubler)
        self.writeVInt(5184000) # TrophyRoad Timer
        self.writeVInt(0) # PowerPlay Timer
        self.writeVInt(5184000) # Brawl Pass Timer

        self.writeVInt(141)
        self.writeVInt(135)

        self.writeVInt(5)

        self.writeVInt(93)
        self.writeVInt(206)
        self.writeVInt(456)
        self.writeVInt(792)
        self.writeVInt(729)

        self.writeBoolean(False) # Offer 1
        self.writeBoolean(False) # Offer 2
        self.writeBoolean(True) # Token Doubler Enabled
        self.writeVInt(2)  # Token Doubler New Tag State
        self.writeVInt(2)  # Event Tickets New Tag State
        self.writeVInt(2)  # Coin Packs New Tag State
        self.writeVInt(0)  # Change Name Cost
        self.writeVInt(0)  # Timer For the Next Name Change
 
        '''
        0: Free Box
        1: Coins
        2: Random Brawler
        3: Brawler
        4: Skin
        6: Brawl Box
        8: Power Points (For a specific brawler)
        9: Token Doubler
        10: Mega Box
        12: Power Points
        14: Big Box
        15: AdBox (Not working anymore)
        16: Gems
        17: Star Points
        19: Pin
        20: Set of Pins
        21: Pin Pack
        23: Pin of Rarity
        27: Pin Pack of Rarity
        30: New Brawer upgraded to level
        31: New Brawer of rarity upgraded to level
        32: Gear Tokens
        33: Gear Scrap
        '''

        shop = json.loads(open("Shop.json", 'r').read()) # import json
        
        self.writeVInt(len(shop)) # Offers count
    
        for shop in shop:
            self.writeVInt(1)  # RewardCount
            self.writeVInt(shop['ItemType'])  # ItemType
            self.writeVInt(shop['Amount']) # Amount
            self.writeDataReference(shop['CsvID1'], shop['CsvID2'])  # CsvID
            self.writeVInt(shop['ExtraID']) # ExtraID
            self.writeVInt(shop['Currency']) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
            self.writeVInt(shop['Cost']) #Cost
            self.writeVInt(shop['Time']) #Time
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(shop['Claim']) # Claim
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(shop['DailyOffer']) # Daily Offer
            self.writeVInt(shop['OriginalCost']) # Original Cost
            self.writeInt(0)
            self.writeString(shop['Text']) # Text
            self.writeBoolean(False)
            self.writeString(shop['Background']) # Background
            self.writeVInt(0)
            self.writeBoolean(shop['Processed']) # This purchase is already being processed
            self.writeVInt(shop['TypeBenefit']) # Type Benefit
            self.writeVInt(shop['Benefit']) # Benefit
            self.writeString()
            self.writeBoolean(shop['OneTimeOffer']) # One time offer
            self.writeBoolean(shop['Claimed']) # Claimed

        self.writeVInt(0)

        self.writeVInt(player.Tokens)
        self.writeVInt(-1)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(1)
        self.writeDataReference(16, player.SelectedBrawler)

        self.writeString(player.Region) # Location
        self.writeString(player.ContentCreator) # Content Creator

        self.writeVInt(19)
        self.writeLong(2, 1)  # Unknown
        self.writeLong(3, 0)  # TokensGained
        self.writeLong(4, 8)  # TrophiesGained
        self.writeLong(6, 0)  # DemoAccount
        self.writeLong(7, 0)  # InvitesBlocked
        self.writeLong(8, 0)  # StarPointsGained
        self.writeLong(9, 1)  # ShowStarPoints
        self.writeLong(10, 0)  # PowerPlayTrophiesGained
        self.writeLong(12, 1)  # Unknown
        self.writeLong(14, 0)  # CoinsGained
        self.writeLong(15, 0)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeLong(16, 0)
        self.writeLong(17, 0)  # TeamChatMuted
        self.writeLong(18, 1)  # EsportButton
        self.writeLong(19, 1)  # ChampionShipLivesBuyPopup
        self.writeLong(20, 0)  # GemsGained
        self.writeLong(21, 0)  # LookingForTeamState
        self.writeLong(22, 0)
        self.writeLong(24, 1)  # Have already watched club league stupid animation

        self.writeVInt(0)

        self.writeVInt(2)  # Brawl Pass
        for i in range(8, 10):
            self.writeVInt(i)
            self.writeVInt(player.bptokens)
            self.writeBoolean(True)
            self.writeVInt(0)

            self.writeByte(2)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)

            self.writeByte(1)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)

        self.writeVInt(0)

        quests = json.loads(open("Quests.json", 'r').read()) # import json
        self.writeBoolean(True) # LogicQuests
        self.writeVInt(len(quests)) # Quests Count
        for x in range(1):
        		for quests in quests:
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(quests['MissionType'])     # Mission Type
        			self.writeVInt(quests['AchievedGoal'])     # Achieved Goal
        			self.writeVInt(quests['QuestGoal'])     # Quest Goal
        			self.writeVInt(quests['TokensReward'])    # Tokens Reward
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(quests['CurrentLevel'])     # Current level
        			self.writeVInt(quests['MaxLevel'])     # Max level
        			self.writeVInt(quests['Timer'])     # Timer
        			self.writeInt8(quests['QuestState'])    # Quest State
        			self.writeDataReference(16, quests['BrawlerID']) # Brawler(16, <BrawlerID>)
        			self.writeVInt(quests['GameMode'])     # GameMode
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(2)     # Unknown

        self.writeBoolean(True)
        self.writeVInt(ownedPinsCount + ownedThumbnailCount)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        self.writeBoolean(True) # Power League Array
        # Power League Data Array Start #
        self.writeVInt(3) # Season
        self.writeVInt(player.power_rank) # Rank Solo League
        self.writeVInt(3) # Season
        self.writeVInt(player.power_rank) # Rank Team League
        self.writeVInt(1) # ?
        self.writeVInt(player.power_rank) # Max Rank Solo
        self.writeVInt(player.power_rank) # Max Rank Team
        self.writeVInt(1) # ?
        self.writeVInt(1) # ?
        self.writeVInt(player.match_played) # Played Game League
        self.writeVInt(0)
        self.writeVInt(0)
        # Power League Data Array End #

        self.writeInt(0)

        self.writeVInt(0)

        self.writeVInt(25) # Count

        # Event Slots IDs Array Start #
        self.writeVInt(1) # Gem Grab
        self.writeVInt(2) # Showdown
        self.writeVInt(3) # Daily Events
        self.writeVInt(4) # Team Events
        self.writeVInt(5) # Duo Showndown
        self.writeVInt(6) # Team Events 2
        self.writeVInt(7) # Special Events(Big Game and other…)
        self.writeVInt(8) # Solo Events (As well as Seasonal Events)
        self.writeVInt(9) # Power Play (Not working)
        self.writeVInt(10) # Seasonal Events
        self.writeVInt(11) # Seasonal Events 2
        self.writeVInt(12) # Candidates of The Day
        self.writeVInt(13) # Winner of The Day
        self.writeVInt(14) # Solo Mode Power League
        self.writeVInt(15) # Team Mode Power League
        self.writeVInt(16) # Club League(Default Map)
        self.writeVInt(17) # Club League(Power Match)
        self.writeVInt(20) # Championship Challenge (Stage 1)
        self.writeVInt(21) # Championship Challenge (Stage 2)
        self.writeVInt(22) # Championship Challenge (Stage 3)
        self.writeVInt(23) # Championship Challenge (Stage 4)
        self.writeVInt(24) # Championship Challenge (Stage 5)
        self.writeVInt(30) # Team Events 3?
        self.writeVInt(31) # Team Events 4?
        self.writeVInt(32) # Team Events 5?
        # Event Slots IDs Array End #

        events = json.loads(open("Events.json", 'r').read()) # import json
        
        self.writeVInt(len(events) + 7) # Events Count(7 it a ChampionShip(3 Stages) and ClubLeague(PowerMatch and Default Game Mode)) and PowerLeague(Solo and Team Mode)
        for event in events:
              # Default Slots Start Array #
              self.writeVInt(0)
              self.writeVInt(events.index(event) + 1)  # EventType
              self.writeVInt(event['CountdownTimer'])  # EventsBeginCountdown
              self.writeVInt(event['Timer'])  # Timer
              self.writeVInt(event['Tokens'])  # Tokens
              self.writeDataReference(15, event['ID'])  # MapID
              self.writeVInt(-64)  # GameModeVariation
              self.writeVInt(event['Status'])  # Status
              self.writeString()
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeVInt(0)
              if event['Modifier'] > 0:
                 self.writeBoolean(True)
                 self.writeVInt(event['Modifier']) # Modifer ID
              else:
                 self.writeBoolean(False)
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeBoolean(False)  # Map Maker Map Structure Array
              self.writeVInt(0)
              self.writeBoolean(False)  # Power League Data Array
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeBoolean(False)  # ChronosTextEntry
              self.writeBoolean(False)
              self.writeBoolean(False)
              self.writeVInt(-1)
              self.writeBoolean(False)
              self.writeBoolean(False)
              # Default Slots End Array #

        # Championship Challenge Slot Start Array #
        # Championship Challenge Stage 1 #
        self.writeVInt(0)
        self.writeVInt(20)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(5184000)  # Timer
        self.writeVInt(0)  # Tokens
        self.writeDataReference(15, 9)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() # ?
        self.writeVInt(0) # ?
        self.writeVInt(0) # Defeates?
        self.writeVInt(3) # Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) # Wins
        self.writeVInt(0) # ???(Dont Change!)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) # Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) # Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)# ???
        self.writeBoolean(False) #???
        self.writeVInt(-1)
        self.writeBoolean(False) # ???
        self.writeBoolean(False) # ???
        
        # Championship Challenge Stage 2 #   
        self.writeVInt(0)
        self.writeVInt(21)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(5184000)  # Timer
        self.writeVInt(0)  # Tokens
        self.writeDataReference(15, 1)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) # Wins
        self.writeVInt(0) # ???(Dont Change!)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) # Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) # Total Wins
        self.writeVInt(3) # ?
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False) # ???
        self.writeBoolean(False) # ???
        self.writeVInt(-1)
        self.writeBoolean(False) # ???
        self.writeBoolean(False) # ???
        
        # Championship Challenge Stage 3 #   
        self.writeVInt(0)
        self.writeVInt(22)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(5184000)  # Timer
        self.writeVInt(0)  # Tokens
        self.writeDataReference(15, 228)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() # ?
        self.writeVInt(0) # ?
        self.writeVInt(0) # Defeates?
        self.writeVInt(3) # Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) # Wins
        self.writeVInt(0) # ???(Dont Change!)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) # Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) # Total Wins
        self.writeVInt(3) # ?
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False) # ???
        self.writeBoolean(False) # ???
        self.writeVInt(-1)
        self.writeBoolean(False) # ???
        self.writeBoolean(False) # ???
        
        # Championship Slots End Array #
        
        # Club League Slots Start Array #
        # Club League Default Map Array #
        self.writeVInt(0)
        self.writeVInt(16)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(86400)  # Timer
        self.writeVInt(0)  # Tokens
        self.writeDataReference(15, 10)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # ChronosTextEntry
        self.writeVInt(-64)
        self.writeBoolean(False)

        # Power Match Array #
        self.writeVInt(0)
        self.writeVInt(17)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(86400)  # Timer
        self.writeVInt(0)  # Tokens
        self.writeDataReference(15, 295)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # ChronosTextEntry
        self.writeVInt(-64)
        self.writeBoolean(False)
        # Club League Slots End Array #
        
        # Power League Solo Mode #
        self.writeVInt(0)
        self.writeVInt(14)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(5184000)  # Timer
        self.writeVInt(0)  # Tokens
        self.writeDataReference(0, 4)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(6) # Season
        self.writeString("TID_BRAWL_PASS_SEASON_9") # Name Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3) # Quests Count
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(30) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(78) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(79) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(60) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(436) # SkinID
        
        self.writeVInt(19) # Road Count
        
        self.writeVInt(1) # Rank
        self.writeVInt(500) # Starpoints
        self.writeVInt(2) # Rank
        self.writeVInt(1000) # Starpoints
        self.writeVInt(3)  # Rank
        self.writeVInt(2000) # Starpoints
        self.writeVInt(4)  # Rank
        self.writeVInt(2500) # Starpoints
        self.writeVInt(5)  # Rank
        self.writeVInt(3000) # Starpoints
        self.writeVInt(6)  # Rank
        self.writeVInt(3750) # Starpoints
        self.writeVInt(7)  # Rank
        self.writeVInt(4500) # Starpoints
        self.writeVInt(8)  # Rank
        self.writeVInt(5500) # Starpoints
        self.writeVInt(9)  # Rank
        self.writeVInt(7000) # Starpoints
        self.writeVInt(10)  # Rank
        self.writeVInt(8750) # Starpoints
        self.writeVInt(11)  # Rank
        self.writeVInt(10000) # Starpoints
        self.writeVInt(12)  # Rank
        self.writeVInt(12500) # Starpoints
        self.writeVInt(13)  # Rank
        self.writeVInt(15000) # Starpoints
        self.writeVInt(14)  # Rank
        self.writeVInt(17500) # Starpoints
        self.writeVInt(15)  # Rank
        self.writeVInt(20000) # Starpoints
        self.writeVInt(16)  # Rank
        self.writeVInt(25000) # Starpoints
        self.writeVInt(17)  # Rank
        self.writeVInt(30000) # Starpoints
        self.writeVInt(18)  # Rank
        self.writeVInt(40000) # Starpoints
        self.writeVInt(19)  # Rank
        self.writeVInt(50000) # Starpoints
    
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Power League Team Mode #
        self.writeVInt(0)
        self.writeVInt(15)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(5184000)  # Timer
        self.writeVInt(0)  # Tokens
        self.writeDataReference(0, 4)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(6) # Season
        self.writeString("TID_BRAWL_PASS_SEASON_9") # Name Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3) # Quests Count
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(30) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(78) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(79) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(60) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(436) # SkinID
        
        self.writeVInt(19) # Road Count
        
        self.writeVInt(1) # Rank
        self.writeVInt(500) # Starpoints
        self.writeVInt(2) # Rank
        self.writeVInt(1000) # Starpoints
        self.writeVInt(3)  # Rank
        self.writeVInt(2000) # Starpoints
        self.writeVInt(4)  # Rank
        self.writeVInt(2500) # Starpoints
        self.writeVInt(5)  # Rank
        self.writeVInt(3000) # Starpoints
        self.writeVInt(6)  # Rank
        self.writeVInt(3750) # Starpoints
        self.writeVInt(7)  # Rank
        self.writeVInt(4500) # Starpoints
        self.writeVInt(8)  # Rank
        self.writeVInt(5500) # Starpoints
        self.writeVInt(9)  # Rank
        self.writeVInt(7000) # Starpoints
        self.writeVInt(10)  # Rank
        self.writeVInt(8750) # Starpoints
        self.writeVInt(11)  # Rank
        self.writeVInt(10000) # Starpoints
        self.writeVInt(12)  # Rank
        self.writeVInt(12500) # Starpoints
        self.writeVInt(13)  # Rank
        self.writeVInt(15000) # Starpoints
        self.writeVInt(14)  # Rank
        self.writeVInt(17500) # Starpoints
        self.writeVInt(15)  # Rank
        self.writeVInt(20000) # Starpoints
        self.writeVInt(16)  # Rank
        self.writeVInt(25000) # Starpoints
        self.writeVInt(17)  # Rank
        self.writeVInt(30000) # Starpoints
        self.writeVInt(18)  # Rank
        self.writeVInt(40000) # Starpoints
        self.writeVInt(19)  # Rank
        self.writeVInt(50000) # Starpoints
        
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0) # Comming Events

        self.writeVInt(10)  # Brawler Upgrade Cost
        self.writeVInt(20) # 2 Level
        self.writeVInt(35) # 3 Level
        self.writeVInt(75) # 4 Level
        self.writeVInt(140) # 5 Level
        self.writeVInt(290) # 6 Level
        self.writeVInt(480) # 7 Level
        self.writeVInt(800) # 8 Level
        self.writeVInt(1250) # 9 Level
        self.writeVInt(1875) # 10 Level
        self.writeVInt(2800) # 11 Level

        self.writeVInt(4)  # Shop Coins Price
        self.writeVInt(20)
        self.writeVInt(50)
        self.writeVInt(140)
        self.writeVInt(280)

        self.writeVInt(4)  # Shop Coins Count
        self.writeVInt(150) # Count
        self.writeVInt(400) # Count
        self.writeVInt(1200) # Count
        self.writeVInt(2600) # Count

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVInt(0)

        self.writeVInt(23)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000038)  # ThemeID (0-Default, 35-Brawlidays_2021, 36-Brawlidays_2021_snow, 37-Brawlentines, 38-LNY22)
        self.writeLong(60, 36270)
        self.writeLong(66, 1)
        self.writeLong(61, 36270)  # SupportDisabled State
        self.writeLong(47, 41381)
        self.writeLong(29, 12)  # Skin Group
        self.writeLong(48, 41381)
        self.writeLong(50, 0)
        self.writeLong(1100, 500)
        self.writeLong(1101, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 1)  # DoubleTokenEvent
        self.writeLong(31, 1)  # GoldRushEvent
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(17, 4)
        self.writeLong(10046, 1)

        self.writeVInt(0) # Timed Int Value Entry

        self.writeVInt(0)  # Custom Event

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeLong(player.ID[0], player.ID[1])  # PlayerID

        self.writeVInt(1) # NotificationFactory

        self.writeVInt(83) # NotifìcationID
        self.writeInt(0)
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeString("F1ash")
        self.writeInt(0)
        self.writeString("Добро пожаловать в LW Brawl") # Title

        self.writeInt(0)
        self.writeString("Ты знал что у нас есть свой Telegram Канал а также веселый чат") # Subtitle

        self.writeInt(0)
        self.writeString("TELEGRAM") # Button Text 

        self.writeString("/36042168-49af-4e79-b5f3-13c8c279bc5c_brawltalkpopup.png") # ImageUrl
        self.writeString('28d8d5533ddecebf766daac49f3290415a36fa42')

        self.writeString("brawlstars://extlink?page=https%3A%2F%2Ft.me%2Flwbrawl") # RedirectLink
        self.writeVInt(0)
        

        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString(player.Name) # Player Name
        self.writeBoolean(player.Registered) # Registered

        self.writeInt(0)

        self.writeVInt(15)

        self.writeVInt(3 + ownedBrawlersCount)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(player.Coins) 

        self.writeDataReference(5, 10)
        self.writeVInt(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVInt(player.ClubCoins)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["Trophies"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["HighestTrophies"])

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["PowerPoints"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["PowerLevel"] - 1)

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["State"])

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(player.Gems)  # Diamonds
        self.writeVInt(player.Gems)  # Free Diamonds
        self.writeVInt(player.Level)  # Player Level
        self.writeVInt(100)
        self.writeVInt(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(1)  # Battle Count
        self.writeVInt(0)  # WinCount
        self.writeVInt(0)  # LoseCount
        self.writeVInt(0)  # WinLooseStreak
        self.writeVInt(0)  # NpcWinCount
        self.writeVInt(0)  # NpcLoseCount
        self.writeVInt(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(0)

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion