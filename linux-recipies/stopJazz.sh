#!/bin/bash
RTC_SERVER=RTCServerDev401
RTC_SERVER_PID=`pgrep -f "${RTC_SERVER}"`
#RTC_SERVER_PID=24450
RTC_SERVER_STOP_CMD="/opt/IBM/${RTC_SERVER}/server/server.shutdown"
#RTC_SERVER_STOP_CMD="kill -9 ${RTC_SERVER_PID}"

if ps -p ${RTC_SERVER_PID} > /dev/null
then
	echo "Stopping ${RTC_SERVER}..." >&1
	${RTC_SERVER_STOP_CMD}
else
	echo "${RTC_SERVER} is not running." >&1
	exit 1
fi

while ps -p ${RTC_SERVER_PID} > /dev/null
do
	sleep 15
done

echo "${RTC_SERVER} stopped successfully." >&1
exit 0