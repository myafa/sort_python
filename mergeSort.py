import random

def performMergeSort(lstElemnetToSort):
    if len(lstElementToSort) ==1:
	return lstElementToSort
    
    lstSubElementToSort1 = []
    lstSubElementToSort2 = []
    for it in range(len(lstElementToSort)):
	if len(lstElementToSort)/2 > itr:
	    lstSubElementToSort1.append(lstElementToSort[itr])
	else:
	    lstSubElementToSort2.append(lstElementToSort[itr])
#Decomposition finished
#Below is recursion
    lstSubElementToSort1 = performMergeSort(lstSubElementToSort1)
    lstSubElementToSort2 = performMergeSort(lstSubElementToSort2)
#Below is Aggregation
    idxCount1 = 0
    idxCount2 = 0
    for itr in range(len(lstElementToSort)):
	if idxCount1 == len(lstSubElementToSort1):
	    lstElementToSort[itr] = lstSubElementToSort2[idxCount2] 
	    idxCount2 +=1
	elif idxCount2 == len(lstSubElementToSort2):
	    lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
	    idxCount1 +=1
	elif SubElementToSort[idxCount1] > lstSubElementToSort2[idxCount2]:
	    lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
	    idxCount2 +=1
	else:
	    lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
	    idxCount1 +=1
    return lstElementToSort
