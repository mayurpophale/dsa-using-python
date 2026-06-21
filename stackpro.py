#operation = ["1","2","+","C","5","D"]
#stack = []
#for i in operation:
#   if i == "C":
#       stack.pop()
#   elif i  == "D":
#       stack.append( 2 * stack[-1])
#   elif i == "+":
#       stack.append(stack[-1]+stack[-2])
#   else:
#       stack.append(int(i))
#print(sum(stack))

s = "acb42"
stack = []
for i in s:
    if i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] :
        stack.append(i)
    else:
        stack.pop()
print(stack)
