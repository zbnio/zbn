#!/usr/bin/env python
# encoding:utf-8
from . import *


@route.route("/get/user/list", methods=['GET', 'POST'])
def get_user_list():
    if request.method == "POST":
        keywords = request.json.get("keywords", "")

        if str(keywords) == "":
            user_list = db.table('zbn_user').select('id', 'account', 'nick_name', 'email', 'update_time',
                                                    'create_time').get()
        else:
            user_list = db.table('zbn_user') \
                .select('id', 'account', 'nick_name', 'email', 'update_time', 'create_time') \
                .where('account', 'like', '%{keywords}%'.format(keywords=keywords)) \
                .or_where('nick_name', 'like', '%{keywords}%'.format(keywords=keywords)) \
                .or_where('email', 'like', '%{keywords}%'.format(keywords=keywords)) \
                .get()

        return Response.code(data=user_list.serialize())


@route.route("/post/user/add", methods=['GET', 'POST'])
def post_user_add():
    if request.method == "POST":
        account = request.json.get("account", "")
        passwd = request.json.get("passwd", "")
        nick_name = request.json.get("nick_name", "")
        email = request.json.get("email", "")

        is_user_use = db.table('zbn_user').where('account', account).first()

        if is_user_use:
            return Response.code(err=ErrUser)

        md5_password = Random.make_md5_password(string=passwd)

        db.table('zbn_user').insert({
            'account': account,
            'passwd': md5_password,
            'nick_name': nick_name,
            'email': email,
            'update_time': Time.get_date_time(),
            'create_time': Time.get_date_time()
        })

        return Response.code()


@route.route("/post/user/update", methods=['GET', 'POST'])
def post_user_update():
    if request.method == "POST":
        id = request.json.get("id", "")
        nick_name = request.json.get("nick_name", "")
        email = request.json.get("email", "")
        passwd = request.json.get("passwd", "")

        if str(passwd) == "":
            db.table('zbn_user').where('id', id).update(
                {
                    "nick_name": nick_name,
                    "email": email,
                    "update_time": Time.get_date_time()
                }
            )
        else:
            md5_password = Random.make_md5_password(string=passwd)

            db.table('zbn_user').where('id', id).update(
                {
                    "nick_name": nick_name,
                    "email": email,
                    "passwd": md5_password,
                    "update_time": Time.get_date_time()
                }
            )

        return Response.code()


@route.route("/post/user/del", methods=['GET', 'POST'])
def post_user_del():
    if request.method == "POST":
        id = request.json.get("id", "")

        token = request.headers.get("token")

        is_user_use = db.table('zbn_user').where('token', token).first()

        if str(is_user_use["id"]) == str(id):
            return Response.code(err=ErrUserDel)

        db.table('zbn_user').where('id', id).delete()

        return Response.code()
