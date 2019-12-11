from scenario import Scenario
#health, rest, recreation, stress, hygiene, intellect, grades



s1 = Scenario(
			"You have a migraine! Unfortunately, you also have homework due tonight.\n"\
			"Do you:\n"\
			"A. Spend the day in bed to recover and hope the teacher gives you an extension\n"\
			"OR\n"\
			"B. Work through the pain and get your assignment done on time?",
			[0, 2, 0, 0, 0, 0, -5], [-1, 0, 0, 1, 0, 0, 5],
			"You get an extension and finish the work later!\n You feel better, and the time you "\
			"spent in bed has invigorated you.",
			"You finish your homework on time, you're utterly miserable.", 1
			)


s2 = Scenario(
			"You woke up late!\n"\
			"Do you:\n"\
			"A. Skip breakfast and go to class\n"\
			"OR\n"\
			"B. Arrive a few minutes late but arrive with a full stomach?", 
			[-1, 0, 0, 0, 0, -1, 0], [1, 0, 0, 0, 0, 0, 0],
			"You get to class but you can't pay attention because you're focused on how "\
			"hungry you are.",
			"You arrive to class 10 minutes late, but you didn't miss anything important "\
			"and now you're ready to focus for the rest of the day.", 2)
			
s3 = Scenario(
			"Time for dinner! You're running short on time due to english homework\n"\
			"Do you:\n"\
			"A. Take the time to prepare a healthy meal\n"\
			"OR\n"\
			"B. Quickly grab fast food and get back to work?",
			[1, 0, 0, 0, 0, 0, 5], [-1, 0, 0, 0, 0, 0, 5],
			"You prepare some grilled chicken and a salad, and turn your homework in "\
			"5 minutes late with no penalty.",
			"You grab a burger and fries and keep working.", 3)

s4 = Scenario(
			"You're overwhelmed with a coding project\n"\
			"Do you:\n"\
			"A. Pull an all-nighter to get it done on time\n"\
			"OR\n"\
			"B. Take a hit to your grade by prioritizing your health and sanity?",
			[-1, -3, -1, 1, 0, 0, 5], [0, 1, 0, 0, 0, 0, -5],
			"You work all night and get the project done, but now"\
			" you're exhausted and stressed out.",
			"You turn the project in late for a reduced grade"
			" but get a decent amount of sleep.", 4)
		
s5 = Scenario(
			"You've got a presentation tomorrow which you haven't started yet.\n"\
			"Do you:\n"\
			"A. Work through the night\n"\
			"OR\n"\
			"B. Put in less effort into the presentation and hope it goes alright?",
			[-1, -1, 0, 0, 0, 0, -15], [0, 0, 0, 0, 0, 0, -5],
			"You put a ton of effort into your presentation and finished a few hours"\
			" early, but now you're exhausted! You decided to take a quick nap...and"\
			" now you've slept through your presentation. You get partial credit for"\
			" turning in the powerpoint.",
			"You weren't able to do all the work you wanted, but you showed up on time"\
			" and put in effort. You get a B.", 5)

s6 = Scenario(
			"You've had a stressful past few days, but you've still got work to do.\n"\
			"Do you:\n"\
			"A. Use the day to relax\n"\
			"OR\n"\
			"B. Keep on working?",
			[0, 0, 1, 1, 0, -1, 0], [0, 0, -2, -1, 0, 1, 0],
			"You're invigorated to keep working after the day off.",
			"You feel a sense of relief as you no longer have to worry about homework "\
			"but you’re dying for a break.", 6)


s7 = Scenario(
			"It's been days since you showered, but you need every bit of time to finish\n"\
			" a major project in your class.\n"\
			"A. Take 30 minutes to shower\n"\
			"OR\n"\
			"B. Keep working?",
			[1, 0, 0, 0, 1, 0, -5], [-1, 0, 0, 0, -2, 0, 5],
			"You’re refreshed and clean, but you are a few minutes late turning it in.",
			"You finish on time, but you are repulsive to anyone around you.", 7)
			
