'''
List Comprehension
'''
##This is what we mean by list comperehension, more concise
#squares = []
#for x in range (10):
#    squares.append(x ** 2)
 
#print(squares)


#print([x ** 2 for x in range(10)])

''' 
Conditionals in List Comprehension
'''
#combs = []
#for x in [1,2,3]: #for in loop
#    for y in [3,1,4]: #for in loop
#        if x != y: #conditional #if x not equal to 3
#            combs.append((x, y)) #touple
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
#print(combs)
#So below, we converted to list 

# with list comprehension
#combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#print(combs)
#!= (not equal to)

'''
Nested List Comprehension
'''

#a list within a list

#matrix = [
#  [1,2,3,4],
#  [5,6,7,8],
#[9,10,11,12] #you dont need a comma as thats the last itme
#]

#print(len(matrix))#matrix has 3 items in it
#res = [[row[i] for row in matrix] for i in range(4)]
#print(res)
# a list within a list and it loops through and gives us 1,5,9


# ===========================


#matrix = [
#  [1,2,3,4],
#  [5,6,7,8],
#[9,10,11,12]
#]

#res = []
#for i in range(4):
#   res.append([row[i] for row in matrix])
#print(res)



matrix = [
  [1,2,3,4],
  [5,6,7,8],
[9,10,11,12]
]

res = []
for i in range(4):
   res_row = []
   for row in matrix:
       res_row.append(row[i])
   res.append(res_row)

print(res)