import random

def sort(list: list):
    swapped = True #initial condition for while loop to run
    A = 1
    while swapped == True:
        swapped = False 
        for item in range(len(list)-A):
            if list[item] > list[item+1]:
                temp = list[item]
                list[item] = list[item+1]
                list[item+1] = temp
                print(f"swapped list[{item}]:{list[item]} and list[{item+1}]:{list[item+1]}")
                swapped = True
        A += 1
    return list


if __name__=="__main__":    
    dataset = []
    for i in range(1,100):
        dataset.append(random.randint(1,100)) #make 100 random values
    print(sort(dataset))

