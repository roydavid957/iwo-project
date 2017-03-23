#!/usr/bin/env python3
#Roy David
#s2764989

import sys
import os
#from pandas_datareader import data, wb

def main(): #def main(argv):
	#os.system("zcat /net/corpora/twitter2/Tweets/2016/08/20160815*.out.gz | /net/corpora/twitter2/tools/tweet2tab user text > 20160815.txt")
	f = open("20160815.txt", "r")
	emojilist = ["^-^","o.O","O.o",">:O",":v",":3",":D",";D",":-D",";-D",":)",";)",":-)",";-)","<3",":P",";P",":-P",";-P","XD","xD","x-D",":'D",":(",":-(","</3",":')",":'(","*-*","-_-","0_0",":o",":O",":-o",":-O",":'O",":'o",">.<",">,<",":*",";*",":|",":/",":]",";]"]
	#emojilist = [":)",":(",":P",":D",":O",";)","B-)","B|",">:(",":/",":'(","3:)","O:)",":*","<3","^-^","-_-","o.O","O.o",">:O",":v",":3"] #http://emojicodes.com/
	young = [str(i) for i in range(1986,2011)]
	old = [str(i) for i in range(1930,1976)]
	agerange = [str(i) for i in range(1930,2011)]
	tweets_w_age_list = tweets_w_age(f, agerange)
	emojicntr = emojicntr_list(tweets_w_age_list, emojilist)
	print("ec", emojicntr[0],"\n" "el", len(emojicntr[1]))
	res = results(young, old, agerange, emojicntr)
	print("o", res[0],"\n" "y", res[1], "\n" "t", res[0]+res[1])
	f.close()

def tweets_w_age(f, agerange):
	tweets_w_age_list = []
	for line in f:
		line = line.split("\t")
		username = line[0]
		if any(age in username[-4:] for age in agerange):
			tweets_w_age_list.append(line)
	return tweets_w_age_list

def emojicntr_list(tweets_w_age_list, emojilist):
	elist = []
	emojicntr = 0
	for line in tweets_w_age_list:
		emoji = ""
		for c in line[1].split():
			if c in emojilist:
				emoji = True
		if emoji == True:
			elist.append(line)
			emojicntr += 1
	return [emojicntr, elist]

def results(young, old, agerange, emojicntr):
	oldcntr = 0
	youngcntr = 0
	for line in emojicntr[1]:
		username = line[0]
		if any(age in username for age in agerange):
			if any(o in username for o in old):
				oldcntr += 1
			elif any(y in username for y in young):
				youngcntr += 1
	return [oldcntr, youngcntr]

if __name__ == "__main__":
	main() #main(sys.argv)
