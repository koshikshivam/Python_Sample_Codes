# print("hello world")


# x = int(input("enter value"))
# if x<0:
#     print("negitive")
# elif x>0:
#     print("positive")
# else:
#     print("zero")



# x = int(input("enter value"))
# if x %2==0:
#     print("even")
# elif x%2!=0:
#     print("odd") 


# sum = 0
# x = int(input("enter value"))
# for i in range(0,x+1):
#     sum = sum+i
#     print(i)
# print(sum)

# sum = 0
# x = int(input("enter num1"))
# y = int(input("enter num2"))
# for i in range(x,y+1):
#     sum = sum+i
#     print(i)
# print(sum)

    
    
# x = int(input("enter value"))
# y = int(input("enter value again"))
# if x >y:
#     print(x,"is grater")
# else:
#     print(y,"is greater")



# x = int(input("enter value"))
# y = int(input("enter value again"))
# z = int(input("enter value againnnn"))

# if x>y and x>z:
#     print(x,"is grater")
# elif y>x and y>z:
#     print(y,"is greater")
# else:
#     print(z,"is gresater")



# x = int(input("enter value"))
# if x % 4==0 and x% 100!=0 or x %400==0:
    
#     print("leap")
# else:
#     print("not leap")



# count=0
# x = int(input("enter value"))

# for i in range(1,x+1):
#     #print(i)
#     if x%i==0:
#         count+=1
#         #print(count)
        
# if count==2:
    
#     print("prime")
# else:
#     print("not prime")
    
    
    
# rem=0
# x = int(input("enter value"))
# while(x!=0):
#     rem = rem+x%10
#     x = x//10
# print(rem)



# rem=0
# rev = 0
# x = int(input("enter value"))
# while(x!=0):
#     rem = x%10
#     x = x//10
#     rev = (rev*10)+rem
# print(rev)



# rem = 0
# rev=0
# x = int(input("enter value"))
# temp =x
# while(x!=0):
#     rem = x%10
#     x  = x//10
    
#     rev = (rev*10)+rem
# if temp==rev:
#         print("palindrome")
# else:
#         print("not palindrome")
# print(rev)


# first = 0
# second = 1 
# x = int(input("enter value"))
# for i in range(first,x+1):
#     third = first+second
#     first = second
#     second = third
#     print(second,end='')



# x = int(input("enter value"))
# for i in range(0,x):
#     i = i**2   
#     print(i)
    
    

# l1.append(5)
# l1.clear()
# x = l1.count(3)
# l1.extend([10,11,12,13,14])
# x = l1.index(4)
# l1.insert(0,[10,11,12,13,14,15])
# l1.pop(4) #you have to mention the index
# l1.sort()
# l1.reverse()


# t1 = (1,2,3,4,5,6)
# x = t1.index(5)
# print(x)


# t1 = (1,2,3,4,5,6,7,8,9,10)
# print(len(t1))                                                                                                                                                                                                  



# s1 = {1,2,3,4,}
# # s1.remove(5)
# l1 = [9,8,7,6,5]
# s1.update(l1)
# print(s1)

# d = {"name":"python",
#      "roll": "language",
#      "number":121
# }
# x = d.keys()
# d["abcd"] = "efgh"
# f  = len(d)




# dict1 ={"name":"python","roll":1234,"lname":"cpython"} 

# dict1.clear()
# print(dict1)
# for i in dict1:
#     print(i)

# dict1.pop("name")
# print(dict1)

# t1 = (1,2,3,4)
# x = t1.index(2)
# print(x)


# s1 = {1,2,3,4,"abcd","efgh"}
# # s1.add(1234)
# s1.remove(1)
# print(s1)
# for i in s1:
#     print(i)

# def my_function():
#     print("hey")
    
# my_function()
    

# def my_fun(name):
#     print("my name is",name)


# my_fun("shiv")

# def add_num(a,b):
#     sum=a+b;
#     return sum; 




# num1=int(input("input the number one: "))
# num2=int(input("input the number one :"))
# print(add_num(num1,num2))


# def my_fun(a,b):
#     sum = a+b
#     mul = a*b
#     sub = a-b
#     print(f"{sum},{mul},{sub} ")
  
# a = int(input("enter value"))
# b = int(input("enter value again"))
# my_fun(a,b)



# def fun2(roll):
#     li = [1,2,3,4]
#     if roll in li:
#         print(f"{roll} is present")
#     else:
#         print(f"{roll} absent")
        
