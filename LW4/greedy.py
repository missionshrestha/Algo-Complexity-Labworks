def greedy(bag,size,):       
    profit=0
    
    for i in bag:
        i["profit/weight"]= round(i["profit"] / i["weight"],2)
    bag.sort(key= lambda x: x["profit/weight"], reverse= True)

    for i in bag:
        if size<=0:
            break
        if i["weight"]<=size:
            profit=profit + i["profit"]
            size=size-i["weight"]
        else:
            profit= profit + i["profit"] * (size/i["weight"])
            size=0
    return profit





