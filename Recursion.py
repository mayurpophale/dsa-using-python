#1.sum of 1st nth natural number
# def s(n):
#     if n == 1:
#         return 1
#     else:
#         return n+s(n-1)   
# print(s(10))

#2.print first nth natural number 
# def printN(n):
#     if n > 0:
#         printN(n-1)
#         print(n,end=" ")
# printN(30)

#3.print first nth natural number in reverse order
# def printreverse(n):
#     if n > 0:
#         print(n,end=" ")
#         printreverse(n-1)
# printreverse(30)

#4.print first nth odd number 
# def printOdd(n):
#     if n > 0:
#         printOdd(n-1)
#         print(2*n - 1,end=" ")
# printOdd(10)

#5.print first nth odd number reverse order
# def printOddRev(n):
#     if n > 0:
#         print(2*n - 1,end=" ")
#         printOddRev(n-1)
# printOddRev(10)

#6.print first nth even number 
# def printEven(n):
#     if n > 0:
#         printEven(n-1)
#         print(2*n ,end=" ")
# printEven(10)

#7.print first nth even number reverse order
# def printEvenRev(n):
#     if n > 0:
#         print(2*n ,end=" ")
#         printEvenRev(n-1)
# printEvenRev(10)

# 8.sum of 1st nth odd natural number
# def sOdd(n):
#     if n == 1:
#         return 1
#     else:
#         return 2*n-1+sOdd(n-1)   
# print(sOdd(10))

#8.sum of 1st nth even natural number
# def sEven(n):
#     if n == 1:
#         return 2
#     else:
#         return 2*n+sEven(n-1)   
# print(sEven(10))

#Factorial
# def Fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*Fact(n-1)
# print(Fact(5))

#Sum of squares of 1st n natural number
def SumSq(n):
    if n == 1:
        return 1
    else:
        return n*n + SumSq(n-1)
    
print(SumSq(5))