import random
import scenarios as s
from tkinter import *
import tkinter
from PIL import Image, ImageTk


stats = [7, 7, 7, 0, 4, 5, 80]
scenList = [s.s1, s.s2, s.s3, s.s4, s.s5, s.s6, s.s7, s.s8, s.s9, 
			s.s10, s.s11, s.s12, s.s13, s.s14, s.s15, s.s16, s.s17,
			s.s18, s.s19, s.s20, s.s21, s.s22, s.s23, s.s24, s.s25,
			s.s26, s.s27, s.s28, s.s29, s.s30]
delList = []

counter = 0

root = Tk()
root.geometry("700x700")
root.title("Health Wealth")

buttonHeight = 60
buttonWidth = 157


main_bg_img = PhotoImage(file="UI\\Main_bg.png")	
title_img = PhotoImage(file="UI\\title_bg.png")
instruc_bg_img = ImageTk.PhotoImage(Image.open("UI\\instructions.png"))
cons_img = PhotoImage(file="")

#photoBoard = ImageTk.PhotoImage(Image.open("UI\Main_bg.png").resize((700, 700), Image.ANTIALIAS))			#changed this
		
A_On = ImageTk.PhotoImage(Image.open("UI\A_on.png"))				
A_Off = ImageTk.PhotoImage(Image.open("UI\A_off.png"))			#changed this
B_On = ImageTk.PhotoImage(Image.open("UI\B_On.png"))				
B_Off = ImageTk.PhotoImage(Image.open("UI\B_Off.png"))			
Cont_Off = ImageTk.PhotoImage(Image.open("UI\cont_off.png").resize((buttonWidth, buttonHeight), Image.ANTIALIAS))
Cont_On = ImageTk.PhotoImage(Image.open("UI\cont_on.png").resize((buttonWidth, buttonHeight), Image.ANTIALIAS))
Instruc_Off = ImageTk.PhotoImage(Image.open("UI\inst_off.png").resize((buttonWidth, buttonHeight), Image.ANTIALIAS))
Instruc_On = ImageTk.PhotoImage(Image.open("UI\inst_on.png").resize((buttonWidth, buttonHeight), Image.ANTIALIAS))
Back_Off = ImageTk.PhotoImage(Image.open("UI\\back_off.png").resize((buttonWidth, buttonHeight), Image.ANTIALIAS))
Back_On = ImageTk.PhotoImage(Image.open("UI\\back_on.png").resize((buttonWidth, buttonHeight), Image.ANTIALIAS))


Start_Off = ImageTk.PhotoImage(Image.open("UI\start_off.png").resize((buttonWidth, buttonHeight), Image.ANTIALIAS))

Start_On = ImageTk.PhotoImage(Image.open("UI\start_on.png").resize((buttonWidth, buttonHeight), Image.ANTIALIAS))


scenNum = 0
aPosX=100	#changed this
aPosY=400
bPosX=450	#changed this
bPosY=400


buttonA=Button()
buttonB=Button()
buttonNext=Button()
instrucButton=Button()
instrucBack=Button()
contButton = Button()
startButton = Button()

lHealth = Label()
lRest = Label()
lRecreation = Label()
lStress = Label()
lHygiene = Label()
lIntellect = Label()
lGrades = Label()

health=StringVar()
rest=StringVar()
recreation=StringVar()
stress=StringVar()
hygiene=StringVar()
intellect=StringVar()
grades=StringVar()

mesVar = StringVar()	
consVar = StringVar()


"""
Here are our end scenarios
Skip this block if you don't want to read them
"""
heBad = "You wake up every day to your body feeling off. Neglecting your body's health has brought negative impacts as it affects your"\
		"physical and mental state. It's not too late to change the course to a better, healthier self.\n\n"
heMed = "Your health can be measured as okay, but sometimes your body feels a bit off. Although you do not feel sick, you know you"\
		"could make better health decisions to lead a healthier life.\n\n"
heGood = "You wake up smiling and ready to tackle the day! Your body thanks you for your healthy decisions, and it returns the favor"\
		"by having your cells run smoothly and steadily.\n\n"	

reBad = "You can’t live off of coffee forever. Science shows that regularly getting under 5 hours of sleep wrecks your decision making,"\
		"so make sure to prioritize sleep as it affects the rest of your body!\n\n"
reMed = "You have enough energy to wake up, but the only problem you have now is keeping that momentum going and staying up. Your energy"\
		" levels fluctuate from being rested to tired. Getting a little more rest would fix this problem.\n\n"
