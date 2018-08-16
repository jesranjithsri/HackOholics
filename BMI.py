from tkinter import *

class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.headerFont = ("Comic Sans", "16", "bold italic")
		
		self.title("BMI Calculator")
		self.setInfo()

	def setInfo(self):
		Label(self, text = "BMI Calculator",
				font = self.headerFont).grid(columnspan = 6)
        
		#get user's height
		Label(self, text = "Height (ft)").grid(row = 1, column = 0)
		self.txtHeightFt = Entry(self)
		self.txtHeightFt.grid(row = 1, column = 1)
		#using the insert function to default all fields to "0"
		self.txtHeightFt.insert(0, "0")
		
		Label(self, text = "  Height (in)").grid(row = 1, column = 3)
		self.txtHeightIn = Entry(self)
		self.txtHeightIn.grid(row = 1, column = 4)
		self.txtHeightIn.insert(0, "0")

		#get user's weight
		Label(self, text = "Weight (lbs)").grid(row = 2, column = 0)
		self.txtWeight = Entry(self)
		self.txtWeight.grid(row = 2, column = 1)
		self.txtWeight.insert(0, "0")

		#label for BMI output and status
		Label(self, text = "Your BMI:").grid(row = 5, column = 0)
		self.lblBMI = Label(self, bg = "#fff", anchor = "w", relief = "groove")
		self.lblBMI.grid(row = 5, column = 1, sticky = "we")
		Label(self, text = "You are:").grid(row = 5, column = 3)
		self.lblBMIStatus = Label(self)
		self.lblBMIStatus.grid(row = 5, column = 4)


		#button to calculate info
		self.btnCalc = Button(self, text = "Calculate BMI")
		self.btnCalc.grid(row = 10, columnspan = 5)
		self.btnCalc["command"] = self.calcBMI

			  
	def calcBMI(self):
		"""calculate the BMI of a person using the formula"""

		#calculate BMI
		feet = int(self.txtHeightFt.get())
		inches = int(self.txtHeightIn.get())
		totalHeight = (12 * feet) + inches

		weight = float(self.txtWeight.get())

		#BMI needs to be a float, int * float is float
		bmi = weight * 703 / (totalHeight * totalHeight)

		self.lblBMI["text"] = "%.2f" % bmi


		#label for BMI status

		if bmi < 18.5:
			self.lblBMIStatus["text"] = "Underweight"
		elif bmi < 24.9:
			self.lblBMIStatus["text"] = "Normal"
		elif bmi < 29.9:
			self.lblBMIStatus["text"] = "Overweight"
		else:
			self.lblBMIStatus["text"] = "Obese"


def main():
	a = App()
	a.mainloop()
	

if __name__ == "__main__":
	main()