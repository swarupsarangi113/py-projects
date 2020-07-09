myList = []
n = int(input('Enter the size of the list: '))
for i in range(n) :
    myitem = input('Enter the '+ str(i)+' item: ')
    myList.append(myitem)
    
#print(myList)
#myList = ['apples','banana','cats','tofu']
    
def list2str(sampleList) :
    output = ''
    for index,item in enumerate(sampleList) :
        if index != len(sampleList) - 1 :
            output += item + ', '
        else :
            output = output + 'and ' + item
            
    print(output)

list2str(myList)