reGood = "The birds are singing outside as you wake up with high levels of energy. The feeling of being alert and comfortable gets you through"\
		"the day. This leaves you more time to focus on things that make you happy, rather than trying to nap throughout the day.\n\n"	

recBad = "You never have time for yourself and feel like you have no purpose sometimes. No matter how busy life gets, always make time"\
		"for yourself to prioritize what matters and makes you happy. What is life, if you never find time to live?\n\n"
recMed = "The days go by as you sometimes find time for yourself and your hobbies. You miss the days when you did stuff you actually"\
		"liked. Remember that “me” time is important and you can have a healthy balance of recreational activities in your schedule.\n\n"
recGood = "You make time for yourself and greatly benefit from this. This motivates you to better yourself in other aspects as you prioritize yourself.\n\n"

sBad = "You need to focus on relaxing more. In the end, your grades don’t matter as much as your mental state.\n"
sMed = "Your mind feels at ease sometimes, but it strays away to some thoughts that make you jittery."\
		"Making time to relax and meditate will improve your stress levels.\n\n"
sGood = "You feel content as the serotonin flows through your head with stress levels being low."\
		"This greatly affects the rest of your body as stress is one less thing to worry about.\n\n"
		
hyBad = "While not the most important aspect of health, bad hygiene will increase your chances of getting sick, while can"\
	"ruin a few days or even a week. Remember to keep clean!\n\n"
hyMed = ""
hyGood = "Your hygiene reflects the good feeling you get after showering away the troubles you had throughout the day."\
		"Feeling fresh and healthy leads to your bright smile being contagious to those around you.\n\n"
iBad = "You feel like your brain hasn’t had much activity lately. This affects your mind on many levels as simple tasks"\
		"become increasingly difficult. Remember to keep your mind busy to strengthen it!\n\n"
iMed = " You’ve been moderately keeping your brain busy by learning a few things but feel as you could improve to keep your mind sharper.\n\n"
iGood = "Keep up the good work with your mind! A sharp mind is as important as a healthy body!\n\n"

gBad = "While your health is important, you’re in college for a reason. You need to pass your classes, or else it will all be for nothing!\n\n"
gMed = "You’re well aware that grades don’t matter as much as your health in the long run! Good job.\n\n"
gGood ="While trying to balance all other aspects of your health, you were able to keep your grades up to an excellent degree! Great job!\n\n"
	
	
outcomes = [[heBad, heMed, heGood], [reBad, reMed, reGood], [recBad, recMed, recGood], 
			[sBad, sMed, sGood], [hyBad, hyMed, hyGood], [iBad, iMed, iGood], [gBad, gMed, gGood]]
			
endVar = StringVar()

def getEndString():
	endStr = ""
	for i in range(7):
		if(i == 3):
			if(stats[i] >6 ):
				endStr+=outcomes[i][0]
			elif(stats[i] > 3):
				endStr+=outcomes[i][1]
			else:
				endStr+=outcomes[i][2]
		elif(i == 4):
			if(stats[i] < 2):
				endStr+=outcomes[i][0]
			elif(stats[i] < 4):
				endStr+=outcomes[i][2]
		elif(i == 6):
			if(stats[i] < 70):
				endStr+=outcomes[i][0]
			elif(stats[i] < 90):
				endStr+=outcomes[i][1]
			else:
				endStr+=outcomes[i][2]
		else:
			if(stats[i] < 4):
				endStr+=outcomes[i][0]
			elif(stats[i] < 7):
				endStr+=outcomes[i][1]
			else:
				endStr+=outcomes[i][2]
	return endStr

"""
Instructions
"""

instrStr="THE GAME:\nPut yourself in the shoes of a college student for a week. You will be "\
 "faced with a series of scenarios about which you have to make decisions. These scenarios are "\
 "based off of real experiences.\nHOW TO PLAY:\nYou have 7 stats to keep track of: health, "\
 "rest, recreation, stress, hygiene, intellect, and your grades. These stats cannot go higher "\
 "than 10, or lower than 0. The hygiene stat in particular is capped at 4. Each decision you "\
 "make will affect some of these stats. Similar to life, you do not know the outcomes of your "\
 "decisions until you make them. Press the button (A or B) corresponding to your decision. At "\
 "the end of 5 days (or scenarios), you will be given an overview on your physical state along "\
 "with some advice. If you care to keep playing past the 5 days, close the game and reopen it. "\
 "Once you are at the start screen, if you press the “Continue” button, you will be able to keep "\
 "going with your same stats and without the scenarios you have already experienced."

