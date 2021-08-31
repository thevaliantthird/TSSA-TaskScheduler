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


task:
1. self.course
2. self.Topic (Code from hashmap)
3. (ENUM) (self.type) Reading for first time(watching lecture)/Learning/Solving/Assignment
4. Expected Time (FLOAT : HOURS)
5. Difficulty
6. Deadline (if any!)

Time Data Type: float (30 min. multiples)

class TimeSlots

self.Day
self.exception = list of tuples of times which can't be used!

self.GenerateUseable :- List of slots which can be used!


1) Energy Function
2) Day end, task updater
3) Time slot Input from User!
3) Time Table Generation
	i) Metropolis Algorithm
	ii) Simmulated Annealing
4) ICS - file

