import sys
import random
import math

sys.setrecursionlimit(1000000)

def dfs(outg,ing,start,end,path,visited):
	if(start == end):
		path.append(end)
		return 1
	if(start in visited):
		return 0
	path.append(start)
	visited.add(start)
	
	for n in outg[start]:
		capacityLeft = outg[start][n][1] - outg[start][n][0];
		if(capacityLeft > 0):
			if(dfs(outg,ing,n,end,path,visited)==1): return 1;

	for n in ing[start]:
		capacityLeft = ing[start][n][0]
		if(capacityLeft > 0):
			if(dfs(outg,ing,n,end,path,visited)==1): return 1;

	path.pop(-1)
	return 0;


def solve(data):
	outgraph={1000000:{},1000001:{}}
	ingraph={1000000:{},1000001:{}}
	
	setA = set()
	setB = set()
	for d in data:
		setA.add(d[0])
		setB.add(d[1])
		if( d[0] not in outgraph): 
			outgraph[d[0]] = {}
			ingraph[d[0]] = {}

		if( d[1] not in outgraph): 
			outgraph[d[1]] = {}
			ingraph[d[1]] = {}
		
		outgraph[d[0]][d[1]] = [0,1]
		outgraph[1000000][d[0]] = [0,1]
		outgraph[d[1]][1000001] = [0,1]

		ingraph[d[1]][d[0]] = [0,1]
		ingraph[d[0]][1000000] = [0,1]
		ingraph[1000001][d[1]] = [0,1]

	totalFlow = 0
	
	while(True):
		path = [];
		visited = set()
		# print 'x'
		if(dfs(outgraph,ingraph,1000000,1000001,path,visited) == 0 ):
			# print 'y'
			break;
		flow = 999999999999999
		for i in range(0,len(path)-1):
			st = path[i]
			ed = path[i+1]
			if(ed in outgraph[st] and outgraph[st][ed][1] - outgraph[st][ed][0] < flow) : flow = outgraph[st][ed][1] - outgraph[st][ed][0]
			if(ed in ingraph[st] and ingraph[st][ed][0] < flow) : flow = ingraph[st][ed][0]
		totalFlow += flow
		# print path
		for i in range(0,len(path)-1):
			st = path[i]
			ed = path[i+1]
			# print st,ed,outgraph
			if(ed in outgraph[st]) : 
				outgraph[st][ed][0] += flow
				ingraph[ed][st][0] += flow
			if(ed in ingraph[st]) : 
				outgraph[ed][st][0] -= flow
				ingraph[st][ed][0] -= flow
		# print path
		# print outgraph
	
	# print totalFlow
	# print outgraph
	
	return len(data) - (totalFlow + (len(setA) + len(setB) - totalFlow*2))

f = open('/Users/nik9618/Downloads/B-small-attempt1.in', 'r')
n = int(f.readline())
c = 1
for _ in range(n):
	n = int(f.readline().split("\n")[0])

	data = []
	wordL = set()
	wordR = set()
	for _ in range(n):
		l = f.readline().split("\n")[0].split(" ")
		data.append(l)
		wordL.add(l[0])
		wordR.add(l[1])
	wordL=list(wordL)
	wordR=list(wordR)
	dictL = {}
	dictR = {}
	idxL = {}
	idxR = {}
	ct =0
	for w in wordL: 
		dictL[ct]=0
		idxL[w]=ct
		ct+=1
	ct=100000
	for w in wordR:
		dictR[ct]=0
		idxR[w]=ct
		ct+=1

	dx = [];
	for d in data:
		dx.append([idxL[d[0]],idxR[d[1]]]) 

	x=solve(dx)
	print "Case #"+str(c)+":", x
	
	c+=1
	# break;
	


