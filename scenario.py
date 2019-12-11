class Scenario:

	def __init__(self, desc, consA, consB, conStrA, conStrB, myNum):
		self.desc = desc
		self.consA = consA
		self.consB = consB
		self.conStrA = conStrA
		self.conStrB = conStrB
		self.myNum = myNum
	
		
	def printDesc(self):
		for i in range(len(self.desc)):
			print(self.desc[i])
	
	def applyCons(self, num, stats):
		tempNum = 0
		for i in range(len(stats)):
			if(num == 0):
				tempNum = stats[i]+self.consA[i]
				if(tempNum < 0):
						stats[i] = 0
				elif(i == 6):
					if(tempNum > 100):
						stats[i] = 100
					else: stats[i] = tempNum
				elif(i == 4):
					if(tempNum > 4):
						stats[i] = 4
					else: stats[i] = tempNum
				else:
					if(tempNum > 10):
						stats[i] = 10
					else: stats[i] = tempNum
			else: 
				tempNum = stats[i]+self.consB[i]
				if(tempNum < 0):
					stats[i] = 0
				elif(i == 6):
					if(tempNum > 100):
						stats[i] = 100
					else: stats[i] = tempNum
				elif(i == 4):
					if(tempNum > 4):
						stats[i] = 4
					else: stats[i] = tempNum					
				else:
					if(tempNum > 10):
						stats[i] = 10
					else: stats[i] = tempNum
				
