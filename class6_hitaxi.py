# in interpreter
#True- this is the right way to write
#5==6- output-False
#5==5 and 4==4  output-true 5==5 
#5==5 and 4==6 output=false
#5==5 or 4==6 output= True
def mark_levels(nums):
    count_a=0
    count_b=0
    count_c=0
    for num in nums:
        if num>=80:
            count_a +=1
        elif num>=60:
            count_b+=1
        else:
            count_c+=1
    print(f"There are {count_a} As, {count_b} Bs and {count_c} Cs.")
mark_levels([80,79,60,59,90]) # type in other nums to check

def mark_levels(nums): # make the code 2 levels
    count_a=0
    count_b=0
    for num in nums:
        if num>=80:
            count_a +=1
        else:
            count_b+=1
    return [count_a, count_b]

print(mark_levels([92,83,77,90,40]))
assert mark_levels([92,83,77,90,40])  ==[3,2]
assert mark_levels([90,80,70,98])==[3,1]

for i in range(5):
    print(i)

m=0
while m <5:
    print (m)
    m =m+1

 #CLASSROOM EXERCISE 1
def evens(nums):
    even_nums=[]
    for num in nums:
        if num %2==0:
            even_nums.append(num)
    return even_nums

assert evens ([1,2,3,4,5,6])==[2,4,6]
assert evens ([7,9,11])==[]

# def even_or_zero(nums): # do exercises
#     evens_zeros=[]
#     for num in nums:
#         if num % 2==0:
#             evens_zeros.append(num)
#         else:
#             evens_zeros.append(0)
#     return evens_zeros

# assert even_or_zero([1,2,3,4])==[0,2,0,]


