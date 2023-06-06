def knapSackFractional(n, bag, size, i):

    # if all items have been evaluated or the capacity of the bag is zero
    if i == n or size <= 0:
        return 0

    # if the weight of the current item is less than or equal to the remaining capacity of the bag
    if bag[i]["weight"] <= size:
        profitin = bag[i]["profit"] + knapSackFractional(len(bag), bag, size-bag[i]["weight"], i+1)
        profitout = knapSackFractional(len(bag), bag, size, i+1)
    else:
        profitin = bag[i]["profit"] * (size / bag[i]["weight"])
        profitout = knapSackFractional(len(bag), bag, size, i+1)
    # we need to return the maximum profit obtained by either including or excluding the current item
    return max(profitin, profitout)


def knapSack01(n, bag, size, i):
    if i == n or size <= 0:
        return 0

    if bag[i]["weight"] <= size:
        profitin = bag[i]["profit"] +  knapSack01(len(bag), bag, size-bag[i]["weight"], i+1)
        profitout = knapSack01(len(bag), bag, size, i+1)
        return max(profitin, profitout)
    else:
        profitout = knapSack01(len(bag), bag, size, i+1)
        return profitout
