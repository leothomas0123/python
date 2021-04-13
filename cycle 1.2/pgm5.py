string=input("Enter a string:")
word=list(string)
ch=string[0]
length=len(string)
for i in range(1,length):
 if(word[i]==ch):
  word[i]='$'
print(word)