# roll = int(input("enter value"))
# fun2(roll) 
        

# def max(a,b,c):
#     if a>=b and a>=c:
#         print(f"{a} is greater")
#     elif b>=c and b>=a:
#         print(f"{b} is greater")
#     else:
#         print(f"{c} is gretaer")
        
# a = int(input("enter value"))
# b = int(input("enter value"))       
# c = int(input("enter value"))
# max(a,b,c)


# def odd_even(a):
#     if a%2==0:
#         print(f"{a} is even")
#     elif a%2!=0:
#         print(f"{a}  is odd")
    
# a = int(input("enter value"))
# odd_even(a)


# def con_vow(a):
#     vo=0;
#     co = 0
#     for i in range(len(a)):
#         if a[i] in ['a','e','i','o','u']:
#             vo = vo+1
#         else:
#             co=co+1
#     print("vowel is ", vo)
#     print("conso is " , co)
    
# a = input("enter string")
# con_vow(a) 
     
     
     
     
# def fact(a):
#     c = 1
#     for i in range(1,a+1):
#         c = c*i
#     print(c) 
# a = int(input("enter value"))
# fact(a)        


# LIST 



# def swap(l1):
#     size = len(l1)
#     temp  = l1[0]
#     l1[0] = l1[size-1]
#     l1[size-1]=temp
#     print(l1)

# l1 = [1,2,3,4]
# swap(l1)
            
    
    
# l1 = [1,2,3,4,5]
# size=(len(l1))
# print(size-3)
    
    
    
# def swap(l1,pos1,pos2):
#     l1[pos1],l1[pos2] = l1[pos2],l1[pos1] 
#     print(l1)

# pos1 = int(input("enter value"))
# pos2 = int(input("enter value again"))

# l1 = [23, 65, 19, 90]
# swap(l1,pos1-1,pos2-1)



# x = lambda x,y: x//y
# print(x(17,8))


# a = lambda x,y,z: x+y+z
# print(a(1,1,1))




# def check(a):
#     if a in l1:
#         print("yes element is present")
#     else:
#         print("element is not present")
# l1 = [1,2,3,4]
# a = int(input("enter element"))
# check(a)



# s = "abcdEFGH"
# t =s.swapcase()
# print(t)



# def print_full_name(first, last):
#     print(f"Hello {first} {last}! You just delved into python.")

# first_name = input()
# last_name = input()
# print_full_name(first_name, last_name)


# def counting(s):
#     size = len(s)
#     for i in s:
#         pass    
#         #print(i)

# s = input("enter string")
# counting(s)



# l1=[2, 3 ,6, 6, 5]
# l1.sort(reverse=True)
# print(l1[2])






# def harshed_number(a):
#     rem = 0
#     sum=0
#     while(a!=0):
#         rem = a%10     
#         a = a//10
#         print(rem)

# x = int(input("enter the value"))
# harshed_number(a)


# def harhsed_number(n):
#     count=0
#     rem=0
#     while(n!=0):
#         rem = n%10
#         count=count+rem
#         n = n//10
#     if n%count==0:
        
#         print("yes")
#     else:
#         print("no")

# n = int(input("enter value"))
# harhsed_number(n)

# import array as arr
# arr=[1,2,3,4,5]
# min=arr[0]
# for i in range(len(arr)):
#     if arr[i]<min:
#         min =arr[i]
# print(min)



# arr=[10, 13, 17, 11, 34, 21]                                                                                                                                                  
# temp=0
# size = len(arr)
# # first = arr[0]
# # last=size-1
# # mid = (first+last)/2
# for i in range(0,size/2):
#     for j in range(0,(size/2)-1):
#         if arr[j]> arr[j+1]:
#             temp = arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=temp
# for i in range(size):
#     print(arr[i])
# #print(size)










# size= len(arr)
# for i in range(size-1,0,-1):
#     print(arr[i],end='  ')
    
    
    
    




# temp=0
# size = len(arr)
# for i in range(0,size):
#     for j in range(0,size-1):
#         if arr[j]>arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1]=temp         
# for i in range(size):
#     print(arr[1])



# arr=[1,2,3,4,5]
# c = 0
# for i in arr:
#     c = c+i
# print(c)


# arr=[1,2,3,4]
# size = len(arr)
# for i in range(size-1,-1,-1):
#     print(arr[i],end='  ')


 
# frequency of elements in array

