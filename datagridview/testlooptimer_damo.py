from threading import Timer


def printHello(): 
  print ("Hello World")
  t = Timer(2, printHello) 
  t.start() 
  
  
if __name__ == "__main__": 
  printHello()
