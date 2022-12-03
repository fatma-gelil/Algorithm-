
list=[2,6,9,0,8,3,1,5,10,4,7]

x=1
while(x<10):
  element=list[x]
  i=x
  x=x+1

  while(i>0 and list[i-1]>element):
    list[i]=list[i-1]
    i=i-1

  list[i]=element

x=0
while(x<10):
  print (list[x])
  x=x+1