#health, rest, recreation, stress, hygiene, intellect, grades	
s8 = Scenario(
			"An assignment is late. Every hour you don’t work on it you’re losing\n"\
			"points. You also didn’t sleep last night trying to get it done.\n"\
			"Do you:\n"\
			"A. Take a break and lose a large number of points on the project\n"\
			"OR\n"\
			"B. Keep working to minimize loses?",
			[0, 1, 1, 0, 0, 0, -10],[0, -1, -1, 0, 0, 0, -5],
			"You take a break and regain some sanity.",
			"You keep working, but you're exhausted now.", 8)

s9 = Scenario(
			"Exercise is important, but it takes time to get a meaningful workout in!\n"\
			"Do you:\n"\
			"A. Put off your work and relaxing in order to workout and shower\n"\
			"OR\n"\
			"B. Do it another day and work on homework so you can relax later?",
			[2, 0, -1, 0, 1, 1, 0], [-2, 0, 1, 0, 0, 0, 5],
			"You go run for an hour and shower. You're now healthy, clean, and ready to learn.",
			"You stayed inside and worked on homework, finishing it early "\
			"for a bonus AND you have time to relax.", 9)
			
			
s10 = Scenario(
			"It’s finals week. You have 3 exams and a project due in the\n"\
			"next four days. You’re on the verge of a C in one of your classes.\n"\
			"You’ve been studying the past few days, but you still feel unprepared.\n"\
			"Your friends have already finished and invite you to come hang out with\n"\
			"them for a few hours.\n"\
			"Do you:\n"\
			"A. Continue studying\n"\
			"OR\n"\
			"B. Relax a bit with your friends?",
			[0, 0, -1, 1, 0, 1, 0], [0, 1, 2, -1, 0, 0, 0],
			"As a result of all your hard work, you get a marginally better grade on your finals, "\
			"but your letter grades didn’t change.",
			"You have a wonderful bonding experience with your friends, making memories which will "\
			"last for years to come. You get marginally worse grades on your finals, but your letter "\
			"grades didn’t change.", 10)

s11 = Scenario(
			"In a pleasant change of pace, you have all your work done on time!\n"\
			"Do you:\n"\
			"A. Spend all of your precious free time relaxing and eating fast food\n"\
			"OR\n"\
			"B. Take some time to workout, shower, eat responsibly, and then relax?",
			[-2, 0, 2, 0,-1, 0, 0], [2, 0, 1, 0, 1, 0, 0],
			"You get a pizza, watch TV, and never leave the couch",
			"You shower, prepare a healthy meal, and relax for a shorter period of time", 11)


s12 = Scenario(
			"Oh no! You’ve caught a cold. It’s 40 degrees outside, but you’ve still\n"\
			"have class. You aren’t well enough to bike, and you didn’t pay \n"\
			"to be able to park, so you can't drive."
			"Do you:\n"\
			"A. Suck it up and walk to class\n"\
			"OR\n"\
			"B. Stay home and treat your cold\n",
			[-3, -1, 0, 1, -1, 1, 0], [0, 2, 0, -1, -1, -1, 0],
			"You made it to class, and you’re all caught up on lectures, but your cold won’t "\
			"go away any time soon.",
			"While you may have missed the lecture, you can probably get notes from a friend, "
			"and your teacher will understand.", 12)

s13 = Scenario(
			"(Ring, ring) Your phone is going off and notice it’s your family. They\n"\
			"usually help you calm down stress and brighten up your day, but you\n"\
			"are also busy playing your favorite game since you haven’t had time\n"\
			"to relax. Your family phone call also takes about an hour.\n"\
			"Do you:\n"\
			"A. Answer your family’s phone call\n"\
			"OR\n"\
			"B. Continue playing the game?\n",
			[2, 0, 2, -2, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0],
			"You vent to your family about your stressful days and they give you advice on what "
			"to do that surprisingly helps. You also catch up and feel the warmth of your family making "\
			"you happier than usual.",
			"You continue playing the game and make some progress feel somewhat accomplished.", 13)
	
	