# arr=[5,5,4,3,1,5]
# count = {}
# for i in arr:
#     if i in count:
#         count[i] = count[i]+1
#     else:
#         count[i]=1
# print(count)
    
    
# arr=[1,2,3,4,3,2]
# size = len(arr)
# for i in range(0,size):
#     for j in range(i+1,size):
#         if arr[i]==arr[j]:
#             print(arr[j])


# string = "PREPinsta"
# print(string.swapcase())



# def count(a):
#     vo=0
#     for i in range(len(a)):
#         if a[i] in ['a','e','i','o','u']:
#             vo = vo+1
#     print(vo)
    
        


# a = input("enter string")

# count(a)
    
 


# def con_vow(a):
#         vo=0;
#     co = 0
#     for i in range(len(a)):
#         if a[i] in ['a','e','i','o','u']:
#             vo = vo+1
#         else:
#             co=co+1
#     print("vowel is ", vo)
#     print("conso is " , co)
    
# a = input("enter string")
# con_vow(a) 



# temp = "nitin"
# s1 = "nitin"[::-1]
# if (temp==s1):
#     print("yes")

# else:
#     print("no")\



    

# s1 = "shivaah"
# size = len(s1)
# count={}
# for i in s1:
#     if i in count:
#         count[i]=count[i]+1
#     else:
#         count[i]=1
# print(count)




# import unittest
# class TextAnylsisTest(unittest.TestCase):
#     def test_function_runs(self):
#         analyze.text()
        
        
        
# if __name__=="main":
#     unittest.main

# a=[1,2,3,4,4,6,7,8,9,8,10,12]
# size = len(a)
# # count={}
# # for i in range(len(a)):
# #     if i in count:
# #         count[i]=count[i]+1
# #     else:
# #         count[i]=1
# # print(count)

# for i in range(0,size):
#     for j in range(i+1,size):
#         if a[i]==a[j]:
#             print(a[i])
    
    
    

# import unittest
# class LearnTest(unittest.TestCase):

#     def test_fn(self):
#         pass


#     def test_fn2(self):
#         pass


# if __name__ == "main":
#     unittest.main()
    

# import math

# print(math.factorial(5))



# l=[5,9,6,4,100]
# l.insert(4,200)
# print(l)





# s1={10,20,30,40}
# # print(s1)
# s1.add(90)
# # print(s1)
# #s1.update(90,80)
# # print(s1)
# s1.update({88,77},[95,66])
# # print(s1)
# s1.discard(10)
# # print(s1)
# # s1.remove(101)
# # print(s1)
# # s1.clear()
# # print(s1)


# s2 = {90,80,70,60}
# # print(len(s2))
# # print(89 in s2)

# s4 = {60,89,30}
# s5 = {99,88,33,30}
# print(s4.union(s5))
# print(s4.intersection(s5))
# print(s4.symmetric_difference(s5))
# print(s4.isdisjoint(s5))

# d1 = {101:'emp1',102:'emp2',103:'emp3',104:'emp4'}
# d1[104]="employee 99"
# print(d1.popitem())
# print(d1)
# print(d1)
# d1.pop(101)
# print(d1)
# d1[101]='employee1'
# print(d1)
# if 102 in d1:
#     print("present")
# else:
#     print("not present")
# print(d1.get(123,'na'))
# if 123 in d1:
#     print(d1[123])
# else:
#     print('na')

# print(d1)
# d1[101]="emp5"
# print(d1)





# a = 10
# b = "12"
# c = a+b
# print(c)
#b = True
# c = a+b
# print(c)


# a = 10
# b = False
# c = a+b
# print(c)



# print(list(s))
# print(tuple(s))
# print(set(s))

# l1 = ['a','b','c','d']
# t1 = ('a','b','c','d')
# s1  = {'a','b','c','d'}
# print()

# a = 'a' 
# b = 20
# c = int(a)+b
# print(c)


# a = 10
# print(oct(a))

# print("welcome ",sep="") 
# print("hello",'shiva','how',sep='-')

# name = input("whats your name")
# print("hello",name)


# s1= ""
# s2 = s1 and"hello"
# print(s2)

# x = 10
# y = 10
# print(x is y)


# n = int(input('enter value'))
# c = 0
# for i in range(1,n+1):
#     c= c+i
# print(c)

