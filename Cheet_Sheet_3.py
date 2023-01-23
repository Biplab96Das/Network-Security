#Class:Encapsulates data and functionality int it
#Data as attribute and functionality as method
#Class is ablueprint for creating concrete instance in memory
#Class can be created on the fly
class Employee():
      pass
employee=Employee()
employee.salary=122000
employee.firstname='Alice'
employee.lastname="wondarland"
print(employee.firstname+" "+employee.lastname+" earns "+str(employee.salary)+"$")
#self is the first argument in the function definition
class Dog:
	"--Blueprint of a Dog--"
	#class variable shared by all instances
	species=["Canies Lupus"]
	def __init__(self,name,color):
		self.name=name
		self.state="Sleeping"
		self.color=color
	def command(self,x):
	    if x==self.name:
	          self.bark(2)
	    elif x==("sit") :
	          self.state="sit"
	    else:
	          self.state="Wag Tail"
	def bark(self,freq):
	    for i in range(freq):
	          print("[" + self.name + "]:Waau!")



bello=Dog("bello","black")
alice=Dog("alice","white")

print(bello.color)
print(alice.color)

bello.bark(1)

alice.command("sit")
print("[alice]:"+alice.state)	     

bello.command("no")
print("[bello]:"+bello.state)

alice.command("alice")

bello.species+=["Wolf"]

print(len(bello.species)==len(alice.species))                         	
