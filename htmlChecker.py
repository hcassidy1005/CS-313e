#  File: htmlChecker.py
#  Description: checks to see if the html tags are valid and matched up 
#  Student's Name: Hailey Cassidy
#  Student's UT EID: HAC787
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 10/09/2017
#  Date Last Modified:10/13/2017

#previously defined Stack class 
class Stack (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items[-1]

   def size (self):
      return len(self.items)

##################################################
def htmlChecker (tagList):
    
    s = Stack()
    balanced = True
    index = 0
    VALIDTAGS = []
    EXCEPTIONS = ["meta", "br","hr"]

    print("Checking the tags:", tagList)

    while index < len(tagList) and balanced:

        tag = tagList[index]

        if tag in EXCEPTIONS: # if the tag is an exception 
            print("The tag", tag, "is an exception and is not added to the stack")
            print("The stack is:", str(s))
            
        elif tag.find("/") != -1: #adds starting tag to the stack
            s.push (tag)
            print("The tag", tag, "was pushed on to the stack")
            print("The stack is now:", str(s))
            
        else:
            if s.isEmpty(): # nothing present in the stack
               print("Error: Nothing in stack to match")
               balanced = False
               
            else:
               top = s.pop()
               
               if not matches (top, tag): #not a match... uh oh
                  print("Error: tag is", tag, "but top of stack is", top)
                  balanced = False
                  
               else: # its a match :)
                  print("The tag", tag, "matches the top of the stack")
                  print("The stack is now:", str(s))
                  
                  if top not in VALIDTAGS: # have to make sure that the tag is in validtags list
                     VALIDTAGS.append(top)
                     print(tag, "is a new valid tag")
                     print("Valid tags:", VALIDTAGS)
                     
        index += 1
       
    # while loop is over
    
    if balanced and s.isEmpty(): #everything is good after the while loop :)
        print("Processing complete.  No mismatches found.")
        
    elif balanced == True and s.isEmpty() == False: #there is still stuff in the stack that wasn't matched :(
        print("Processing complete.  Unmatched tags remain on stack:", str(s))

    print("Valid Tags:", VALIDTAGS)
    print("Exceptions:", EXCEPTIONS)


def matches (open, close):
    if open in close:
       return True
    else:
       return False

# write function called getTag that starts after < and then saves everything until you get to a > or a space
def getTagList():
   
    # making a string withof the whole text file 
    txtStr = ""
    with open("htmlfile.txt", "r", encoding="utf-8" ) as htmlfile:
          for line in htmlfile:
             for ch in line:
                txtStr += ch


    tagList = []
    
    #traversing through text
    index = 0
    while index < len(txtStr):
       ch = txtStr[index]

       # if its the start of a tag
       if ch == "<":
          index += 1
          newTag = ""
          # get the tag until a space or >
          while ch != " " or ">":
             ch = txtStr[index]
             newTag += ch
             index += 1
             tagList. append(newTag)
             
       else: # if it's not a tag
          index += 1
    
          
    return tagList

       
def main():
             
    htmlChecker(getTagList())

main()