s14 = Scenario(
			"The day has come when your hardest class has its online quiz. You didn’t\n"\
			"get enough time to study the material, but your classmate tells you that\n"\
			"there’s a quizlet with all the answers.\n"\
			"Do you:\n"\
			"A. Cheat and use the quizlet\n"\
			"OR\n"\
			"B. Take the quiz with the knowledge you know?",
			[0, 0, 0, 2, 0, -2, 5], [0, 0, 0, -1, 0, 1, -5],
			"You cheated and completed the quiz with a 100%. Although you did well on the quiz, your guilt and "\
			"stress of your professor finding out fills your mind.",
			"You decided on taking the quiz with your own knowledge, resulting in getting a 60%. You feel like you "\
			"tried your best with the knowledge you had and feel confident about getting your grade up soon.", 14)
	
s15 = Scenario(
			"It’s finally one of those days, and you get to relax at home. With the day \n"\
			"off, you think of some stuff to do.\n"\
			"Do you:\n"\
			"A. Sleep and catch up on rest\n"\
			"OR\n"\
			"B. Stay up binge watching TV while eating junk food?",
			[1, 2, 0, 0, 0, 0, 0], [-1, -2, 2, 0, 0, 0, 0],
			"Recharging yourself feels great in the morning as you’re ready to tackle the day.",
			"You finished a whole series, but feel exhausted and sick in your stomach the next morning.", 15
			)		
			

s16 = Scenario(
			"Finally, it’s Thanksgiving break. You’re exhausted, but are really looking\n"\
			"forward to spending time with your family. You decide to take one last look\n"\
			"at your emails before you disconnect for the break, and notice an email\n"\
			"from you teacher telling you that your big end-of-the-year project is due\n"\
			"this week instead of next!\n"\
			"Do you:\n"\
			"A.Spend time with your family \n"\
			"OR\n"\
			"B.Spend time working on the project?\n",
			[2, 0, 1, 0, 0, 0, -5], [-1, -2, 0, 0, 0, 0, 5],
			"You take the late penalty, but end up spending quality time with your family "\
			"and make wonderful memories. You feel refreshed!",
			"You decide to spend the break working on your project. You successfully get it "\
			"finished, but you didn’t rest or spend time with your family.", 16
			)
			

s17 = Scenario(
			"It’s the night before a big project is due, and your computer is giving you\n"\
			"problems! You are almost done though, and are making final tweaks before\n"\
			"turning it in and getting some much needed rest for the night. Unfortunately,\n"\
			"your computer crashes and you lose all of your work!\n"\
			"Do you:\n"\
			"A.Email your teacher and tell them what happened\n"\
			"OR\n"\
			"B.Pull an all nighter to start over on your project?\n",
			[1, 1, 0, 0, 0, 0, -5], [0, -2, 0, 0, 0, 1, 0],
			"You email your teacher and go to bed. The next day you get a reply. They are completely "\
			"understanding, but still acknowledge that you had more than a month to work on it.",
			"Since you already did the project the first time, doing it a second time was a lot easier. "\
			"You replicate your lost project, and turn it in on time, but you are exhausted and stumble "\
			"when presenting the project.", 17
			)
			
s18 = Scenario(
			"Class starts in an hour but it’s pouring! You haven’t missed a class yet, and\n"\
			"your teacher doesn’t take attendance.\n"\
			"Do you:\n"\
			"A. Brave the rain and make it to class\n"
			"OR\n"\
			"B.Stay home?",
			[0, 0, 0, -1, -1, 2, 0], [0, 0, 0, 2, 0, 0, -5],
			"You make it to class on time, but you fall in a puddle while walking. Your clothes "\
			"are muddy and soaked, and your backpack and its belongings are equally as soggy. "\
			"Nothing spectacular happened in class.",
			"You decide to stay up and catch up on some work, but your friend texts you asking you "\
			"“where you were today!” You find out that your teacher gave a surprise quiz, and you "\
			"made a 0 on it.", 18
			)

