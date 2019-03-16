#!/bin/bash
RTC_SERVER=RTCServerDev401
RTC_SERVER_PID=`pgrep -f "${RTC_SERVER}"`
RTC_SERVER_START_CMD="/opt/IBM/${RTC_SERVER}/server/server.startup"

if [ -z "${RTC_SERVER_PID}" ] > /dev/null
then
	echo "Starting ${RTC_SERVER}..." >&1
	${RTC_SERVER_START_CMD}
else
	echo "${RTC_SERVER} is already running." >&1
	exit 1
fi

echo "${RTC_SERVER} started successfully." >&1
exit 0
