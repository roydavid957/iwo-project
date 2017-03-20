#!/usr/bin/env python3
#Roy David
#s2764989

import sys
import os
#from pandas_datareader import data, wb

def main(): #def main(argv):
	#makedata
	#os.system("zcat /net/corpora/twitter2/Tweets/2016/08/20160815*.out.gz | /net/corpora/twitter2/tools/tweet2tab user text > 20160815.txt")

	f = open("20160815.txt", "r")

	#emojilist
	emojis = ["^-^","o.O","O.o",">:O",":v",":3",":D",";D",":-D",";-D",":)",";)",":-)",";-)","<3",":P",";P",":-P",";-P","XD","xD","x-D",":'D",":(",":-(","</3",":')",":'(","*-*","-_-","0_0",":o",":O",":-o",":-O",":'O",":'o",">.<",">,<",":*",";*",":|",":/",":]",";]","B|","B-)",">:("]
	#emojis = [":)",":(",":P",":D",":O",";)","B-)","B|",">:(",":/",":'(","3:)","O:)",":*","<3","^-^","-_-","o.O","O.o",">:O",":v",":3"] #http://emojicodes.com/

	#ageranges
	young = [str(i) for i in range(1986,2011)]
	old = [str(i) for i in range(1930,1976)]
	agerange = [str(i) for i in range(1930,2011)]

	#tweets_w_age_list
	tweets_w_age = []
	for line in f:
		line = line.split("\t")
		username = line[0]
		if any(age in username[-4:] for age in agerange):
			tweets_w_age.append(line)

	#emojicntr&list
	elist = []
	emojicntr = 0
	for line in tweets_w_age:
		emoji = ""
		for c in line[1].split():
			if c in emojis:
				emoji = True
		if emoji == True:
			elist.append(line)
			emojicntr += 1
	print("ec",emojicntr)
	print("el",len(elist))

	#results
	oldcntr = 0
	youngcntr = 0
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
if __name__ == "__main__":
	main() #main(sys.argv)