main_bg = Canvas(root, width=700, height=700)
main_bg.create_image(350, 350, image=main_bg_img)	

title_bg = Canvas(root, width=700, height=700)
title_bg.create_image(350, 350, image=title_img)

instruc_bg = Canvas(root, width=700, heigh=700)
instruc_bg.create_image(350, 350, image=instruc_bg_img)


cons_bg = Canvas(root, width=700, height=700)
cons_bg.create_image(350, 350, image=cons_img)


endMess	= Message(root, justify=CENTER, textvariable=endVar, width=500, font=("", 12))

consMess = Message(root, justify=LEFT, textvariable=consVar, width=500, font=("", 12))
message = Message(root, justify=LEFT, textvariable=mesVar, width=5000, font=("",12))
instructions=Message(root, justify=CENTER, text=instrStr, width=550, font=("", 12))



			
lHealth = Label(root, textvariable=health, font=("", 12))
lRest = Label(root, textvariable=rest, font=("", 12))
lRecreation = Label(root, textvariable=recreation, font=("", 12))
lStress = Label(root, textvariable=stress, font=("", 12))
lHygiene = Label(root, textvariable=hygiene, font=("", 12))
lIntellect = Label(root, textvariable=intellect, font=("", 12))
lGrades = Label(root, textvariable=grades, font=("", 12))



def dispdateStats(chng):
	pos = "+"
	neg = "-"
	strList = ["Health", "Rest", "Recreation", "Stress", "Hygiene", "Intellect", "Grades"]
	varList = [health, rest, recreation, stress, hygiene, intellect, grades]
	for i in range(7):
		if(chng[i] != 0):
			if(chng[i] > 0):
					varList[i].set(strList[i]+" "+pos+" "+str(chng[i])+": "+str(stats[i]))
			else: varList[i].set(strList[i]+" "+neg+" "+str(abs(chng[i]))+": "+str(stats[i]))
		else: varList[i].set(strList[i]+": "+str(stats[i]))

	lHealth.place(x=300, y=350)
	lRest.place(x=300, y=375)
	lRecreation.place(x=300, y=400)
	lStress.place(x=300, y=425)
	lHygiene.place(x=300, y=450)
	lIntellect.place(x=300, y=475)
	lGrades.place(x=300, y=500)
	
def removeStats():
	lHealth.place_forget()
	lRest.place_forget()
	lRecreation.place_forget()
	lStress.place_forget()
	lHygiene.place_forget()
	lIntellect.place_forget()
	lGrades.place_forget()
	

def bpCont():
	global delList
	global stats
	with open("do_not_delete.txt") as f:
		results = f.read().splitlines()
	if(len(results) != 0):	
		results = list(map(int, results))
		for i in range(7):
			stats[i] = results[i]
		for i in range(8, len(results)):
			delList.append(results[i])
			del scenList[results[i]-1]
	start()

def bpA():
	global scenNum
	scenList[scenNum].applyCons(0, stats)
	consVar.set(scenList[scenNum].conStrA)
	delList.append(scenList[scenNum].myNum)
	dispdateStats(scenList[scenNum].consA)
	del scenList[scenNum]
	buttonA.place_forget()
	buttonB.place_forget()
	message.place_forget()
	main_bg.place_forget()
	consMess.place(x=100, y=50)
	buttonNext.place(x=275, y=525)
	instruc_bg.place(x=0, y=0)
	

def bpB():
	global scenNum
	scenList[scenNum].applyCons(1, stats)
	consVar.set(scenList[scenNum].conStrB)
	delList.append(scenList[scenNum].myNum)
	dispdateStats(scenList[scenNum].consB)
	del scenList[scenNum]

	buttonA.place_forget()
	buttonB.place_forget()
	message.place_forget()
	main_bg.place_forget()
	consMess.place(x=100, y=50)
	#cons_bg.place(x=0, y=0)
	buttonNext.place(x=275, y=525)
	instruc_bg.place(x=0, y=0)
	
def bpNext():
	removeStats()
	consMess.place_forget()
	cons_bg.place_forget()
	global scenNum
	global counter

	if(counter<4):
		scenNum = random.randint(0, len(scenList)-1)
		scenList[scenNum]=scenList[scenNum]
		mesVar.set(scenList[scenNum].desc)
		buttonA.place(x=aPosX, y=aPosY)
		buttonB.place(x=bPosX, y=bPosY)
		message.place(x=75, y=150)
		buttonNext.place_forget()
		instruc_bg.place_forget()
		main_bg.place(x=0, y=0)
		counter+=1
	else:
		endVar.set(getEndString())
		endMess.place(x=100, y=50)
		buttonNext.place_forget()
		#instruc_bg.place(x=0, y=0)
		f = open("do_not_delete.txt", "w")
		for i in range(len(stats)):
			f.write(str(stats[i])+"\n")
		for i in range(len(delList)):
			f.write(str(delList[i])+"\n")
		f.close()

	
	
