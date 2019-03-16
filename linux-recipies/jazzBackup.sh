#!/bin/bash
RTC_SERVER=RTCServerDev401
RTC_BUILD_SERVER=TeamConcertBuild
BACKUP_DIR=/home/backup
EXCLUDE_DIRS=/opt/IBM/${RTC_BUILD_SERVER}/buildsystem/buildengine/eclipse/fetched
REMOTE_BACKUP_LOCATION=root@rigel:/home/fileserver/backups/$(echo ${HOSTNAME} | cut -d"." -f1)

bash stopJazz.sh

TIMESTAMP_LABEL=$(date "+%Y%m%d-%H%M")
RTC_SERVER_BACKUP_FILE=${BACKUP_DIR}/${RTC_SERVER}_${TIMESTAMP_LABEL}.tar.gz
RTC_BUILD_SERVER_BACKUP_FILE=${BACKUP_DIR}/${RTC_BUILD_SERVER}_${TIMESTAMP_LABEL}.tar.gz

echo "Creating Jazz Team Server backup in ${RTC_SERVER_BACKUP_FILE}"
tar -cpzf ${RTC_SERVER_BACKUP_FILE} /opt/IBM/${RTC_SERVER}
tar -cpzf ${RTC_BUILD_SERVER_BACKUP_FILE} /opt/IBM/${RTC_BUILD_SERVER} --exclude ${EXCLUDE_DIRS}

echo "Copying ${RTC_SERVER_BACKUP_FILE} to ${REMOTE_BACKUP_LOCATION}"
scp ${RTC_SERVER_BACKUP_FILE} ${REMOTE_BACKUP_LOCATION}
scp ${RTC_BUILD_SERVER_BACKUP_FILE} ${REMOTE_BACKUP_LOCATION}

bash startJazz.sh

