# coding:utf-8

from flask import jsonify


class Response(object):
    @staticmethod
    def code(err=None, data=None):
        if err is None:
            err = ErrSuccess

        if data is None:
            return jsonify(code=err.errcode, msg=err.errmsg)
        else:
            return jsonify(code=err.errcode, msg=err.errmsg, data=data)


class ErrSuccess(object):
    errcode = 0
    errmsg = 'Success'


class Err(object):
    errcode = 1001
    errmsg = '未知错误'


class ErrToken(object):
    errcode = 1002
    errmsg = 'TOKEN 失效'


class Err403(object):
    errcode = 1003
    errmsg = '权限不存在'


class ErrUserNot(object):
    errcode = 1004
    errmsg = '账号不存在'


class ErrUserPassword(object):
    errcode = 1005
    errmsg = '密码不正确'


class ErrUser(object):
    errcode = 1006
    errmsg = '账号已经存在'


class ErrType(object):
    errcode = 1007
    errmsg = '分类已经存在'


class ErrTypeUse(object):
    errcode = 1008
    errmsg = '分类正在使用'


class ErrVariablenUse(object):
    errcode = 1009
    errmsg = '变量已经存在'


class ErrUserDel(object):
    errcode = 1010
    errmsg = '不能删除本人账号'


class ErrAppRunError(object):
    errcode =  1011
    errmsg = 'app运行错误'
