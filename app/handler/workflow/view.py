#!/usr/bin/env python
# encoding:utf-8
from . import *


@route.route("/get/workflow/list", methods=['GET', 'POST'])
def get_user_list():
    if request.method == "POST":
        keywords = request.json.get("keywords", "")
        type = request.json.get("type", "0")

        workflow_list = db.table('zbn_workflow') \
            .join('zbn_user', 'zbn_workflow.user_id', '=', 'zbn_user.id') \
            .join('zbn_type', 'zbn_workflow.type_id', '=', 'zbn_type.id') \
            .select('zbn_workflow.id', 'zbn_workflow.uuid', "zbn_workflow.type_id", 'zbn_workflow.name',
                    'zbn_workflow.update_time', 'zbn_workflow.create_time', 'zbn_user.nick_name',
                    'zbn_type.name as type_name')

        if str(type) != "0":
            workflow_list = workflow_list.where("zbn_workflow.type_id", type)

        if str(keywords) == "":
            workflow_list = workflow_list.order_by('zbn_workflow.id', 'desc').get()
        else:
            workflow_list = workflow_list.where('zbn_workflow.name', 'like', '%{keywords}%'.format(keywords=keywords)) \
                .order_by('zbn_workflow.id', 'desc').get()

        return Response.code(data=workflow_list.serialize())


@route.route("/post/workflow/add", methods=['GET', 'POST'])
def post_workflow_add():
    if request.method == "POST":
        uuid = Random.make_uuid()

        token = request.headers.get("token")
        user_id = redis.get(token)

        db.table('zbn_workflow').insert({
            'uuid': str(uuid),
            "type_id": 1,
            "user_id": user_id,
            'name': "未命名剧本",
            'start_app': "",
            'end_app': "",
            'flow_json': "",
            'flow_data': "",
            'update_time': Time.get_date_time(),
            'create_time': Time.get_date_time()
        })

        return Response.code(data={"uuid": uuid})


@route.route("/post/workflow/detail", methods=['GET', 'POST'])
def get_workflow_detail():
    if request.method == "POST":
        uuid = request.json.get("uuid", "")

        workflow_info = db.table('zbn_workflow').select('uuid', 'name', 'start_app', 'end_app', 'flow_json',
                                                        'flow_data', 'type_id').where("uuid", uuid).first()

        return Response.code(data=workflow_info.serialize())


@route.route("/post/workflow/update", methods=['GET', 'POST'])
def post_workflow_update():
    if request.method == "POST":
        uuid = request.json.get("uuid", "")
        name = request.json.get("name", "")
        start_app = request.json.get("start_app", "")
        end_app = request.json.get("end_app", "")
        flow_json = request.json.get("flow_json", "")
        flow_data = request.json.get("flow_data", "")
        type_id = request.json.get("type_id", "")

        db.table('zbn_workflow').where('uuid', uuid).update({
            'name': name,
            'start_app': start_app,
            'end_app': end_app,
            'flow_json': flow_json,
            'flow_data': flow_data,
            'type_id': type_id,
            'update_time': Time.get_date_time()
        })

        return Response.code()


@route.route("/post/workflow/del", methods=['GET', 'POST'])
def post_workflow_del():
    if request.method == "POST":
        uuid = request.json.get("uuid", "")

        db.table('zbn_workflow').where('uuid', uuid).delete()

        return Response.code()


@ws.route('/logs')
def echo_socket(socket):
    while not socket.closed:
        message = socket.receive()

        if message:
            req_data = json.loads(message)
            method = req_data["method"]

            if method == "ping":
                pass
            elif method == "run":
                uuid = req_data["data"]["uuid"]
                run_exec(socket=socket, uuid=uuid)
