#!/usr/bin/env python3
#Roy David
#s2764989

import sys
import os
import time

def main(argv): #main():

	start_time = time.time()
	print("This program calculates the use of emojis in tweets by age(young(1986-2010)/old(1930-1976)) in %'s using a /net/corpora/twitter2/Tweets file from the RUG")
	print("\nRetrieving data, might take a couple of minutes...")
	f = []
	for line in sys.stdin:
		f.append(line)
	#os.system("zcat /net/corpora/twitter2/Tweets/2016/08/20160815*.out.gz | /net/corpora/twitter2/tools/tweet2tab user text > 20160815.txt")
	print("Retrieving data done")
	#f = open("20160815.txt", "r")
	emojilist = ["^-^","o.O","O.o",">:O",":v",":3",":D",";D",":-D",";-D",":)",";)",":-)",";-)","<3",":P",";P",":-P",";-P","XD","xD","x-D",":'D",":(",":-(","</3",":')",":'(","*-*","-_-","0_0",":o",":O",":-o",":-O",":'O",":'o",">.<",">,<",":*",";*",":|",":/",":]",";]"]
	young = [str(i) for i in range(1986,2011)]
	old = [str(i) for i in range(1930,1977)]
	agerange = [str(i) for i in range(1930,2011)]
	print("Filtering data by birthyear in username...")
	tweets_w_age_list = tweets_w_age(f, agerange)
	print("Filtering data done")
	print("Filtering data by emojis in tweets...")
	emojicntr = emojicntr_list(tweets_w_age_list, emojilist, old, young)
	print("Filtering data done")
	print("\nPrinting statistics:")
	print("total tweets within agerange(1930-2010):\t\t\t", len(tweets_w_age_list),"\ntotal tweets within old agerange(1930-1976):\t\t\t", emojicntr[2],"\ntotal tweets within young agerange(1986-2010):\t\t\t", emojicntr[3])
	print("total emojis used within the agerange(1930-2010):\t\t", emojicntr[0],"\ntotal tweets with emojis within agerange(1930-2010):\t\t", len(emojicntr[1]))
	res = results(young, old, agerange, emojicntr)
	print("total tweets with emojis within old agerange(1930-1976):\t", res[0],"\ntotal tweets with emojis within young agerange(1986-2010):\t", res[1])
	print("\nResults:")
	print("% old tweets w/ emoji(s) / total old tweets in data:\t\t", res[2],"\n% young tweets w/ emoji(s) / total young tweets in data:\t", res[3])
	#f.close()
	print("\n--- %s seconds ---" % (time.time() - start_time)) #http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution

def tweets_w_age(f, agerange): #filters data by birthyear in agerange in username, returns filtered datalist
	tweets_w_age_list = []
	for line in f:
		line = line.split("\t")
		username = line[0]
		if any(age in username[-4:] for age in agerange):
			tweets_w_age_list.append(line)
	return tweets_w_age_list

def emojicntr_list(tweets_w_age_list, emojilist, old, young): #filters data by emojis, counts total emojis, total old&young tweets, returns list of: total emojis, list w/ all tweets w/ emojis, total old tweets, total young tweets
	elist = []
	emojicntr = 0
	tot_old_tweets = 0
	tot_young_tweets = 0
	for line in tweets_w_age_list:
		if any(y in line[0] for y in young):
			tot_young_tweets += 1
		if any(o in line[0] for o in old):
			tot_old_tweets += 1
		emoji = ""
		for c in line[1].split():
			if c in emojilist:
				emoji = True
				emojicntr += 1
		if emoji == True:
			elist.append(line)
	return [emojicntr, elist, tot_old_tweets, tot_young_tweets]

def results(young, old, agerange, emojicntr): #counts how many old tweets there are in the data who use emojis, same for young people, gets percentages
	oldcntr = 0
	youngcntr = 0
	for line in emojicntr[1]: #emojicntr[1] = elist
		username = line[0]
		if any(age in username for age in agerange):
			if any(o in username for o in old):
				oldcntr += 1
			elif any(y in username for y in young):
				youngcntr += 1
	perc_old = (oldcntr/emojicntr[2])*100
	perc_young = (youngcntr/emojicntr[3])*100
	return [oldcntr, youngcntr, perc_old, perc_young]

if __name__ == "__main__":
	main(sys.argv) #main()
