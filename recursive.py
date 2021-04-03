# def recu_sum(numList):
#     if len(numList) ==1:
#         return numList[0]
#     return numList[0] + recu_sum(numList[1:])

# print(recu_sum([1,3,5,7,9]))

# def b_(num):
#     if num == 1:
#         return -5
#     return -5+ b_(num-1) + 9

# print(b_(4))

print('\n')

def lookval(ls, look_val):
    nmax= len(ls)
    nmin = 0
    if len(ls) ==1:
        if ls[0] == look_val:
            return True
        return False
    else:
        nmid= len(ls)//2
    if look_val == ls[nmid]:
        return True
    elif look_val<ls[nmid]:
        nmax = nmid
        return lookval(ls[nmin:nmax],look_val)
    else:
        nmin = nmid
        return lookval(ls[nmin:nmax],look_val)
flist = [1,2,3,4,5,6,8,9,10,11,14,16]
print(lookval(flist,7))

