#  File: sorting.py
#  Description: tests the speed of different sorts in different cases 
#  Student's Name: Hailey Cassidy
#  Student's UT EID: HAC787
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 11/26/17
#  Date Last Modified:11/26/17

###################################

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def reverse (alist): 
    # makes list in reverse order
     rlist = []

     while len(alist) > 0:
         rlist.append(alist[len(alist)-1])
         alist.remove(alist[len(alist)-1])

     return rlist

def almostSorted (alist):
    # swaps n pairs of elements randomly
    n = len(alist) * 0.1 # 10% of list, number of swaps

    for i in range(int(n)):
        randomIndex1 = random.randint(0,len(alist)-1) # random index
        randomIndex2 = random.randint(0,len(alist)-1) # random index
        # swap 
        temp = alist[randomIndex1]
        alist[randomIndex1] = alist[randomIndex2]
        alist[randomIndex2] = temp

    return alist 
        


def main():

# input type random   

    print("Input type = Random")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    
# bubble sort

    # for bubble sort n = 10 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble10_averageTime = totalTime / 5 

    # for bubble sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble100_averageTime = totalTime / 5 

    # for bubble sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble1000_averageTime = totalTime / 5

    print("      bubbleSort    " + '{:.6f}'.format(bubble10_averageTime) + "   " + '{:.6f}'.format(bubble100_averageTime) + "   "+ '{:.6f}'.format(bubble1000_averageTime))

# insertion sort

    # for insertion sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert10_averageTime = totalTime / 5 

    # for insertion sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert100_averageTime = totalTime / 5 

    # for insertion sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert1000_averageTime = totalTime / 5

    print("   insertionSort    "+ '{:.6f}'.format(insert10_averageTime) + "   " + '{:.6f}'.format(insert100_averageTime) + "   "+ '{:.6f}'.format(insert1000_averageTime))

# merge sort

    # for merge sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge10_averageTime = totalTime / 5 

    # for merge sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge100_averageTime = totalTime / 5 

    # for merge sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge1000_averageTime = totalTime / 5

    print("       mergeSort    "+ '{:.6f}'.format(merge10_averageTime) + "   " + '{:.6f}'.format(merge100_averageTime) + "   "+ '{:.6f}'.format(merge1000_averageTime))

# quick sort

    # for quick sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick10_averageTime = totalTime / 5 

    # for quick sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick100_averageTime = totalTime / 5 

    # for quick sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        random.shuffle(myList) # shuffled list
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick1000_averageTime = totalTime / 5

    print("       quickSort    "+ '{:.6f}'.format(quick10_averageTime) + "   " + '{:.6f}'.format(quick100_averageTime) + "   "+ '{:.6f}'.format(quick1000_averageTime))

