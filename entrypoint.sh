#!/bin/sh
service nginx start
service postgresql start
service redis-server start
# service cron start
# service ntp start
/usr/bin/supervisord -n
