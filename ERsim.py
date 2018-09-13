#  File: ERsim.py
#  Description: simulation of ER with patients being added and treated in queues according to severity of condition 
#  Student's Name: Hailey Cassidy
#  Student's UT EID: HAC787
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 10/14/17
#  Date Last Modified: 10/19/17

class Queue (object):
   def __init__(self):
      self.items = [ ]

   def __str__(self):
      return str(self.items)

   def isEmpty (self):
      return self.items == [ ]

   def enqueue (self, item):
      self.items.append(item)

   def dequeue (self):
      return self.items.pop(0)

   def peek (self):
      return self.items[0]

   def size (self):
      return len(self.items)
    
#################################

# creating the three queues
critical = Queue()
serious = Queue()
fair = Queue()

def addPatient(condition, name):

    # adds patient to stated queue
    if condition == "Critical":
        critical.enqueue(name)
    elif condition == "Serious":
        serious.enqueue(name)
    elif condition == "Fair":
        fair.enqueue(name)

    #output of queues after patient is added
    print("\tQueues are:")
    print("\tFair:", fair)
    print("\tSerious:", serious)
    print("\tCritical:", critical)
    

def treatNext():

    # if there is a critical patient they should be treated
    if critical.isEmpty() == False:
        print("\tTreating", critical.peek(), "from Critical queue")
        critical.dequeue()
        print("\tQueues are:")
        print("\tFair:", fair)
        print("\tSerious:", serious)
        print("\tCritical:", critical)

    # if there are no critical patients a serious patient should be treated 
    elif serious.isEmpty() == False:
        print("\tTreating", serious.peek(), "from Serious queue")
        serious.dequeue()
        print("\tQueues are:")
        print("\tFair:", fair)
        print("\tSerious:", serious)
        print("\tCritical:", critical)

    # if there are no serious or critical patients a fair patient should be treated       
    elif fair.isEmpty() == False:
        print("\tTreating", fair.peek(), "from Fair queue")
        fair.dequeue()
        print("\tQueues are:")
        print("\tFair:", fair)
        print("\tSerious:", serious)
        print("\tCritical:", critical)
        
    # there aren't patients in any queues       
    else:
        print("No patients in queues")
        

def treatCondition(condition):

    # treats patient from stated queue
    if condition == "Critical":
        print("\tTreating", critical.peek(), "from Critical queue")
        critical.dequeue()
        
    elif condition == "Serious":
        print("\tTreating", serious.peek(), "from Serious queue")
        serious.dequeue()
        
    elif condition == "Fair":
        print("\tTreating", fair.peek(), "from Fair queue")
        fair.dequeue()

    # output of queue after patient is treated 
    print("\tQueues are:")
    print("\tFair:", fair)
    print("\tSerious:", serious)
    print("\tCritical:", critical, "\n")
        

def treatAll():

    # as long as there are critical patients keep treating them
    while critical.isEmpty() == False:
        treatCondition("Critical")

    # after all critical patients are treated move on to serious patients
    while serious.isEmpty() == False:
        treatCondition("Serious")

    # after all serious patients are treated move on to fair patients
    while fair.isEmpty() == False:
        treatCondition("Fair")
        


def main():

    f = open("ERsim.txt", "r")# opens text file for reading 
    line = f.readline() # reads a line
    
    while line != "": # as long as line isn't ""
        commandList = line.split() # gives list of words in line with breaks between " "
        
        if commandList[0] == "add": # add patient
            print("\nCommand: Add patient", commandList[2], "to", commandList[1], "queue\n")
            addPatient(commandList[1], commandList[2])
            
        elif commandList[0] == "treat":
            if commandList[1] == "next": #treat next 
                print("\nCommand: Treat next patient\n")
                treatNext()
            elif commandList[1] == "all": # treat all
                print("\nCommand: Treat all patients\n")
                treatAll()
            else: # treat condition 
                print("\nCommand: Treat next patient on", commandList[1], "queue\n")
                treatCondition(commandList[1])
                
        elif commandList[0] == "exit": # exit program 
            print("\nCommand: Exit\n")
            break
         
        else: # not a valid command given 
            print("\nInvalid command\n")
            
        line = f.readline() # moves on to reading the next line
        
    
main()
        
    
