#!/usr/bin/env python
# encoding:utf-8
from . import *


@route.route("/get/dashboard/logs", methods=['GET', 'POST'])
def get_dashboard_logs():
    if request.method == "POST":
        logs_list = db.table('zbn_logs') \
            .join('zbn_workflow', 'zbn_logs.uuid', '=', 'zbn_workflow.uuid') \
            .select('zbn_logs.id', "zbn_logs.app_name", 'zbn_logs.result', 'zbn_workflow.create_time',
                    'zbn_workflow.name').order_by('zbn_logs.id', 'desc').limit(10).get()

        return Response.code(data=logs_list.serialize())


@route.route("/get/dashboard/sums", methods=['GET', 'POST'])
def get_dashboard_sums():
    if request.method == "POST":
        user_count = db.table('zbn_user').count()
        workflow_count = db.table('zbn_workflow').count()
        logs_count = db.table('zbn_logs').count()

        data = {
            "user_count": user_count,
            "workflow_count": workflow_count,
            "logs_count": logs_count
        }

        return Response.code(data=data)


@route.route("/get/dashboard/workflow", methods=['GET', 'POST'])
def get_dashboard_workflow():
    if request.method == "POST":
        sql = '''
        SELECT
            zbn_type.name as type,
            sum(1) AS value
        FROM
            zbn_workflow
        JOIN zbn_type ON zbn_workflow.type_id = zbn_type.id
        GROUP BY
            zbn_type.name;
        '''

        workflow_data = db.select(sql)

        return Response.code(data=workflow_data)


@route.route("/get/dashboard/exec", methods=['GET', 'POST'])
def get_dashboard_exec():
    if request.method == "POST":
        sql = '''
        SELECT
            DATE_FORMAT(create_time, "%%m-%%d") as timex,
            count(id) as value
        FROM
            zbn_logs
        WHERE
            DATE(create_time) > DATE_SUB(CURDATE(), INTERVAL 7 DAY)
        GROUP BY
            timex;
        '''

        exec_data = db.select(sql)

        return Response.code(data=exec_data)
