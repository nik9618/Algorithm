import math

def calcScore(s1,s2):
	# print s1,s2
	a1 =""
	a2 =""
	for i in range(len(s1)):
		if(s1[i]!='?' and s2[i]!='?'):
			a1+=s1[i];
			a2+=s2[i];
			# print a1,a2
			if(s1[i]>s2[i]):
				for j in range(i+1,len(s1)):
					if(s1[j] =='?'):
						a1+='0'
					else:
						a1+=s1[j]

					if(s2[j] =='?'):
						a2+='9'
					else:
						a2+=s2[j]
				break;
			if(s1[i]<s2[i]):
				for j in range(i+1,len(s1)):
					if(s1[j] =='?'):
						a1+='9'
					else:
						a1+=s1[j]

					if(s2[j] =='?'):
						a2+='0'
					else:
						a2+=s2[j]
				break;

	if(int(a1)>int(a2)): return (int(a1)-int(a2),a1,a2)
	return (int(a2)-int(a1),a1,a2)


def solve(s1,s2):
	ans1='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
	ans2='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
	diff = 9999999999999999999999999999
	for i in range(len(s1)):
		# print s1,s2
		if(s1[i] == '?' and s2[i] == '?'):
			
			s1[i] = '0'
			s2[i] = '1'
			(sc,a1,a2) = calcScore(s1,s2)
			
			if(sc<=diff):
				if(sc<diff or a1<ans1 or (a1==ans1 and a2<ans2)):
					ans1=a1
					ans2=a2
					diff=sc

			s1[i] = '1'
			s2[i] = '0'
			(sc,a1,a2) = calcScore(s1,s2)
			
			if(sc<=diff):
				if(sc<diff or a1<ans1 or (a1==ans1 and a2<ans2)):
					ans1=a1
					ans2=a2
					diff=sc

			s1[i] = '0'
			s2[i] = '0'
			continue;

		if(s1[i] == '?' and s2[i] != '?'):
			if(s2[i]>='1'):
				s1[i] = chr((int(s2[i])-1)+48)
				(sc,a1,a2) = calcScore(s1,s2)
				if(sc<=diff):
					if(sc<diff or a1<ans1 or (a1==ans1 and a2<ans2)):
						ans1=a1
						ans2=a2
						diff=sc

			if(s2[i]<='8'):
				s1[i] = chr((int(s2[i])+1)+48)
				(sc,a1,a2) = calcScore(s1,s2)
				if(sc<=diff):
					if(sc<diff or a1<ans1 or (a1==ans1 and a2<ans2)):
						ans1=a1
						ans2=a2
						diff=sc

			s1[i] = s2[i]
			continue;

		if(s2[i] == '?' and s1[i] != '?'):
			if(s1[i]>='1'):
				s2[i] = chr((int(s1[i])-1)+48)
				
				(sc,a1,a2) = calcScore(s1,s2)
				if(sc<=diff):
					if(sc<diff or a1<ans1 or (a1==ans1 and a2<ans2)):
						ans1=a1
						ans2=a2
						diff=sc

			if(s1[i]<='8'):
				s2[i] = chr((int(s1[i])+1)+48)
				(sc,a1,a2) = calcScore(s1,s2)
				if(sc<=diff):
					if(sc<diff or a1<ans1 or (a1==ans1 and a2<ans2)):
						ans1=a1
						ans2=a2
						diff=sc

			s2[i] = s1[i]
			continue;

		if(s1[i] == s2[i]):
			continue;
		else:
			(sc,a1,a2) = calcScore(s1,s2)
			if(sc<=diff):
				if(sc<diff or a1<ans1 or (a1==ans1 and a2<ans2)):
					ans1=a1
					ans2=a2
					diff=sc
			break;

	if(i==len(s1)-1):
		(sc,a1,a2) = calcScore(s1,s2)
		if(sc<=diff):
			if(sc<diff or a1<ans1 or (a1==ans1 and a2<ans2)):
				ans1=a1
				ans2=a2
				diff=sc

	return (ans1,ans2)

# 1?999
# 2?000

f = open('/Users/nik9618/Downloads/B-small-attempt1.in', 'r')
n = int(f.readline())
c = 1
for _ in range(n):
	s = f.readline().split("\n")[0].split(" ")
	str1 = s[0]
	str2 = s[1]
	
	x1 = ['0']
	for x in str1:
		x1.append(x);
	x2 = ['0']
	for x in str2:
		x2.append(x);

	# print x1,x2
	(x1,x2) = solve(x1,x2)
	
	print "Case #"+str(c)+":",
	a1 = ''
	for i in x1:
		a1+=str(i)
	print a1[1:],
	a1 = ''
	for i in x2:
		a1+=str(i)
	print a1[1:]
	c+=1







