#!/bin/bash
# s2764989
# inl.wts.oz
#
# Descr:A shell script that counts how many tweets, unique tweets, retweets
# 	there are in a sample of tweets and shows the first 20 unique tweets
# 	that are not retweets
#
# Usage:./sample-tweets.sh FILE(/net/corpora/twitter2/Tweets/2016/08/2017040212.out.gz | /net/corpora/twitter2/tools/tweet2tab user text)

# argument is the file, check if we get it
TEXT=$1
if [ -z "$TEXT" ]
then
	echo "specify a file!"
	exit
fi
# counts lines(tweets)
cat $TEXT | wc -l
# counts unique tweets
cat $TEXT | uniq | wc -l
# counts RT's within unique tweets
cat $TEXT | uniq | grep -c 'RT'
# show the first 20 unique tweets in the sample that are not retweets
cat $TEXT | uniq | grep -v 'RT' | head -20

