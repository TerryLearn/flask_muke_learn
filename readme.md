### 开始flask项目的步骤
* 安装Python环境
* 检验Python和pip是否安装完毕
* 新建项目文件夹
* 安装virtralenv
* 为什么需要安装虚拟环境
* 使用pipenv
* 安装pipenv pip install pipenv
* 使用pipenv创建一个虚拟环境和项目绑定
* 启动pipenv
* 安装各种包 比如flask pipenv install flask
* pipenv --venv 虚拟环境的路径

### Flask基本原理与核心知识

#### 最小的视图函数
from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
def hello():
	return "Hello, Terry"

app.run()

#### 打开调试模式
app.run(debug=True) #debug=True 自动重启 host=0.0.0.0 修改host可以被外网访问
调试模式性能较差 
~                              
