#  File: RPG.py
#  Description: Game where wizards and fighters battle to the death!
#  Student's Name: Hailey Cassidy
#  Student's UT EID: HAC787
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 9/15/17
#  Date Last Modified:9/22/17

class Weapon:
    
    def __init__(self, weaponType):
        self.type = weaponType
        if self.type == "dagger":
            damage = 4
        elif self.type == "axe":
            damage = 6
        elif self.type == "staff":
            damage = 6
        elif self.type == "sword":
            damage = 10
        else:
            self.type == "none"
            damage = 1
            
    def __str__(self):
        return str(self.type)
            
        
class Armor:
    
    def __init__(self, armorType):
        self.type = armorType
        armorClass = 10
        if self.type == "plate":
            armorClass = 2
        elif self.type == "chain":
            armorClass = 5
        elif self.type == "leather":
            armorClass = 8
        else:
            self.type == "none"
            armorClass = 10
            
    def armorClass(self):
        return str(self.armorClass)

    def __str__(self):
        return str(self.type)
            
        
class RPGCharacter:
    
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return "\n" + self.name + "\n" + "   Current Health: " + str(self.health) + "\n" + "   Current Spell Points: " + str(self.spell) + "\n" + "   Wielding: " + str(self.Weapon) + "\n" + "   Wearing: " + str(self.Armor) + "\n" + "   Armor class: " + self.Armor.armorClass() + "\n" 
            
    def checkForDefeat(self):
        if self.health <= 0:
            return 1
        else:
            return 0
        
    def wield(self, weapon):
        self.Weapon = Weapon(weapon)
        print(self.name, "is now weilding a(n)", self.Weapon)

    def fight(self,other):
        other.health -= self.Weapon.damage()
        
        print(self.name, "attacks", other.name, "with a(n)", self.Weapon)
        print(self.name, "does", self.Weapon.damage, "damage to", other.name)
        print(other.name, "is now down to", other.health, "health")
        
        #checking defeat
        if other.checkForDefeat() == 1:
            print(other.name, "has been defeated!")

    def unwield(self):
        self.Weapon = Weapon("none")
        print(self.name, "is no longer wielding anything.")

    def putOnArmor(self, armor):
        self.Armor = Armor(armor)
        print(self.name, "is now wearing", self.Armor)

    def takeOffArmor(self):
        self.Armor = Armor("none")
        print(self.name, "is no longer wearing anything.")
    
        

class Fighter (RPGCharacter):
    
    def __init__(self,name):
        self.name = name
        self.health = 40
        self.spell = 0


class Wizard (RPGCharacter):
    
    def __init__(self,name):
        self.name = name
        self.health = 16
        self.spell = 20
        self.Armor = Armor("none")

    #overrides RPGCharacter wield and specifies it for wizard
    def wield(self, weapon):
        self.Weapon = Weapon(weapon)
    
        #check to see if its a valid weapon for wizard
        setWeapon = set(str(self.Weapon).split(' '))
        setAxe = set(("axe").split(' '))
        setSword = set(("sword").split(' '))
        if setWeapon == setAxe or setWeapon == setSword:
            print("Weapon not allowed for this character class.")
        else:
            print(self.name, "is now weilding a(n)", self.Weapon)

    #overrides RPGCharacter putOnArmor and specifies it for wizard
    def putOnArmor(self, armor):
        print(self.name, "cannot wear armor because he/she is a wizard.")

    def castSpell(self, spellType, other):
        self.spellType = spellType
        print(self.name, "cast", self.spellType, "at", other.name)

        #making strings of spell types
        fireball = "Fireball"
        lightning = "Lightning Bolt"
        heal = "Heal"

        #convering strings to sets 
        setSpell = set(str(self.spellType).split(' '))
        setFireball = set(fireball.split(' '))
        setLightning = set(lightning.split(' '))
        setHeal = set(heal.split(' '))

        #comparing sets and casting chosen spell
        if setSpell == setFireball:
            self.spell -= 3
            damage = 5
            other.health -= damage
            print(self.name, "does", damage, "damage to", other.name)
            print(other.name, "is now down to", other.health, "health")
        elif setSpell == setLightning:
            self.spell -= 10
            damage = 10
            other.health -= damage
            print(self.name, "does", damage, "damage to", other.name)
            print(other.name, "is now down to", other.health, "health")
        elif setSpell == setHeal:
            self.spell -= 6
            other.health += 6
            print(self.name, "heals", other.name, "for 6 health points.")
            print(other.name, "is now at", other.health, "health") 
        else:
            print ("Unknown spell name. Spell failed")

        #checking for defeat
        if other.checkForDefeat() == 1:
                print(other.name, "has been defeated!")



def main():

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)

    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)


main()
