# Fei's django app demo INTRO / 简介

## 模型扩展

### 继承AbstractUser并扩展

对于新开发系统，可以**考虑**从AbstractUser继承并扩展，增加需要的字段。

以下是一个例子

```
# 以下是自建了一个用户模型，并且已经在settings中替换了

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    chinese_name = models.CharField(max_length=50, unique=True, blank=False)
    chinese_pass = models.CharField(max_length=100, blank=True)
    chinese_addr = models.CharField(max_length=200, blank=True)

# 在settings中设定了替换默认的User模型
AUTH_USER_MODEL = 'app_models.CustomUser'

# 迁移后创建了自定义的用户表，名字是 <appname_customuser>
# 默认的auth_user表没有了，被此customuser表代替
# 而其它的系统表名字都不变，仍然是auth_groups /auth_permissions等
# 可以看到，customuser在User模型上，增加了上面自定义的三个字段
CREATE TABLE `app_models_customuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `chinese_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `chinese_pass` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `chinese_addr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `chinese_name` (`chinese_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

# 看一下user permissions表，本来默认指向 auth_user的外键，现在指向了这个customuser表；
# 本来指向auth_permission的外键，依然不变

CREATE TABLE `app_models_customuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_models_customuser_us_customuser_id_permission_b33a0c84_uniq` (`customuser_id`,`permission_id`),
  KEY `app_models_customuse_permission_id_948a0a60_fk_auth_perm` (`permission_id`),
  CONSTRAINT `app_models_customuse_customuser_id_50275884_fk_app_model` FOREIGN KEY (`customuser_id`) REFERENCES `app_models_customuser` (`id`),
  CONSTRAINT `app_models_customuse_permission_id_948a0a60_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
```

因此，从AbstractUser扩展，实际上就是把默认的auth_user，替换成了自定义的CustomerUser。

以上CustomUser模型在后续可以修改定义，增减字段，然后执行迁移，也是很方便的。

### One-To-One方式扩展

在已有的系统增加，则可以考虑通过one to one的关系，增加一个额外的模型；

```
既可以使用django的auth backend，也可以扩展使用自定义的认证方式，例如使用多个标识（用户名/邮箱/手机呈等）登录。
```

## 直接修改模型并迁移 vs one-to-one 

直接修改模型保证新加的字段和原字段在同一张表里，每个用户进来的时候一次就获取到需要数据；

one-to-one意味着每个用户进来的时候，需要访问两张表才获取到全部数据，性能当然会降低，对系统压力更大一点；

不过，如果额外增加的信息是一个很少用到的信息，用one-to-one，能减少访问表的次数，对性能反而是有益的。

## 自行定制middleware

针对全部用户或针对全部访问请求的操作，可以用定制middleware实现

见`fei/fei_middlewares`目录：

```
# 为用户初始化一些信息
data_initial.py
    initial_user_asset
    initial_user_extra

# 为用户自动生成token
generate_token.py
    generate_token_if_not_exist

# 开放了一个测试用户，为了避免被改密码，简单的禁止了该用户的改密码功能
# 其实只是禁止了change password的url
user_filter.py
    disable_user_change_pass

# 以下几个middlewares作为调试工具，可以在控制台打印出当前访问用户、headers、用户token等信息
headers_info.py
    request_headers
    response_headers
logging_user.py
    django_current_user
drf_token_info.py
    drf_user_info
```



## 自行定制auth backend

通过定制的backend，实现username, email，手机号，或者任何其它需要的用户标识来进行认证；

并且用户可以用password或pay_password等任何密码来进行认证。

```
fei/fei_backends/fei_auth.py
```

## API Root / Open API / Swagger等

写了一个简单的后端demo

```
http://demo.hhxx.me/v2/									# Api Root
http://demo.hhxx.me/drf/openapi/				# Open API
http://demo.hhxx.me/drf/swargger/				# 用swagger UI格式的接口列表
```

## 一个表情包加文字的小功能

```
http://demo.hhxx.me/img/emoji/					# 一个表情包处理的功能，做给朋友玩
																				# fei/app_img
```

## 一个查询IP的小功能

```
http://demo.hhxx.me/ip/									# 发现查询自已的公网ip的功能还比较常用，然后一些查ip的网站老是给一个页面出来，所以做个小功能，直接返回个json就可以了，便于命令行curl访问。用法：

curl demo.hhxx.me/ip/										# output: {"Your IP": "61.140.26.251"}
```

## webhook

```
# 收到webhook后，在本地就去git pull一下相应的repo
# 用于在ecs上自动更新代码
# 没想好需要些什么功能，目前就最简单粗暴的git pull一下
https://fei-webhook.readthedocs.io/						# webhook的文档
https://github.com/colingong/fei_webhook/			# 项目代码
```

## celery / rabbitmq /redis 等

TODO: 