# n = int(input('enter value'))
# c = 1
# for i in range(1,10):
#     c = n*i
#     print(c, sep="--")



# i=0
# while(i<=5):
#     print('gfg')
#     i=i+1
    
    
# def fun_sum(n):
#     c = 0
#     for i in range(1,n+1):
#         c=c+i
#     return c
        
# print(fun_sum(5))



# l=[30,60,40]
# x = len(l)
# y=(sum(l))
# print('mean of above list is ' , y/x)


#------------------------------------------------------------------------------------------------------------------------------------------

# l  =[10,41,30,15,18]
# even=[]
# odd = []
# for i in l:
#     if i%2==0:
#         even.append(i)
# print('the even numbers in', l , 'is',  even)
# for k in l:
#     if k %2!=0:
#         odd.append(k)
# print('the odd numbers in', l , 'is',  odd)


# l = [11,19,6,17,8,14,7]
# x=10
# temp=[]
# for i in l:
#     #print(i,end=" ")
#     if x>i:
#         temp.append(i)
# print(temp)


# l = [1,2,3,4]
# l2 = l[:]
# print(l is l2)


# li=[10,9,17,18,15]
# max = li[0]
# min = li[0]
# for i in li:
#     if (i>=max):
#         max = i
# print('max = ',max ,end = " ")
# print()
 
# for j in li:
#     if (j<min):
#         min = j
# print('min  =', min ,end=" ")
# print()  


# li=  [70, 11, 20, 4, 100]
# largest  = max(li)
# s_largest = 0
# for i in li:
#     if i !=largest:
#         if s_largest==0:
#             s_largest = i
#             print(s_largest)
# #         else:
#             s_largest = max(i,s_largest)
# print(s_largest)
            
        
#finding the second largest number in a list

# li = [10,20,30,40]
# new_li = list(li)
# temp = li
# temp.remove(max(new_li))
# # print(temp)
# s_max = temp[0]
# for i in temp:
#     if i >=s_max:
#         s_max=i
# print('second largest = ',  s_max)


# def is_sorted(l):
#     for i in range(1,len(l)):
#         if l[i]<l[i-1]:
#             return False
#         else:
#             return True
        
# l= [10,20,30,40,50]
# if is_sorted(l):
#     print("yes")
# else:
#     print('No')

# l = [10,30,20,50]
# temp = l
# s1 =sorted(l)
# if temp == s1:
#     print('yes')
# else:
#     print('no')



# def is_odd(l):
#     res = 0
#     for i in l:
#         count = l.count(i)
#         if count%2!=0:
#             res = i
#             return res
#             break
    

# l = [10,10,10,10,10,20,20]
# print(is_odd(l))

# l = [10,20,30,40]
# s = len(l)
# for i in range(1,s):
#     print(i)
# # print(l[1:]+l[0:1])

 
# rotation if element by one place

# def rotation(l):
#     n = len(l)
#     first_element = l[0]
#     # print(n)
#     # print(first_element)
#     for i in range(1,n):
#         #print(i)
#         l[i-1]=l[i]
#     l[n-1]=first_element
#     return l
    
# l = [10,20,30,40]
# print(rotation(l))

# def largest(a,b,c):
#     if a>b and a>c:
#         print(a," is greater")
#     elif b>a and b>c:
#         print(b ,'is greater')
#     else:
#         print(c,'is greater')
        
# c = largest(3,7,11)
# print(c)

# temp = " hy\'s \n this is shivam"
# print(temp)

# s = input('enter string')
# rev = ''
# for i in s:
#     rev = i+rev
#     print(rev)
    
# name = "shivam"
# technology = "python"
# t1 = "my name is %s and my technology is %s" %(name,technology)
# print(t1)



# name = "shiv"
# tech = "python"
# s4 = f"my name is {name} and my technology is {tech}"
# print(s4) 
# s1 = "my name is {0} and my technology is {1}".format(name,tech)
# print(s1)


# a = 10
# b = 20
# s1 = f'sum of {a} and {b} is {a+b}'
# s2 = f'product of {a} and {b} is {a*b}'
# print(s1)
# print(s2)


