import random

list1=['a','b','c']
list2=['x','y','z']
list3=['p','q','r']

classList=[0,1,2]

dataset={}

#randomly creating a dataset from above lists
for i in range(20):
    dataset[(random.choice(list1),random.choice(list2),random.choice(list3))]=random.choice(classList)

#displaying the dataset
for i in dataset:
    print(i,':',dataset[i])

#count the no. of different classes
countOfClasses={}
for classItem in classList:
    countOfClasses[classItem]=0
    for key in dataset:
        if classItem == dataset[key]:
            countOfClasses[classItem]+=1

print('\n')
print('count of classes......')
for i in countOfClasses:
    print(i,':',countOfClasses[i]) 

probabilityOfClasses={}
for classItem in countOfClasses:
    probabilityOfClasses[classItem]=countOfClasses[classItem]/len(dataset)

print('\n')
print('probability of each class......')
for i in probabilityOfClasses:
    print(i,':',probabilityOfClasses[i])


def count_of_x_wrt_a_class(x,aClass):
    count_x=0
    for dataItem in dataset:
        if aClass==dataset[dataItem] and x in dataItem:
            count_x+=1
    return count_x

print('\n')
testTuple=(random.choice(list1),random.choice(list2),random.choice(list3))
print('TESTING TUPLE : ',testTuple)

#maxProbability is used to store the maximum of all the probabilities...sara program bnane k baad isko bnaya hu...ekdum last mei...initially isko -1 lelo coz ksi ki probability negative hogi nhi
maxProbability=-1

#ek dictionary to store probability values for each class
probabilityRecord={}
for aClass in classList:
    print('\n')
    prodOfCondProb=1
    for anItem in testTuple:
        print('probability of ',anItem,'with respect to ','class ',aClass,' : ',count_of_x_wrt_a_class(anItem,aClass)/countOfClasses[aClass])
        #find a conditional probability and multiply it to previously calculated probabilities
        prodOfCondProb*=count_of_x_wrt_a_class(anItem,aClass)/countOfClasses[aClass]

    print('product of all conditional probabilities for class ',aClass,' : ',prodOfCondProb)
    print('probability of getting class ',aClass,' such that dataitem ',testTuple,'exist is ',prodOfCondProb*probabilityOfClasses[aClass])

    probabilityRecord[aClass]=prodOfCondProb*probabilityOfClasses[aClass]

    if prodOfCondProb*probabilityOfClasses[aClass] > maxProbability:
        maxProbability=prodOfCondProb*probabilityOfClasses[aClass]

print('\n')
for record in probabilityRecord:
    if probabilityRecord[record]==maxProbability:
        print('Predicted class for given data item ',testTuple,'is : ',record)
        break
print('\n')