def bpInstr():
	instrucBack.place(x=260, y=500)
	instrucButton.place_forget()
	startButton.place_forget()
	contButton.place_forget()
	instructions.place(x=75, y=15)
	instruc_bg.place(x=0, y=0)
	
#Back on the button game 
def bpBack():
	instrucBack.place_forget()
	instructions.place_forget()
	instruc_bg.place_forget()
	title_bg.place(x=0, y=0)
	startButton.place(x=250, y=400)
	instrucButton.place(x=250, y=475)
	contButton.place(x=250, y=550)
	
#Start button press
def start():
	global scenNum
	scenNum = random.randint(0, len(scenList)-1)
	
	buttonA.place(x=aPosX, y=aPosY)
	buttonB.place(x=bPosX, y=bPosY)
	mesVar.set(scenList[scenNum].desc)
	message.place(x=75, y=150)
	startButton.place_forget()
	instrucButton.place_forget()
	contButton.place_forget()
	title_bg.place_forget()
	main_bg.place(x=0, y=0)
	
	
	

	
#Changing button presses
def on_enterA(e):
		buttonA['image'] = A_On
def on_leaveA(e):
		buttonA['image'] = A_Off
		
def on_enterB(e):
		buttonB['image'] = B_On
def on_leaveB(e):
		buttonB['image'] = B_Off
		
def on_enterCont(e):
		contButton['image'] = Cont_On
def on_leaveCont(e):
		contButton['image'] = Cont_Off
		
def on_enterNext(e):
		buttonNext['image'] = Cont_On
def on_leaveNext(e):
		buttonNext['image'] = Cont_Off
		
def on_enterStart(e):
		startButton['image'] = Start_On
def on_leaveStart(e):
		startButton['image'] = Start_Off
		
def on_enterInst(e):
		instrucButton['image'] = Instruc_On
def on_leaveInst(e):
		instrucButton['image'] = Instruc_Off
		
def on_enterBack(e):
		instrucBack['image'] = Back_On
def on_leaveBack(e):
		instrucBack['image'] = Back_Off
		


buttonA = Button(root, image=A_Off, command=bpA, height=250, width=190)
buttonB = Button(root, image=B_Off, command=bpB, height=250, width=200)	#changed this 
buttonNext=Button(root, image=Cont_Off, text="Continue", font=("", 20), command=bpNext)	
startButton = Button(root, image=Start_Off, text="Begin Game", width=buttonWidth, height=buttonHeight, command=start)
instrucButton=Button(root, image=Instruc_Off, text="Instructions", font=("",22), command=bpInstr)
instrucBack=Button(root, image=Back_Off, text="Back", font=("", 20), command=bpBack)
contButton = Button(root, image=Cont_Off, text = "Continue", font=("", 20), command=bpCont)

#these are also necessary for button hovering
buttonA.bind("<Enter>", on_enterA)
buttonA.bind("<Leave>", on_leaveA)
buttonB.bind("<Enter>", on_enterB)
buttonB.bind("<Leave>", on_leaveB)
buttonNext.bind("<Enter>", on_enterCont)
buttonNext.bind("<Leave>", on_leaveCont)
startButton.bind("<Enter>", on_enterStart)
startButton.bind("<Leave>", on_leaveStart)
contButton.bind("<Enter>", on_enterCont)
contButton.bind("<Leave>", on_leaveCont)
buttonNext.bind("<Enter>", on_enterNext)
buttonNext.bind("<Leave>", on_leaveNext)
instrucButton.bind("<Enter>", on_enterInst)
instrucButton.bind("<Leave>", on_leaveInst)
instrucBack.bind("<Enter>", on_enterBack)
instrucBack.bind("<Leave>", on_leaveBack)




#startMessage = Message(root, text="Serious Game", font=("", 40), width=500)




if __name__ == '__main__':
	#health, rest, recreation, stress, hygiene, intellect, grades
	startButton.place(x=250, y=400)
	instrucButton.place(x=250, y=475)
	contButton.place(x=250, y=550)
	title_bg.place(x=0, y=0)
	root.mainloop()
