

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    #status code 200 404 301
    # content-type http headers
    #content-type = text/html默认
    headers = {
        'content-type':'application/json',
        'location':'http://www.bing.com'
    }
    return '<html><html>', 301, headers



#入口文件中添加，表示只在入口文件中执行
#生产环境 nginx+uwsgi app.run不会执行 保证生产环境不会启动flask自带的web服务器
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'], port=81)