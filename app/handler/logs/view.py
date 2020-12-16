#!/usr/bin/env python
# encoding:utf-8
from . import *


@route.route("/get/logs/list", methods=['GET', 'POST'])
def get_logs_list():
    if request.method == "POST":
        logs_list = db.table('zbn_logs') \
            .join('zbn_workflow', 'zbn_logs.uuid', '=', 'zbn_workflow.uuid') \
            .select('zbn_logs.id', "zbn_logs.app_name", 'zbn_logs.result', 'zbn_workflow.create_time',
                    'zbn_workflow.name').get()

        return Response.code(data=logs_list.serialize())
