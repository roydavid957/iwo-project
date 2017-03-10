#!/bin/bash
# s2764989
# inl.wts.oz
#
# Descr:A shell script that counts how many tweets, unique tweets, retweets
# 	there are in a sample of tweets and shows the first 20 unique tweets
# 	that are not retweets
#
# Usage:./sample-tweets.sh FILE(20170301:12.txt)
#	download the .txt file from: https://github.com/roydavid957/iwo-project
#	to create .txt file: zcat /net/corpora/twitter2/Tweets/2017/03/20170301\:12.out.gz | /net/corpora/twitter2/tools/tweet2tab text > FILENAME

echo -e "\e[33mUsage:./sample-tweets.sh FILE(20170301:12.txt)"
echo -e "	download the .txt file from: https://github.com/roydavid957/iwo-project"
echo -e "	to create .txt file: zcat /net/corpora/twitter2/Tweets/2017/03/20170301\:12.out.gz | /net/corpora/twitter2/tools/tweet2tab text > FILENAME\e[0m"
echo ""
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
cat $TEXT | uniq | grep -c -w 'RT'
#show the first 20 unique tweets in the sample that are not retweets
cat $TEXT | uniq | grep -v -w 'RT' | head -20

