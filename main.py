from os import system
system('clear')

with open (file='read.txt', mode='r') as readfile:
           content=readfile.read()
  print(content)