# txt =input('enter text')
# start = 0
# end = len(txt)-1
# while start<end:
#     if txt[start] != txt[end]:
#         print('no')
#         break
#     start = start+1
#     end = end-1
# else:
#     print('yes')
        
        
# def anagram(s1,s2,s3,s4):
#     if len(s1) == len(s2) and s3 == s4:
#         return True
#     else:
#         return False
    
    
# s1 = "abaac"
# s2  = "acbaa"
# s3 = sorted(s1)
# s4 = sorted(s2)
# c=anagram(s1,s2,s3,s4)
# print(c)

# s1 = "bad"
# s2 = "dad"
# s3 = sorted(s1)
# s4 = sorted(s2)
# if len(s1) == len(s2) and s3 ==s4:
#     print('yes')
# else:
#     print('no')


# if len(s1)!=len(s2):
#     print("no")
# count = [0]*256 

# s1 = 23
# s2 = 'gfg'
# print(hash(s2))




# l1=[10,20,30,40]
# d = int(input('enter value'))
# temp = l1[0]
# c = len(l1)
# for i in range(1,c):
#     l1[i-d] = l1[i]
# l1[c-d]=temp
# print(l1)
    


# li=['shiv','ravi','ram']
# for i in enumerate(li):
#     print(i)




# def fun_1(n):
#     if n==0: 
#         return
#     else:
#         fun_1(n-1)
#         print(n)
#         fun_1(n-1)


# fun_1(3)

# for i in range(5,0,-1):
#     print(i)

# def recursion(n):
#     if n==0:
#         return None
#     else:
#         recursion(n-1)
#         print(n)
#         recursion(n-1)
# recursion(3)



# def rec(n):
#     if n<=1:
#         return 0
#     else:
#         return 1+rec(n/2)
    
# print(rec(16))

# print(1/2)




# def fun_sum(n):
#     if n<10:
#         return 1
#     else:
        
#         return int(n%10) + fun_sum(int(n/10))
# print(fun_sum(1234))


# def powrr(a,b):
#     if b==0:
#         return 1
#     else:
#         return a*powrr(a,b-1)
# print(powrr(2,4))


# def Toh(n,source,middle,destination):
#     if n == 1:
#         print('move disk {disk}  from {source} to {destination} destination'.format(source,destination))
#     else:
#         Toh(n-1,source,middle)
        
        
        
# print(Toh(1,2,3,4))


# def rec():
#     pass


# print(rec())

 
#  
    
# def fun2(n):
#     if n<=1:
#         return 0
#     else:
#         return 1+fun2(n/2)
# fun2(5)



# s1 = "geek"
# s2 = len(s1)
# for i in range(s2-1,-1,-1):
#     print(s1[i],end="  ")

# print(s1[::-1])



# def rev(s):
#     s1 = len(s)
#     for i in range(s1-1,0 ,-1):
#         print(s[i],end=" ")

# s = input('enter string')
# rev(s)




# def facto(n):
#     if n==0:
#         return 1
#     else: 
#         return n*facto(n-1)


# print(facto(5))



# def fun(n):
#     if n==0:
#         return 
#     else:
#         fun(n-1)
#         print(n)
#     fun(n-1)
# fun(3)


# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
    
#     if count>2:
#         return False
#     else:
#         return True     
# print(prime(5))


# def prime(n,i=2):
#     if n==i:
#         return True
#     else:
#         n%i==
    


# print(prime(971))


# def fun(n):
#     if n==0:
#         return 
    
#     else:
#         print(n)
#         # fun(n-1) 
# fun(3)




# li=[1, 3, 5, 5, 5, 5, 67, 123, 125]
# count = 0
# c = len(li)
# x = 5
# for i in range(len(li)):
#     if x == li[i]:
#         print(i)
#         break
    

# li=[10,15,20,20,40,40]
# x=20
# for i in range(len(li)-1,0,-1):
#     if li[i]==x:
#         print(i)
#         break


# li = [10,20,20,20,30,30]



# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.next = None
    
#     def printlist(head):
#         current = head
#         while(current!=None):
#             print(current.key)
#             current = current.next
        
        
        
#     head = node(10)
#     head.next = node(20)
#     head.next.next = node(30)
#     printlist(head)
    
    
    
        
        
# temp1 = node(10)
# temp2 = node(20)
# temp3 = node(40)

# temp1.next = temp2
# temp2.next = temp3
# temp3.next = None
# head = temp1


# sample codes.............

# d2={'i':1,'v':5}
# for i in d2.values():
#     print(i)

