#!/bin/bash
supervisord -c /etc/supervisord.conf && tail -f /tmp/supervisord.log