s19 = Scenario(
			"You walk out to your car to drive to class, but you notice that your car \n"\
			"has a flat! Class starts in 30 minutes!\n"\
			"Do you:\n"\
			"A.Email your teacher, and get the flat fixed\n"\
			"OR\n"\
			"B.Run to school?",
			[1, 0, 0, -2, 0, 0, 0], [0, -1, 0, 3, 0, 0, 0],
			"You email your teacher that you won’t make it to class today because you have to deal\n"\
			"with your flat tire. They are understanding, but you forgot you had a quiz today!\n"\
			"Luckily, your teacher will let you make up the quiz, and your tire is under warranty\n"\
			"so it is replaced for free!",
			"You end up going to class anyways, leaving the tire flat without pumping it "\
			"up. You procrastinate on getting the tire fixed, forget about it for a few "\
			"months, until one day you forget about it and go for a drive. The tire ends "\
			"up shredding and your rim bends. You end up needing to call a tow truck.", 19
			)
	
s20 = Scenario(	
			"Bing! Your gas light comes on, indicating that you are low on gas. Class\n"\
			"starts in 20 minutes, and you think you can make it to class with the \n"\
			"amount of gas that you have.\n"\
			"Do you:\n"\
			"A.Don’t stop for gas and go to class\n"\
			"OR\n"\
			"B.Stop at the closest gas station to fill your car up?",
			[0, 0, 0, 2, 0, -1, 0], [0, 0, 0, -1, 0, 2, 0],
			"You are 5 minutes away from your parking garage, but your car runs out of gas. "\
			"You end up missing class, waiting for one of your friends to come and bring "\
			"enough gas in a gas can to get you go the gas station you passed on the way "\
			"there.",
			"You stop to get gas, and are 5 minutes late to class. Everything ends up being "\
			"fine, since the teacher was also late.", 20
			)
	
s21 = Scenario(
			"Movie night! You and your friends plan to see a movie tonight, but there are\n"\
			"only two movies you all have not seen. You have the deciding vote.\n"\
			"Do you pick:\n"\
			"A. The horror movie “The Dead With In”\n"\
			"OR\n"\
			"B. The comedy “Garbage day”?",
			[0, 0, 2, 1, 0, 0, 0], [0, 1, -1, 0, 0, 0, 0],
			"You get freaked out by some of the monsters in the movie, but ultimately had "\
			"a good time with your friends.",
			"The movie was not really funny and you fell asleep. You and your friends go "\
			"home feeling like you all wasted the night.", 21
			)	
	
s22 = Scenario(
			"Family is visiting? Your uncle, who you don’t get to see very often, will be\n"\
			"in town for a few hours, but you have class when he arrives.\n"\
			"Do you:\n"\
			"A. Skip class and spend all the time you can with him\n"\
			"OR\n"\
			"B. Finish class and spend what little time you have left?\n",
			[2, 0, 0, 2, 0, 0, 0], [0, 0, 0, -1, 0, 2, 0],
			"You and your uncle spend your time having a lovely meal at your favorite "\
			"restaurant, but you feel as if you are missing an important lesson the "\
			"whole time.",
			"You learn about some interesting topics and class end a little early. You "\
			"spend the time you have with your uncle chatting about your interesting lesson.", 22
			)
			
s23 = Scenario(
			"New Game! The next big game in a franchise you love releases tomorrow, but\n"\
			"your wallet is a little low on funds.\n"\
			"Do you:\n"
			"A. Wait until you have more money to spend\n"\
			"OR\n"\
			"B. Buy the game and budget more after?",
			[0, 0, -1, -1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0],
			"You decide to save up money for the game later down the line and prioritize "\
			"other necessities.",
			"You buy the game and enjoy it, but you scrape by for the next two weeks.", 23
			)
			
s24 = Scenario(
			"Where are you Bingo? Your dog ran away and you want to find her, but you have\n"\
			"a project that is due tomorrow.\n"\
			"Do you:\n"\
			"A. Spend your day looking for your dog\n"\
			"OR\n"\
			"B. Hope he comes home and work on your project?\n",
			[0, 0, 0, -1, 0, 0, -5], [0, 0, 0, 2, 0, 0, 5],
			"You spend hours searching the neighborhood and are relieved to find her. "\
			"Once you get home you are too exhausted to work on you project.",
			"You finish your project, but can’t worry about your dog the whole time.", 24
			)

