#!/usr/bin/env python


import sys
import random


def compute_average(l): return sum(l)/float(len(l))

def compute_variance(l):
	average = compute_average(l)
	sq_diffs = [(i-average)**2 for i in l]
	return sum(sq_diffs)/float(len(l))

def improve(all, Horses, iterations):
	start_var = compute_variance([sum([Horses.get(h) for h in group]) for group in all])
	counter = 0
	while counter < iterations:
		# select two groups at random, select one horse from each group and switch. see if variance improves.
		new_all = [group[:] for group in all]
		random.shuffle(new_all)
		group1, group2 = new_all[0], new_all[1]
		random.shuffle(group1)
		random.shuffle(group2)
		horse1, horse2 = group1[0], group2[0]
		group1.remove(horse1)
		group2.remove(horse2)
		group1.append(horse2)
		group2.append(horse1)
		new_var = compute_variance([sum([Horses.get(h) for h in group]) for group in new_all])
		if new_var < start_var:
			print "Improvement found: new_var = ", new_var
			all = [group[:] for group in new_all] 
			start_var = new_var
		counter += 1
	return all

with open(sys.argv[1]) as f:
	lines = f.readlines()

lines = [line.decode('UTF-8') for line in lines if not "(Scratched)" in line]

Horses = {}
for line in lines:
	horse = line.split(': ')[0]
	odds = line.split(': ')[1].strip('\n').split('-')
	prob = float(odds[1])/(float(odds[0])+float(odds[1]))
	Horses[horse] = prob

for horse in sorted(Horses, key=Horses.get, reverse=True):
	print horse, Horses.get(horse)
print

all = [[], [], [], [], [], [], []]

for horse in sorted(Horses, key=Horses.get, reverse=True):
	current_totals = [sum([Horses.get(h) for h in i]) for i in all]
	i = current_totals.index(min(current_totals))	
	all[i].append(horse)

for group in all:
	for horse in group:
		print horse, Horses.get(horse)
	print sum([Horses.get(h) for h in group])
	print

print "Average Implied Probability:", compute_average([sum([Horses.get(h) for h in group]) for group in all])
print "Variance:", compute_variance([sum([Horses.get(h) for h in group]) for group in all])
print
print "Optimizing..."

all = improve(all, Horses, 100000)

print
for group in all:
	for horse in group:
		print horse, Horses.get(horse)
	print sum([Horses.get(h) for h in group])
	print
print "Average Implied Probability:", compute_average([sum([Horses.get(h) for h in group]) for group in all])
print "Variance:", compute_variance([sum([Horses.get(h) for h in group]) for group in all])
