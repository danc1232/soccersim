__author__ = 'DanielCasey'
import random
import time

class Team:
    def __init__(self,name):
        self.name = name
        self.players = Offense(),Offense(),Offense(),Defense(),Defense(),Defense(),Goalie()
        self.offense = []
        self.defense = []
        self.goalie = []
        self.addOff()
        self.addDef()
        self.addGtd()

    def addOff(self):
        for i in self.players:
            if i.pos == 1:
                self.offense.append(i)

    def addDef(self):
        for i in self.players:
            if i.pos == 2:
                self.defense.append(i)

    def addGtd(self):
        for i in self.players:
            if i.pos == 3:
                self.goalie.append(i)

    def announceNames(self):
        for i in self.players:
            print(i.name)

    def lineUp(self):
        print(self.name+'\n'+"------------------------")
        for i in self.players:
            if i.pos == 1:
                print(i.name+" -- Offense"+"\n"+"Speed : "+str(i.speed)+" Dexterity : "+str(i.dex)+" Strength : "+str(i.str)+"\n")
            elif i.pos == 2:
                print(i.name+" -- Defense"+"\n"+"Speed : "+str(i.speed)+" Dexterity : "+str(i.dex)+" Strength : "+str(i.str)+"\n")
            else:
                print(i.name+" -- Goalie"+"\n"+"Speed : "+str(i.speed)+" Dexterity : "+str(i.dex)+" Strength : "+str(i.str)+"\n")


class Player:
    def __init__(self):
        self.speed = random.randrange(25,100)
        self.dex = random.randrange(25,100)
        self.str = random.randrange(25,100)
        self.name = random.choice(("Daniel","Brett","Mark","Tyler","Nick"))


class Offense(Player):
    def __init__(self):
        Player.__init__(self)
        self.pos = 1

    def shoot(self):
        kick = self.dex + self.str
        if kick >= random.randrange(50,201):
            return 1
        else:
            return 0

    def passBall(self):
        passAtt = self.dex + self.str
        check = random.randrange(50,201)
        if check <= passAtt:
            att = 1 ##pass advances one step
        else:
            att = 0 ##pass is unsuccessful

        keepBallCheck = random.randrange(25,101)
        if self.dex <= keepBallCheck:
            pos = 0 ##possession is retained
        else:
            pos = 1 ##pass is intercepted

        return(att,pos)


class Defense(Player):
    def __init__(self):
        Player.__init__(self)
        self.pos = 2

    def passBall(self):
        passAtt = self.dex + self.str
        check = random.randrange(50,201)
        if check <= passAtt:
            att = 1 ##pass advances one step
        else:
            att = 0 ##pass is unsuccessful

        keepBallCheck = random.randrange(25,101)
        if self.dex <= keepBallCheck:
            pos = 0 ##possession is retained
        else:
            pos = 1 ##pass is intercepted

        return(att,pos)


class Goalie(Player):
    def __init__(self):
        Player.__init__(self)
        self.pos = 3

    def goalKick(self):
        kick = self.dex + self.str
        if kick >= 160:
            return 3
        elif 160 >> kick >= 80:
            return 2
        else:
            return 1


