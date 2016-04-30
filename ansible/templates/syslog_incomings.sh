#!/bin/sh
tail -200 /var/log/supervisor/supervisord.log > /tmp/supervisor_d.json
curl -k -H "Content-Type: application/json" -H "Accept: application/json" -X POST --data @/tmp/supervisor_d.json https://incomings.io/incomings/BZwdYlxdl6tWdL6C