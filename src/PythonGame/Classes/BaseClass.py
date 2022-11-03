class Base:
    def __init__(self,atk,armor,spd,luck,hp):
        self.atk = 10
        self.armor = 10
        self.spd = 10
        self.luck = 10
        self.hp = 100
    
    def getAtk(self):
        return self.atk
    
    def getArmor(self):
        return self.armor
    
    def getSpd(self):
        return self.spd
    
    def getLuck(self):
        return self.luck
    
    def getHp(self):
        return self.hp
    
    def setAtk(self,newAtk):
        self.atk = newAtk
        
    def setArmor(self,newArmor):
        self.armor = newArmor
        
    def setSpd(self,newSpd):
        self.spd = newSpd
        
    def setLuck(self,newLuck):
        self.luck = newLuck
        
    def setHp(self,newHp):
        self.hp = newHp
        
    def attack(self):
        pass

        
    