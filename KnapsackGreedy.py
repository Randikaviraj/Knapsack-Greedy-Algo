import sys
import time

def shortKey(ele):
    return ele[1]


def GreedyKnapsack(value: list,cost: list,amountOfMoneyWeHave: int):
    initialMoney=amountOfMoneyWeHave
    g=[]
    a=[]
    for i in range(len(value)):
        a.append((i,(value[i]/cost[i])))
    a.sort(key=shortKey,reverse=True)
    
    for item in a:
        if amountOfMoneyWeHave<=0:
            break
        if cost[item[0]]<=amountOfMoneyWeHave:
            g.append(item[0])
            amountOfMoneyWeHave=amountOfMoneyWeHave-cost[item[0]]
            
    amax=max(value)
    valueG=0
    for i in g:
        valueG=valueG+value[i]
        
    if amax>valueG and cost[value.index(amax)]<=initialMoney:
        return value.index(amax)
    else:
        return g
        
    


if __name__ =="__main__":
    try:
                
        with open(sys.argv[1],"r") as file:
            print(f"{sys.argv[1]} Reading..")
            line=file.readline()
            amountOfMoneyWeHave=int(line.split(" ")[1])
            cost=[]
            value=[]
            line=file.readline()
            while line:
                list=line.split(" ")
                costValuePair=[]       
                for item in list:
                    item=item.strip('\n')
                    if item:
                        costValuePair.append(int(item))
                value.append(costValuePair[0])
                cost.append(costValuePair[1])
                line=file.readline()

            print('Algorithm Started::')
            seconds = time.time()
            g=GreedyKnapsack(value,cost,amountOfMoneyWeHave)
            seconds = seconds-time.time()
            print('Answer to Min cost Knapsack problem :')
            print("____________________________________________________________________________")
            print("Object set :")
            print(g)
            print("____________________________________________________________________________")
            print('Finished::')
            print('Running Time in second'+str(seconds))
            
    except Exception as e:
        print(e)
        print('Invalid no of Arguments :: python KnapsackGreedy.py <filename> ')