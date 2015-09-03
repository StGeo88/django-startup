# django-startup

django web 项目通用模板

## 特性列表

#### 脚本

- run.sh
- install.sh
- backup.sh

#### 数据安全

backup.sh 脚本自动备份数据库 / media 目录下的文件至 `init_data` 目录

下次执行 install.sh 脚本时，自动加载

#### Template 管理

templates 搜索路径:

- base/templates
- 每个 installed app 下的 templates 文件夹

#### MEDIA 资源管理

media 目录, 默认不进行版本管理.

建议使用单独的 repo 进行版本管理.


#### static 文件管理

默认版本管理时, 忽略根目录下的 static 文件夹.

通用的 js / css 文件使用 [我的私有 CDN](http://static.jackon.me)

建议,
`base/static` 目录下只放自定义 static 文件

生产环境部属时, 使用 collectstatic 收集至 project 根目录下的 static 目录里即可.

```shell
$ python manage.py collectstatic
```

#### 编码规范

遵循 PEP8 规范.  例外:

######  settings.py 报 Wildcard imports 错误

示例代码:

```python
try:
    from local_settings import *
except Exception as e:
    pass
```

报错内容:
```shell
settings.py|117 col 5| F403 'from local_settings import *' used;
unable to detect undefined names
```

###### url.py 报 E128 缩进错误

示例代码:

```python
urlpatterns = patterns('accounts.views',
    url(r'^signin$', 'signin', name='signin'),
    url(r'^signout$', 'signout', name='signout'),
)
```

报错内容:

```shell
accounts/urls.py|6 col 5| E128 continuation line under-indented for visual indent
```


## 注意

1. base 不作为 installed app 存在

## Build Dev Env

#### Linux / Mac

```shell
$ sudo pip install -r requirements.txt
$ ./install.sh
$ ./run.sh
```

#### Windows

```shell
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser --username=jackon --email=jiekunyang@gmail.com
$ python manage.py runserver 0.0.0.0:8000
```

## 快速使用

1. `base.context_processors.site_info.py` 中配置 brand logo 与 navbar
