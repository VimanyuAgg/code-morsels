import copy

def getSubsets_after(setz):

    def _getSubsets_after(setz, index):
        if index == -1:
            return [[]]

        old_subs = _getSubsets_after(setz,index-1)
        new_subs = []
        item = setz[index]
        print(f"index:{index} - old_subs: {old_subs}")
        for val in old_subs:

            print(f"index:{index} - appending val: {val} from old_subs")
            new_subs.append(val)
            print(f"index:{index} - appended val: {val} from old_subs: new_subs: {new_subs}")
            entry = copy.deepcopy(val)
            entry.append(item)
            print(f"entry:{entry}")
            new_subs.append(entry)
            # print(f"index:{index} - appending val.append(item): {val.append(item)} from old_subs: new_subs: {new_subs}")
            # new_subs.append(val.append(item)) ## List is mutable
            print(f"index:{index} - appended val.append(item) from old_subs: new_subs: {new_subs}")

        return new_subs

    return _getSubsets_after(setz,len(setz)-1)

def getSubsets(setz, index):
    print(f"starting index: {index}")
    allSubsets = []
    if len(setz) == index:
        # base case - add empty set
        print(f"index: {index} match! _ adding [] to allSubsets")
        if [] not in allSubsets:
            allSubsets.append([])
    else:
        allSubsets = getSubsets(setz, index + 1)
        print(f"index:{index} - allSubsets after getSubsets - {allSubsets}")
        item = setz[index]
        print(f"index:{index} - item - {item}")
        moreSubsets = []
        print(f"index:{index} - initializing moreSubsets - {moreSubsets}")

        for subset in allSubsets:
            newSubset = []
            print(f"index:{index} -checking subset - {subset}")
            # newSubset = [value for value in subset if value not in newSubset]
            for value in subset:
                print(f"value in subset: {value}")
                if value not in newSubset:
                    print(f"{value} not in newSubset---appending to newSubset")
                    newSubset.append(value)
                else:
                    print(f"{value} exists in newSubsetAlready")
            # [newSubset.append(]
            newSubset.append(item)
            print(f"newSubset after appending item: {newSubset}")
            moreSubsets.append(newSubset)

        print(f"weird newSubset:{newSubset}")
        print(f"moreSubsets:{moreSubsets}")
        for value in moreSubsets:
            print(f"value in subset: {value}")

            if value not in newSubset:
                allSubsets.append(value)
            else:
                print(f"{value} exists in newSubset:{newSubset}")
        # [allSubsets.append(value) for value in moreSubsets if value not in newSubset]

    print(f"**returning {allSubsets}***")
    return allSubsets


def getSubsets_noprints(setz, index):
    allSubsets = []
    if len(setz) == index:
        # base case - add empty set
        if [] not in allSubsets:
            allSubsets.append([])
    else:
        allSubsets = getSubsets(setz, index + 1)
        item = setz[index]
        moreSubsets = []

        for subset in allSubsets:
            newSubset = []
            # newSubset = [value for value in subset if value not in newSubset]
            for value in subset:
                if value not in newSubset:
                    newSubset.append(value)
                else:
                    print(f"{value} exists in newSubsetAlready")
            # [newSubset.append(]
            newSubset.append(item)
            moreSubsets.append(newSubset)

        for value in moreSubsets:

            if value not in newSubset:
                allSubsets.append(value)
            else:
                print(f"{value} exists in newSubset:{newSubset}")
        # [allSubsets.append(value) for value in moreSubsets if value not in newSubset]

    print(f"**returning {allSubsets}***")
    return allSubsets



# print(getSubsets([1, 2, 3], 0))
print(getSubsets_after([1,1, 2, 3]))
# print(getSubsets(['a', 'b', 'c'], 0))
