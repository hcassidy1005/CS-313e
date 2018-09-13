#  File: MultiwayTree.py
#  Description: Tells if different multiway tree are isomorphic to each other 
#  Student's Name: Hailey Cassidy
#  Student's UT EID: HAC787
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 12/1/17
#  Date Last Modified:12/8/17 

# input list [data item, [list of children] ]

class MultiwayTree:

    def __init__(self, pyTree):
        # given pyTree, a python representation of a tree
        # create a node-and-pointer representation of that tree

        # not sure what I'm doing here!!!
        
        self.data = pyTree[0]
        self.children = []
        for i in range(len(pyTree[1])):
        
            self.children.append(MultiwayTree(pyTree[1][i]))

            

    def preOrder(self):
        # print out the node-and-pointer representaztion of a tree using preorder

        #3 laws of recursion

        #have a base case

        #iterate to the base case

        #call itself

        result = str(self.data) + " "

        for i in range(len(self.children)):
            result += self.children[i].preOrder() 

        

        return result


        # preorder goes root, left, right 

    def isIsomorphicTo(self, other):
        # return True if tree self has the same structure as the tree other
        # return False otherwise

        
        if len(self.children) != len(other.children):
            return False 
        elif len(self.children) == 0 and len(other.children) == 0:
            return True 
        else:
            for i in range(len(self.children)):
                if(not(self.children[i].isIsomorphicTo(other.children[i]))):
                    return False
            return True 
            
        


def main():
    f = open("MultiwayTreeInput.txt", "r")# opens text file for reading
    line = f.readline()
    treeNum = 1
    while line != "":

        # first tree
        print("Tree " + str(treeNum) + ": " + line)
        inputList = eval(line)
        tree1 = MultiwayTree(inputList)
        print("Tree "+ str(treeNum) + " preorder: " + tree1.preOrder() + "\n")

        # second tree
        line = f.readline()
        treeNum += 1 
        print("Tree " + str(treeNum) + ": " + line)
        inputList = eval(line) 
        tree2 = MultiwayTree(inputList)
        print("Tree "+ str(treeNum) + " preorder: " + tree2.preOrder() + "\n")

        # comparing the two trees 
        if tree1.isIsomorphicTo(tree2):
            print("Tree " + str(treeNum - 1) + " is isomorphic to Tree "+ str(treeNum) + "\n")
        else:
            print("Tree " + str(treeNum - 1) + " is not isomorphic to Tree "+ str(treeNum) + "\n")

        line = f.readline()
        treeNum += 1

main() 
