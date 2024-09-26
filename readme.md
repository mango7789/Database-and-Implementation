## 卖多多销售数据库系统

- 技术路径：基于`Django`框架开发，后端为`MySQL`
- 项目对标：“进销存管理+人员管理+数据可视化分析”**一站式轻量级**数据库系统

### 项目文件结构

```txt
├──database\        # 数据库配置文件夹
    ├──__init__.py       
    ├──asgi.py   
    ├──handler.py       # 异常状态处理器 
    ├──settings.py      # 数据库设置
    ├──urls.py          # web端url地址
    └──wsgi.py   
├──manager\         # @app 管理层   
    ├──__init__.py
    ├──admin.py       
    ├──apps.py         
    ├──test.py   
    ├──models.py        # 管理层表结构
    ├──forms.py         # 管理层表单
    ├──utils.py         # 辅助函数
    ├──config.py        # 参数(常数)配置   
    └──views.py         # 管理层主要函数
├──staff\           # @app 员工层
    ├──__init__.py  
    ├──admin.py       
    ├──apps.py         
    ├──test.py   
    ├──models.py        # 员工层表结构
    └──views.py         # 员工层表单+主要函数
├──backup\          # 存储用户上传的订单文件
├──static\          # 静态文件   
├──template\        # 所有html文件
├──doc\             # 大赛相关的所有文档
├──manage.py        # 管理该项目的python文件
├──retail.sql       # 导入测试数据的sql脚本
└──requirements.txt # 该项目依赖库文件
```

### 本地部署

- 在MySQL中创建 `Retail`表，并在`settings.py`中配置对应的用户名和密码
  ```sql
  CREATE SCHEMA Retail;
  USE Retail;
  ```
  ```python
  ### database/settings.py
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'retail',       # 数据库名称
          'USER': 'root',         # 用户名
          'PASSWORD': '123456',   # 密码
          'HOST': '127.0.0.1',
          'PORT': '3306'
      }
  }
  ```  
- 导入表结构和数据
  ```sql
  mysql -u root -p [CR][LF]
  123456 [CR][LF]
  USE Retail;
  SOURCE retail.sql;
  ```
- 启动本地服务器
  ```cmd
  python manage.py runserver --insecure [0.0.0.0:80]
  ```
  点击 http://127.0.0.1:8000/ 即可跳转到登录界面

> [!TIP]
> `--insecure`参数保证静态文件能被`Django`读取，`0.0.0.0:80`保证网址能被外部计算机通过80号端口进行访问

### 小组成员

- [mango7789](https://github.com/mango7789)
- [Oxlord-Lin](https://github.com/Oxlord-Lin)
- [Julius-Woo](https://github.com/Julius-Woo)
