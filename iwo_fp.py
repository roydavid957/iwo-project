#!/usr/bin/env python3
#Roy David
#s2764989

import sys
import os
#from pandas_datareader import data, wb

def main(): #def main(argv):
	#os.system("zcat /net/corpora/twitter2/Tweets/2016/08/20160815*.out.gz | /net/corpora/twitter2/tools/tweet2tab user text > 20160815.txt")
	f = open("20160815.txt", "r")
	emojis = [":D",";D",":-D",";-D",":)",";)",":-)",";-)","<3",":P",";P",":-P",";-P","XD","xD","x-D",":'D",
		":(",":-(","</3",":')",":'(","*-*","-_-","0_0",":o",":O",":-o",":-O",":'O",":'o",">.<",">,<",":*",";*"]
	elist = []
	emojicntr = 0
	young = [str(i) for i in range(1986,2011)]
	old = [str(i) for i in range(1930,1976)]
	agerange = [str(i) for i in range(1930,2011)]
	oldcntr = 0
	youngcntr = 0
	fage = open("twwage.txt", "w")
	for line in f:
		line = line.split("\t")
		username = line[0]
		if any(age in username[-4:] for age in agerange):
			fage.write("\t".join(line))
	fage.close()
	fage = open("twwage.txt", "r")
	for line in fage:
		emoji = ""
		line = line.split("\t")
		for c in line[1].split():
			if c in emojis:
				emoji = True
		if emoji == True:
			elist.append(line)
			emojicntr += 1
	print("ec",emojicntr)
	print("el",len(elist))
	for line in elist:
		username = line[0]
		if any(age in username for age in agerange):
			if any(o in username for o in old):
				oldcntr += 1
			elif any(y in username for y in young):
				youngcntr += 1
	print("o",oldcntr)
	print("y",youngcntr)
	print("t",youngcntr+oldcntr)
	f.close()
	fage.close()
if __name__ == "__main__":
	main() #main(sys.argv)