# l =[1, 2, 3, 4, 5]                                                                                                                                                                                                                                                                                                            
# def rotation(l):
#     n = len(l)
#     first_element = l[0]
#     # print(n)
#     # print(first_element)
#     for i in range(1,n):
#         #print(i)
#         l[i-1]=l[i]
#     l[n-1]=first_element
#     return l

# print(rotation([1, 2, 3, 4, 5]))
    




#basic questions...........

# def pos_or_nev(n):
#     if n>0:
#         print("positive")
#     elif n<0:
#         print("negitive")
#     else:
#         print(0)
        
# pos_or_nev(-9)



# def eve_or_odd(n):
#     if n%2==0:
#         print("even")
#     elif n%2!=0:
#         print("odd")

# eve_or_odd(8)




# def sum_of_n(n):
#     c = 0
#     for i in range(0,n+1):
#         c = c+i;
#     print(c)
        
        
# sum_of_n(4)



# def greatest_of(a,b):
#     if a>b:
#         print( a,"is big")
#     else:
#         print(b,"is bigger")
            
# greatest_of(6,8)


# def prime(n):
#     count=0
#     for i in range(2,n+1):
#         if n%i==0:
#             count+=1
            
#     if count>2:
#         print("no")
#     else:
#         print("yes")
        
# prime(7)




# def digits(n):
#     sum=0
#     while(n!=0):
#         sum+= n%10
#         n = n//10
#     print(sum)
        
# digits(1234)



# def rev(n):
#     while(n!=0):
#         rem = n%10
#         n = n/10
#     print(rem)
# rev(1234) 


# li = [1,3,20,4,1,0]
# n = len(li)
# for i in range(1,n):
#     if li[i] >= li[i-1] and li[i]>=li[i+1]:
#         print(i)
         
         
# l1 = [3, 2, 1, 56, 10000, 167]
# max= l1[0]
# for i in range(0,len(l1)):
#     if l1[i]<max:
#         max = l1[i]
# print(max)
        

# l1=[1,2,3,4]
# print(l1[::-1])


# arr=[2,1,0,2,1,0]
# left = arr[0]
# right = len(arr)-1
# current = 0

# l1=[2,1,0,2,1,0]
# def swap(l1):
#     temp = l1[a]




#toh

# def tower_of_hanoi(disks, source, auxiliary, target):  
#     if(disks == 1):  
#         print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
#         return  
#     # function call itself  
    
    
    
#     tower_of_hanoi(disks - 1, source, target, auxiliary) 
     
#     print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
#     tower_of_hanoi(disks - 1, auxiliary, source, target)    
  
# disks = int(input('Enter the number of disks: '))  
# # We are referring source as A, auxiliary as B, and target as C  
# tower_of_hanoi(disks, 'A', 'B', 'C')  # Calling the function 




# def fun1(n):
#     if n==0:
#         return 
#     else:
#         fun1(n-1)
#         print(n)
#         fun1(n-1)
        
# fun1(3)
#

# def dnf_sort(arr,n):
#     low = 0
#     mid = 0
#     high = len(arr)-1
#     while(mid<=high):
#         if arr[mid]==0:
#             low,mid = mid,low
#             low+=1
#             mid+=1
            
            
#         elif arr[mid]==1:
#             mid+=1
#         elif arr[mid]==2:
#             mid,high = high,mid
#             mid+=1
#             high-=1
#     return arr
#     # return arr
# def printArray(arr):
#     for k in arr:
#         print(k)



# arr=[2,0,1]
# n = len(arr)
# r = dnf_sort(arr,n)
# c = printArray(arr)
# print(r)



# s = "8955795758"
# c=int(s)
# if c%7==0:
#     print("1")
# else:
#     print("0")


# T = int(input())

# testCases = []
# for i in range(T):
    
#     l = int(input())
#     testCase = [int(x) for x in  input().split(" ")]
#     testCases.append(testCase)

# print(testCases)



#class Node....
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.next = None
        
        

# # logic.....
# def PrintList(head):
#     current = head
#     while(current!=None):
#         print(current.key,end="->")
#         current = current.next              
        

# #driver code...
# head = Node(10)
# head.next  = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# PrintList(head)



#searching an element in an linked list..............

# class Node:
#     def __init__(self,k):
#         self.key = k 
#         self.next = None
        
        
# def Fun_Search(head,x):
#     pos = 1
#     current=head
#     while(current!=None):
#         if current.key == x:
#             return pos
#         else:
#             pos = pos+1
#             current = current.next 
#     return -1