# input type sorted  

    print("\nInput type = Sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    
# bubble sort

    # for bubble sort n = 10 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble10_averageTime = totalTime / 5 

    # for bubble sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble100_averageTime = totalTime / 5 

    # for bubble sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble1000_averageTime = totalTime / 5

    print("      bubbleSort    " + '{:.6f}'.format(bubble10_averageTime) + "   " + '{:.6f}'.format(bubble100_averageTime) + "   "+ '{:.6f}'.format(bubble1000_averageTime))

# insertion sort

    # for insertion sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert10_averageTime = totalTime / 5 

    # for insertion sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert100_averageTime = totalTime / 5 

    # for insertion sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert1000_averageTime = totalTime / 5

    print("   insertionSort    "+ '{:.6f}'.format(insert10_averageTime) + "   " + '{:.6f}'.format(insert100_averageTime) + "   "+ '{:.6f}'.format(insert1000_averageTime))

# merge sort

    # for merge sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge10_averageTime = totalTime / 5 

    # for merge sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge100_averageTime = totalTime / 5 

    # for merge sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge1000_averageTime = totalTime / 5

    print("       mergeSort    "+ '{:.6f}'.format(merge10_averageTime) + "   " + '{:.6f}'.format(merge100_averageTime) + "   "+ '{:.6f}'.format(merge1000_averageTime))

# quick sort

    # for quick sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick10_averageTime = totalTime / 5 

    # for quick sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick100_averageTime = totalTime / 5 

    # for quick sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick1000_averageTime = totalTime / 5

    print("       quickSort    "+ '{:.6f}'.format(quick10_averageTime) + "   " + '{:.6f}'.format(quick100_averageTime) + "   "+ '{:.6f}'.format(quick1000_averageTime))

# input type reverse   

    print("\nInput type = Reverse")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    
# bubble sort

    # for bubble sort n = 10 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble10_averageTime = totalTime / 5 

    # for bubble sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble100_averageTime = totalTime / 5 

    # for bubble sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble1000_averageTime = totalTime / 5

    print("      bubbleSort    " + '{:.6f}'.format(bubble10_averageTime) + "   " + '{:.6f}'.format(bubble100_averageTime) + "   "+ '{:.6f}'.format(bubble1000_averageTime))

# insertion sort

    # for insertion sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert10_averageTime = totalTime / 5 

    # for insertion sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert100_averageTime = totalTime / 5 

    # for insertion sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert1000_averageTime = totalTime / 5

    print("   insertionSort    "+ '{:.6f}'.format(insert10_averageTime) + "   " + '{:.6f}'.format(insert100_averageTime) + "   "+ '{:.6f}'.format(insert1000_averageTime))

# merge sort

    # for merge sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge10_averageTime = totalTime / 5 

    # for merge sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge100_averageTime = totalTime / 5 

    # for merge sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge1000_averageTime = totalTime / 5

    print("       mergeSort    "+ '{:.6f}'.format(merge10_averageTime) + "   " + '{:.6f}'.format(merge100_averageTime) + "   "+ '{:.6f}'.format(merge1000_averageTime))

# quick sort

    # for quick sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick10_averageTime = totalTime / 5 

    # for quick sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick100_averageTime = totalTime / 5 

    # for quick sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        myList = reverse(myList) # reverses list 
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick1000_averageTime = totalTime / 5

    print("       quickSort    "+ '{:.6f}'.format(quick10_averageTime) + "   " + '{:.6f}'.format(quick100_averageTime) + "   "+ '{:.6f}'.format(quick1000_averageTime))

# input type almost sorted    

    print("\nInput type = Almost sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    
# bubble sort

    # for bubble sort n = 10 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        almostSorted(myList) # reverses list 
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble10_averageTime = totalTime / 5 

    # for bubble sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble100_averageTime = totalTime / 5 

    # for bubble sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        bubbleSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    bubble1000_averageTime = totalTime / 5

    print("      bubbleSort    " + '{:.6f}'.format(bubble10_averageTime) + "   " + '{:.6f}'.format(bubble100_averageTime) + "   "+ '{:.6f}'.format(bubble1000_averageTime))

# insertion sort

    # for insertion sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert10_averageTime = totalTime / 5 

    # for insertion sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert100_averageTime = totalTime / 5 

    # for insertion sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        insertionSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    insert1000_averageTime = totalTime / 5

    print("   insertionSort    "+ '{:.6f}'.format(insert10_averageTime) + "   " + '{:.6f}'.format(insert100_averageTime) + "   "+ '{:.6f}'.format(insert1000_averageTime))

# merge sort

    # for merge sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge10_averageTime = totalTime / 5 

    # for merge sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge100_averageTime = totalTime / 5 

    # for merge sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        mergeSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    merge1000_averageTime = totalTime / 5

    print("       mergeSort    "+ '{:.6f}'.format(merge10_averageTime) + "   " + '{:.6f}'.format(merge100_averageTime) + "   "+ '{:.6f}'.format(merge1000_averageTime))

# quick sort

    # for quick sort n = 10
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(10)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick10_averageTime = totalTime / 5 

    # for quick sort n = 100 
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(100)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick100_averageTime = totalTime / 5 

    # for quick sort n = 1000
    totalTime = 0
    for x in range(5):
        myList = [i for i in range(1000)]
        myList = almostSorted(myList) # reverses list 
        startTime = time.time()
        quickSort(myList)
        endTime = time.time()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime
    quick1000_averageTime = totalTime / 5

    print("       quickSort    "+ '{:.6f}'.format(quick10_averageTime) + "   " + '{:.6f}'.format(quick100_averageTime) + "   "+ '{:.6f}'.format(quick1000_averageTime))

main()

