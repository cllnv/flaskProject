from flask import Flask
from flask import jsonify
from flask import request,session
from flask import render_template
from flask import make_response
# from test_flask.com_db import Con_DB

app = Flask(__name__)

app.secret_key = 'dfdfdf'
user_info = {'1001':['123456','A',9000],'1002':['123456','B',1000]}
userinfo1 = [{'account':'111','name':'cll'},{'account':'222','name':'cll1'}]


@app.route('/users', methods=['GET'])
def users():
    return 'Hello World!'


@app.route('/users1/userid', methods=['GET'])
def get_userid():
    acc = request.args.get('account')  # 获取客户端传来的参数
    if acc:
        for i in userinfo1:
            if acc == i['account']:
                return jsonify({'code':10000,'message':'success'})
        else:
            return jsonify({'code': 1001, 'message': '账号不存在'})
    else:
        return jsonify({'code': 1001, 'message': '账号不存在'})


@app.route('/users/<string:account>', methods=['GET'])
def get_users(account):
    # get_cookies = request.cookies.get('acc')
    get_cookies = session.get('acc')
    print(get_cookies)
    if get_cookies:
        if account in user_info:
            info = user_info[account]
            return f'尊敬的{info[1]},余额为{info[2]:.2f}'
        else:
            return '账号不存在'
    else:
        return 'cookies未通过'


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'GET':
    #     return jsonify({'code': 10001, 'message': 'method error'})
    # else:
    #  request.args.get('account') #  获取的是url后面问号跟的参数
        acc = request.form.get('account')
        pwd = request.json.get('password')
        # print("pwd:"+pwd)
        if pwd:
            sql = f'select * from userinfo where account="{acc}";'
            # info = cd.query_one(sql)
            res = make_response('成功')
            # res.set_cookie('username',acc,max_age=60)
            session['acc'] = 11  # 添加session
            return jsonify({'code': 1000, 'message': 'success'})
        else:
            return jsonify({'code': 1001, 'message': 'fail'})


@app.route('/test', methods=['GET', 'POST'])
def test():
    # request.args.get('account') #  获取的是url后面问号跟的参数
    args1 = request.args.get('args1')
    form1 = request.form.get('form1')
    values1 = request.values.get('values1')
    print(args1)
    print(form1)
    print(values1)
    return "acc1"  # flask 请求不可以没有返回值


'''
       args:
      param   form-data   x-www-form-urlencoded  json
get    yes      no                no              no
post   yes      no                no              no

       form:
      param   form-data   x-www-form-urlencoded  json
get    no      yes                yes              no
post   no      yes                yes              no

     values:
      param   form-data   x-www-form-urlencoded  json
get    yes      no                no              no
post   yes      yes                yes              no
'''


@app.route('/logout', methods=['GET','POST'])
def logout():
    try:
        res = make_response({"code": 10000, "message": "logout success"})
        # res.delete_cookie('acc') # 删除指定cookies
        session.pop('acc')  # 删除指定session
    except Exception:
        return jsonify({"code": 10001, "message": "unknown error"})


if __name__ == '__main__':
    # app.run() 默认方式启动
    app.run(host='0.0.0.0', port=5000, debug=True)#不生效
