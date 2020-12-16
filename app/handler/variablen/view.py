#!/usr/bin/env python
# encoding:utf-8
from . import *


@route.route("/get/variablen/list", methods=['GET', 'POST'])
def get_variablen_list():
    if request.method == "POST":
        type = request.json.get("type", "0")
        keywords = request.json.get("keywords", "")

        variablen_list = db.table('zbn_variablen') \
            .join('zbn_type', 'zbn_variablen.type_id', '=', 'zbn_type.id') \
            .select('zbn_variablen.id', 'zbn_variablen.type_id', 'zbn_type.name as type_name', 'zbn_variablen.key',
                    'zbn_variablen.value', 'zbn_variablen.update_time',
                    'zbn_variablen.create_time')

        if str(type) != "0":
            variablen_list = variablen_list.where("type_id", type)

        if str(keywords) == "":
            variablen_list = variablen_list.get()
        else:
            variablen_list = variablen_list.or_where('key', 'like', '%{keywords}%'.format(keywords=keywords)).or_where(
                'value', 'like', '%{keywords}%'.format(keywords=keywords)).get()

        return Response.code(data=variablen_list.serialize())


@route.route("/post/variablen/add", methods=['GET', 'POST'])
def post_variablen_add():
    if request.method == "POST":
        type_id = request.json.get("type_id", "")
        key = request.json.get("key", "")
        value = request.json.get("value", "")

        is_key_use = db.table('zbn_variablen').where('key', key).first()

        if is_key_use:
            return Response.code(err=ErrVariablenUse)

        db.table('zbn_variablen').insert({
            'type_id': type_id,
            'key': key,
            'value': value,
            'update_time': Time.get_date_time(),
            'create_time': Time.get_date_time()
        })

        return Response.code()


@route.route("/post/variablen/update", methods=['GET', 'POST'])
def post_variablen_update():
    if request.method == "POST":
        id = request.json.get("id", "")
        type_id = request.json.get("type_id", "")
        key = request.json.get("key", "")
        value = request.json.get("value", "")

        is_key_use = db.table('zbn_variablen').where('key', key).first()

        if is_key_use:
            if str(is_key_use["id"]) != str(id):
                return Response.code(err=ErrVariablenUse)

        db.table('zbn_variablen').where('id', id).update(
            {
                "type_id": type_id,
                "key": key,
                "value": value,
                "update_time": Time.get_date_time()
            }
        )

        return Response.code()


@route.route("/post/variablen/del", methods=['GET', 'POST'])
def post_variablen_del():
    if request.method == "POST":
        id = request.json.get("id", "")
        db.table('zbn_variablen').where('id', id).delete()
        return Response.code()