class Game:
    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2
        self.ball = 0  ## if ball == 1, team 1 has possession
        self.field = 3 ##field is split into 5 zones, (1|2|3|4|5), 3 is midfield, 1 is closest to team 1 goal, 5 is closest to team2 goal
        self.score1 = 0
        self.score2 = 0
        self.play()

    def action(self):
        if self.ball == 1:
            if self.field == 1:
                gtd = self.team1.goalie[0]
                self.field = self.field + gtd.goalKick()
                pCheck = random.randrange(1,11) ##possession check, see passBall(), similar
                if pCheck <= 7:
                    self.ball = 1
                else:
                    self.ball = 2
            elif self.field == 2:
                df = self.team1.defense[random.randrange(0,3)]
                att,pos = df.passBall()
                if att == 1:
                    self.field += 1
                else:
                    pass
                if pos == 1:
                    self.ball = 2
                else:
                    pass
            elif self.field == 3:
                df = self.team1.defense[random.randrange(0,3)]
                att,pos = df.passBall()
                if att == 1:
                    self.field += 1
                else:
                    pass
                if pos == 1:
                    self.ball = 2
                else:
                    pass
            elif self.field == 4:
                off = self.team1.offense[random.randrange(0,3)]
                if random.randrange(25,101) <= off.speed: ##check to see if player can just run to goal range
                    self.field = 5
                else:
                    att,pos = off.passBall()
                    if att == 1:
                        self.field += 1
                    else:
                        pass
                    if pos == 1:
                        self.ball = 2
                    else:
                        pass
            else:
                off = self.team1.offense[random.randrange(0,3)]
                shotOnGoal = off.shoot()
                if shotOnGoal == 1:
                    self.score1 += 1
                    print(self.team1.name,"have scored!")
                    print(self.score1,self.score2)
                else:
                    self.ball = 2

        elif self.ball == 2:
            if self.field == 5:
                gtd = self.team2.goalie[0]
                self.field = self.field - gtd.goalKick()
                pCheck = random.randrange(1,11)
                if pCheck <= 7:
                    pass
                else:
                    self.ball = 1

            elif self.field == 4:
                df = self.team2.defense[random.randrange(0,3)]
                att,pos = df.passBall()
                if att == 1:
                    self.field -= 1
                else:
                    pass
                if pos == 1:
                    self.ball = 1
                else:
                    pass

            elif self.field == 3:
                df = self.team2.defense[random.randrange(0,3)]
                att,pos = df.passBall()
                if att == 1:
                    self.field -= 1
                else:
                    pass
                if pos == 1:
                    self.ball = 1
                else:
                    pass

            elif self.field == 2:
                off = self.team2.offense[random.randrange(0,3)]
                if random.randrange(25,101) <= off.speed: ##check to see if player can just run to goal range
                    self.field = 1
                else:
                    att,pos = off.passBall()
                    if att == 1:
                        self.field -= 1
                    else:
                        pass
                    if pos == 1:
                        self.ball = 1
                    else:
                        pass
            else:
                off = self.team2.offense[random.randrange(0,3)]
                shotOnGoal = off.shoot()
                if shotOnGoal == 1:
                    self.score2 += 1
                    print(self.team2.name,"have scored!")
                    print(self.score1,self.score2)
                else:
                    self.ball = 1



    def play(self):
        self.ball = random.choice((1,2))
        clock = 90
        while clock >> 0:
            self.action()
            time.sleep(random.randint(1,4))
            if self.ball == 1:
                if self.field == 1:
                    ball = "at their own goal."
                elif self.field == 2:
                    ball = "at their end of the field."
                elif self.field == 3:
                    ball = "at midfield."
                elif self.field == 4:
                    ball = "at their opponent's end of the field."
                else:
                    ball = "approaching the opponent's goal."
                print(self.team1.name,"have the ball",ball)
            if self.ball == 2:
                if self.field == 5:
                    ball = "at their own goal."
                elif self.field == 4:
                    ball = "at their end of the field."
                elif self.field == 3:
                    ball = "at midfield."
                elif self.field == 2:
                    ball = "at their opponent's end of the field."
                else:
                    ball = "approaching the opponent's goal."
                print(self.team2.name,"have the ball",ball)
            clock -= 1

        print("game over")
        print("Final Score : " + self.team1.name + " : " + str(self.score1) + " -- " + self.team2.name + " : " + str(self.score2))

        dexcheck1 = 0
        strcheck1 = 0
        specheck1 = 0
        dexcheck2 = 0
        strcheck2 = 0
        specheck2 = 0

        for player in self.team1.players:
            dexcheck1 += player.dex
            strcheck1 += player.str
            specheck1 += player.speed

        for player in self.team2.players:
            dexcheck2 += player.dex
            strcheck2 += player.str
            specheck2 += player.speed

        print(dexcheck1,strcheck1,specheck1)
        print(dexcheck2,strcheck2,specheck2)


team1 = Team("Team 1")
team1.lineUp()
team2 = Team("Team 2")
team2.lineUp()

game = Game(team1,team2)

