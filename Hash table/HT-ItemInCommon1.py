def item_in_common(list1, list2):
    # for i in list1:
    #     for j in list2:
    #         if i == j:
    #             return True
    # return False
    seen = {}
    for i in list1:
        seen[i] = True
    for j in list2:
        if j in seen:
            return True
    return False


list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))

