#!/bin/sh
#set -x #echo on
if ! test $# -eq 1
then
	echo 'Usage: sopcast1 <channel>'
	exit 0
fi
/usr/local/bin/sp-auth/sp-sc-auth sop://broker.sopcast.com:3912/$1 3908 8908 > /dev/null
