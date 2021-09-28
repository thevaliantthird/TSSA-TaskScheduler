# TSSA-TaskScheduler
Task Scheduler using Simulated Annealing!


Super class TSSA:

Time table for each day : List of list!

Attributes of each task:

Dictionary : Mapping course to list of topics
Hashmap from Each topic of each course to a number!

course :

1. self.credits
2. self.consistency


work:

1. Relative Work proportion
2. 

task:
1. self.course
2. self.Topic (Code from hashmap)
3. (self.type) Reading for first time(watching lecture)/Learning/Solving/Assignment  :::: A tuple of (Watching Lec, Learning, Solving, Coding, Writing Formally)
4. Expected Time (FLOAT : HOURS)
5. Difficulty
6. Deadline (if any!)
7. Description

Time Data Type: float (30 min. multiples)

class TimeSlots

self.Day
self.exception = list of tuples of times which can't be used!

self.GenerateUseable :- List of slots which can be used!


1. Energy Function
2. Day end, task updater
3. Time slot Input from User!
4. Time Table Generation
	i. Metropolis Algorithm
	ii. Simmulated Annealing
5. ICS - file

Energy Functions Arguments : 

A list of timing slots and what could be done in those slots as a 8-member vector:
1. The watching lecture component of the work, 
2. the learning/memorizing part of the work, 
3. the problem-solving part of the work, 
4. the coding part of the work, 
5. the writing as an assignment part of the work, 
6. Difficulty
7. (Deadline - CurrTime)