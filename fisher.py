

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    return 'Hello, TerrySH'


#入口文件中添加，表示只在入口文件中执行
#生产环境 nginx+uwsgi app.run不会执行 保证生产环境不会启动flask自带的web服务器
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'], port=81)