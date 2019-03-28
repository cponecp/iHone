from werkzeug.routing import BaseConverter
from ihome.utils.response_code import RET
from functools import wraps
from flask import session, g, jsonify


class ReConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(ReConverter, self).__init__(url_map)
        self.regex = regex


def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')  # session与request属于请求上下文  这一步获取user_id,是利用改写的seesion存储去redis中拿
        if user_id:
            g.user_id = user_id  # g 属于应用上下文  为了方便视图函数再次获取user_id, 利用g传递已经获取过的user_id
            return view_func(*args, **kwargs)
        else:
            return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")

    return wrapper


# login_required总结: 如果涉及到在一次请求中,多个函数间传参数,可以利用g对象灵活的来传递