# head = Node(10)
# head.next  = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# x = int(input("enter value"))
# print(Fun_Search(head,x))   



# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
        
# def insert_begin(head,key):
#     temp = Node(key)
#     temp.next = head 
#     return temp


# head = None 
# head = insert_begin(head,10)
# head = insert_begin(head,20)
# head = insert_begin(head,30)
# key = int(input("enter val"))
# print(insert_begin(head,key))





# class node:
#     def __init__(self,key):
#         self.key =key 
#         self.next = None
        
        
# def printList(head):
#     current = head 
#     while(current!=None):
#         print(current.key,end="->")
#         current = current.next
        
        
# def Insert_beg(head,key):
#     temp = node(key)
#     temp.next=head 
#     return temp  




# head = None
# head = Insert_beg(head,10)
# head = Insert_beg(head,20)
# head = Insert_beg(head,30)
# head = Insert_beg(head,40)
# printList(head)


# head = node(10)
# head.next = node(20)
# head.next.next = node(30)
# head.next.next.next = node(40)
# printList(head)






# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None 
        
        
# def search(head,n):
#     pos = 1
#     current = head 
#     while(current!=None):
#         if current.key == n:
#             return pos
#         pos = pos+1 
#         current = current.next
#     return -1
        

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# n = int(input("enter the element you want to search in linked list"))
# print(search(head,n))



#quick sort algorithim.
# def Quick_sort(l):
#     if len(l)<=1:
#         return l 
#     else:
#         pivot = l.pop()
#     greater=[]
#     lower = []
#     for i in l:
#         if i>=pivot:
#             greater.append(i)
#         else:
#             lower.append(i)
#     return Quick_sort(lower) + [pivot] + Quick_sort(greater)
# l=[4,90,2,0]
# print(Quick_sort(l))


# def fun1(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fun1(n-1)

# print(fun1(5))


#print 10 to 1 using recursion

# def fun2(n):
#     if n<=0:
#         return 
#     else:
#         fun2(n-1)
#         print(n)
# n=10 
# fun2(n)

#power of number using recursion 


# def power_of_number(b,p):
#     if b!=0:
#         return b*power_of_number(b,p-1)


# b=2
# p=4
# power_of_number(b,p,power_of_number(b,p)) 




# t1=("python",[10,20,30],(2,4,16))
# c=t1[1]
# d = c[1]
# print(d)



# t1=(11,[22,33,44,55])
# c = t1[1]
# c[0]=222
# #print(c[0])
# print(c)



# t1 = (7, 8, 9, 1, 10, 7)
# c=0
# for i in t1:
#     c+=i
# print(c)


#interchange first and last element in list

# l1=[1,2,3,4]
# size = len(l1)
# a = l1[0]
# b=l1[-1]
# temp = l1[0]
# l1[0]=l1[-1]
# l1[-1]=temp
# print('return after exchanging their values..........')
# print(l1)

#maximum of 2 numbers in python..............
# l1=[4,3,7,9,1,0]
# maximum=l1[0]
# for i in range(0,len(l1)):
#     if l1[i]<=maximum:
#         maximum=l1[i]
# print(maximum)

#reverse the string python

# s1 = "hellopythonandjava" 
# s2=" "
# for i in s1:
#     s2 = i+s2
#     print(s2)   
#second largest element in list 
# l1 = [9,10,20,4]
# l2 = list(set(l1))
# print(l2)
# print(l2[-3])
# maximum = l1[0]
# for i in range(0,len(l1)):
#     if l1[i]>maximum:
#         max=l1[i]
# #print(max)
# temp = max 

#python programe to copy a li






# from turtle import *
# color('red')
# begin_fill()
# pensize(5)
# setposition(0,0)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()
# penup()
# setposition(0,220)
# pendown()
# write('i love you',font=("Arial,18,normal"),align='center')
# hideturtle()
# done()


# from turtle import *
# color('red', 'black')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


# import pdb

# bike1 = 'yamaha'
# bike1_price = 90000

# bike2 = 'honda'
# bike2_price = 80000
# pdb.set_trace()

# name = input('enter name')
# print(f"hello{name}")
# choose = input('press one for bike 1 and 2 for bike 2')
# if choose ==1:
#     print("f{bike_price}bike will cst you{bike2_price}")
# elif choose==2:
#     print(bike2_price)
    



