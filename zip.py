s1={2,3,1}
s2={'b','a','c'}
s3=list(zip(s1,s2))
print(s3) 

list1=[10,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
    stock=['reliance','tcs','hdfc']
    prices=[2134,1127,3420]
    new_dict={stock:price for stock,price in zip(stock,prices)}
    for stock,price in zip(stock,prices):
        print(f"the price of {stock} is {price}")