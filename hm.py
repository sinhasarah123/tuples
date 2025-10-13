numbers1=[1,2,3]
numbers2=[4,5,6,7]
result=map(lambda x,y:x+y,numbers1,numbers2)
numbers1,numbers2
print(list(result))
numbers=[1,2,3,4,5,6]
def sq(n):
    return n*n
squared=map(sq,numbers)
print(list(squared))