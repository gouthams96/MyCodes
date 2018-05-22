print ("******** Multiplication Table **********")
def mult(i,n):
    return i*n

def linePrinter(i,n):
    print (str(i)+" * "+str(n)+" = "+str (mult(i,n)))
    return

number = int (input ("Number : "))

for i in range(1,11):
    linePrinter(i,number)

