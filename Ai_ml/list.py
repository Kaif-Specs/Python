list = [1,2,3,4,5,6,6,78]
print(list)
print(max(list))
print(sorted(list))
print(max(list))
print(len(list))
print(min(list))
print(4 in(list))
list0=['hiiii kaif']*4
print(list0)
list1 =['a','b','c','d']
print(max(list1))
fruits = ['apple']
fruits.append('mango')
print(fruits)
fruits.append('hello')
print(fruits)
num1 =[1,2,3,4]
num2 =[4,4,4,4,3,3,3,3]
num1.extend(num2)
print(num1)
num3 =[1,2,3,4,5,6,7]
num3.remove(4)
print(num3)
color =['red','balck']
color.pop(1)
print(color)
num5 =[1,2,3,4,5]
num5.clear()
print(num5)
num6 =[1,2,3,4,4,4,5,6]
num7 =[2,3,4,51,2,34]
print(num6.index(5))
print(num6.count(4))
num7.sort()
print(num7)
items5 = [3,4,5,6,7]
items5.pop(3)
print(items5)
listz=[1,2,3,4,5]+[2,3,4,5,6]
print(listz)

listnoman=[1,2,3,4,4,5,6,6]
listjnaida=[2,3,4,5,67]
print(listnoman==listjnaida)
#tuples
tup1=('physics''maths''bio')
tup2=('india','pakistan','noida')
print()
dict ={'name':"kaif",'class':"4th",'section':"c"}
print(dict)
dict1 ={'size':"kaif",'color':"4th",'class':"c"}
print(dict1)
dict2 ={'name':"kaif",'class':"4th",'section':"c"}
print(dict2)
#def function name (parameters):
#statements
#return value
#def area(length = 10, width =5):
#
#keyword
#def employee(name,salary)
def student_info(**details):
    print(details)
    student_info(name="amit",roll="101",dept="MCA")