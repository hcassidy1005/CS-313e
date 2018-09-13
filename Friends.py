#  File: Friends.py
#  Description: program that tracks friends using text based input
#  Student's Name: Hailey Cassidy
#  Student's UT EID: HAC787
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 11/7/17
#  Date Last Modified:11/10/17

###################################
class Node (object):
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            # always do this â€“ saves a lot
                                  # of headaches later!
   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER

###################################
class linkedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        output = "[ "
        while current != None:
            output = output + str(current.getData()) + " "
            current = current.getNext()
        output += "]"
        return output

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def find(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def delete(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current == None:
            return False
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return True

    def isEmpty(self):
        return self.head == None

###################################           

class User:
    

    def __init__(self, name): 
        self.name = name
        self.friendList = linkedList()
        print("   ", name, "now has an account.")

    def getName(self):
        return self.name

    def addFriend(self, friend, userList):
        if self.friendList.find(friend):
            print("   ", self.name, "and", friend, "are already friends.")
        else:
            self.friendList.add(friend)
            getUser(userList, friend).friendList.add(self.name)
            print("   ", self.name, "and", friend, "are now friends.")

    def deleteFriend(self, friend, userList):
        if self.friendList.find(friend):
            self.friendList.delete(friend)
            getUser(userList, friend).friendList.delete(self.name)
            print("   ", self.name, "and", friend, "are no longer friends.")
        else:
            print("   ", self.name, "and", friend, "aren't friends, so you can't unfriend them.")

    def listAllFriends(self):

        if self.friendList.isEmpty():
            print("   ", self.name, "has no friends.")
        else:
            print("   ", self.friendList)

    def queryFriendStatus(self, friend):

        if self.friendList.find(friend): 
            print("   ", self.name, "and", friend, "are friends.")
        else:
            print("   ", self.name, "and", friend, "are not friends.")

    def exitProgram (self):
        print("    Exiting...")
        
###################################

def getUser(alist, item):
    current = alist.head
    
    while current != None:
        if current.getData().getName() == item:
            return current.getData()
        else:
            current = current.getNext()
    return None
    
def main ():
    userList = linkedList()
    f = open("FriendData.txt", "r")# opens text file for reading 
    line = f.readline() # reads a line
    
    while line != "": # as long as line isn't ""
        commandList = line.split() # gives list of words in line with breaks between " "
        
        if commandList[0] == "Person": # add account
            print("\n--> Person", commandList[1])
            if getUser(userList, commandList[1]) != None:
                print("    A person with name", commandList[1], "already exists.")
            else:
                newUser = User(commandList[1])
                userList.add(newUser) 
            
        elif commandList[0] == "List": # list friends
            print("\n--> List", commandList[1])
            if getUser(userList, commandList[1]) != None:
                getUser(userList, commandList[1]).listAllFriends() 
            else:
                print("    A person with name", commandList[1], "does not currently exist.")

        elif commandList[0] == "Friend": # add friend
            print("\n--> Friend", commandList[1], commandList[2])
            if commandList[1] == commandList[2]:
                print("    A person cannot friend him/herself.")
            elif getUser(userList, commandList[1]) != None and getUser(userList, commandList[2]) != None:
                getUser(userList, commandList[1]).addFriend(commandList[2], userList)
            
            else:
                if getUser(userList, commandList[1]) == None:
                    print("    A person with name", commandList[1], "does not currently exist.")
                if getUser(userList, commandList[2]) == None:
                    print("    A person with name", commandList[2], "does not currently exist.")
            
        elif commandList[0] == "Unfriend": # delete friend
            print("\n--> Unfriend", commandList[1], commandList[2])
            if commandList[1] == commandList[2]:
                print("    A person cannot unfriend him/herself.")
            elif getUser(userList, commandList[1]) != None and getUser(userList, commandList[2]) != None:
                getUser(userList, commandList[1]).deleteFriend(commandList[2], userList)
            else:
                if getUser(userList, commandList[1]) == None:
                    print("    A person with name", commandList[1], "does not currently exist.")
                if getUser(userList, commandList[2]) == None:
                    print("    A person with name", commandList[2], "does not currently exist.")
             
            
        elif commandList[0] == "Query": # query friend 
            print("\n--> Query", commandList[1], commandList[2])
            if commandList[1] == commandList[2]:
                print("    A person cannot query him/herself.")
            elif getUser(userList, commandList[1]) != None and getUser(userList, commandList[2]) != None:
                getUser(userList, commandList[1]).queryFriendStatus(commandList[2])  
            else:
                if getUser(userList, commandList[1]) == None:
                    print("    A person with name", commandList[1], "does not currently exist.")
                if getUser(userList, commandList[2]) == None:
                    print("    A person with name", commandList[2], "does not currently exist.")
            
            
                
        elif commandList[0] == "Exit": # exit program 
            print("\n--> Exit")
            newUser.exitProgram() # need to fix 
            break
         
        else: # not a valid command given 
            print("\nInvalid command\n")
            
        line = f.readline() # moves on to reading the next line

main()
    

    
