
import random

class Soldier():
    """A class to model basics behavior of a soldier"""

    def __init__(self, health, strength):
        """Initialize a soldier"""

        self.health = health
        self.strength = strength

    def attack(self):
        """A simple way to model an attack."""

        return self.strength

    def receiveDamage(self, damage):
        """A simple way to model an incoming attack."""

        self.health -= damage


class Viking(Soldier):
    """A class to model a Viking."""

    def __init__(self, name, health, strength):
        """Initialize the attributes of a viking"""
        self.name = name
        self.health = health
        self.strength = strength
       
        


def receiveDamage(self, damage):
    """Vikings receive damage differently"""

    if damage >= self.health:
        self.health = 0
        return f"{self.name} has died in act of combat"
    elif damage < self.health:
        self.health -= damage
        return f"{self.name} has received {damage} points of damage"


def battleCry(self):
    """A simple battle cry"""

    return "Odin owns you ALL!"


class Saxon(Soldier):
    """A class to model Saxons"""

    def __init__(self, health, strength):
        """Initialize the attributes of Saxons"""

        super().__init__(health, strength)

    def receiveDamage(self, damage):
        """Saxons receive damage like Coca receives Mentos"""

        if damage > self.health:
            self.health = 0
            return "A Saxon has died in combat"
        elif damage < self.health:
            self.health -= damage
            return f"A Saxon has received {damage} points of damage"


class War():

    def __init__(self):
        """Initialize the aspects of WAR!!"""
        self.VikingArmy = []
        self.SaxonArmy = []

    def addViking(self, Viking):
        """Adding one Viking to the Viking army"""

        
        self.VikingArmy.append(Viking)

    def addSaxon(self, Saxon):

        
        self.SaxonArmy.append(Saxon)

    def VikingAttack(self):
        """Modeling a Viking attack on a Saxon"""
        attacked_saxon = random.choice(self.SaxonArmy)
        attacking_viking = random.choice(self.VikingArmy)

        if attacking_viking.strength > attacked_saxon.health:
            self.SaxonArmy.remove(attacked_saxon)

        return attacked_saxon.receiveDamage(attacking_viking.attack())

    def SaxonAttack(self):
        """Modeling a Saxon attack on a Viking"""
        attacked_viking = random.choice(self.VikingArmy)
        attacking_saxon = random.choice(self.SaxonArmy)

        if attacking_saxon.strength > attacked_viking.health:
            self.VikingArmy.remove(attacked_viking)

        return attacked_viking.receiveDamage(attacking_saxon.attack())

    def showStatus(self):

        if not self.SaxonArmy:
            print("Vikings have won the war of the century!")

        if not self.VikingArmy:
            print("Saxons have fought for their lives and survived another day...")

        if self.SaxonArmy and self.VikingArmy:
            print("Vikings and Saxons are still in the thick of battle.")


#Hice una pequeña prueba y funciona :) 
x = War()
viking1 = Viking("queso", 100, 100)
x.addViking(viking1)

saxon1 = Saxon(20,20)
x.addSaxon(saxon1)

x.VikingAttack()
x.showStatus()