s25 = Scenario(
			"Lazy Tuesday? It is Tuesday and you have all of your assignments completed.\n"\
			"You are not sure if you should take the day for yourself or study for an]n"\
			"exam that is in a few weeks.\n"\
			"Do you:\n"\
			"A. Study\n"\
			"OR\n"\
			"B. Relax",
			[0, 0, 0, -1, 0, 1, 5], [0, 1, 1, -1, 0, 0, 0],
			"You study for a future exam and feel confident that you will do good on it.",
			"You feel super relaxed and rested ready to tackle what comes next.", 25
			)

s26 = Scenario(
			"Some friends you have not seen since last year stop by and ask if you wanna\n"\
			"play some games you used to play together for old times sake.\n"\
			"Do you:\n"\
			"A. Finish up that last bit of homework\n"\
			"OR\n"\
			"B. Spend the night playing with friends?",
			[0, 0, 0, -1, 0, 0, 5], [0, 0, 0, 1, 0, 0, -5],
			"You get that homework done, and feel at ease knowing your are entering the "\
			"week on top of your workload.",
			"You spend your time having the night of your life playing minecraft with your "\
			"old buds, you didn't get that homework done though.", 26
			)

s27 = Scenario(
			"A friend invites you to go out and ride your bikes to see all your campus has\n"\
			"to offer.\n"
			"Do you:\n"\
			"A. Go out for a ride and find some new places to eat.\n"\
			"OR\n"\
			"B. Say no and go relax on your own.",
			[0, 0, 1, 1, 0, 0, 0], [0, 0, -1, -1, 0, 0, 0],
			"You go out and burn off some calories, but you also fall over on your bike "\
			"and get a nasty scrape on your leg. You now have to fit in time to go get "\
			"it checked out at the doctor.",
			"You spend the night just chilling on your favorite couch, in cozy clothing, "
			"while taking pleasure in watching your favorite show.", 27
			)

s28 = Scenario(
			"The Wifi goes out at around 11:30 pm. You have your paper all finished\n"\
			"and you need to turn it in; however, the nearest place that would\n"
			"be open and have Wifi is a 30 minute walk away.\n"\
			"Do you:\n"\
			"A. Suck it up, put on your slides and run to that place.\n"\
			"OR\n"\
			"B. Admit the world is going to end, tell yourself you'll\n"\
			"email your teacher in the morning and sleep.",
			[0, -1, 0, -1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0],
			"You set out at a brisk pace, you manage to make it and turn in your paper; "\
			"however, the adrenaline rush makes you unable to sleep.",
			"You fall into your bed as the exhaustion from the day settles down. You have "\
			"the best sleep you have had in awhile, but you can't seem to get a hold of "\
			"your professor.", 28
			)


s29 = Scenario(
			"Its lunch time, but the food court that you wanted to go to is full of people.\n"
			"It would easily be a 30 minute wait, and you don't want to miss out on \n"\
			"studying time.\n"\
			"Do you:\n"\
			"A. Stand your ground and wait in line, getting the best lunch you have had in\n"\
			"awhile.\n"\
			"OR\n"\
			"B. Skip the food, and go back to studying, a short break was all you needed?",
			[1, 0, 0, 0, 0, 1, 0], [-1, 0, 0, 0, 0, 1, 0],
			"You have a grand time indulging in your favorite food with friends, but you "\
			"miss out on that studying time.",
			"You study some more for that test you have in an hour and power through the hunger.", 29
			)

s30 = Scenario(
			"You are done with your work for today.\n"\
			"Do you:\n"\
			"A. Spend the rest of your day taking a fat nap because you earned it.\n"\
			"OR\n"\
			"B. Start looking ahead at future chapters, because you are a good student?",
			[0, 1, 0, 0, 0, -1, 0], [0, -1, 0, 0, 0, 1, 0],
			"You sleep the night away and feel at ease.",
			"You spend the day getting ahead of things because the professors are not "\
			"gonna pull a fast one on you.", 30
			)