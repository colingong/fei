# Fei's django app demo INTRO / 简介

## 项目布署在这儿

<a href="http://demo.hhxx.me">http://demo.hhxx.me</a>

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

## 用docker来布署开发环境

```
# 腾讯云 ecs: 1CPU/1GB Ram/40GB HDD
# 本机布署以下应用/组件

python:3.6ays           0.0.0.0:8001->8000/tcp                               8001dj_webhook
python:3.6inutes        0.0.0.0:5553->5556/tcp, 0.0.0.0:83->8000/tcp         83dj_fei
python:3.6eeks          0.0.0.0:5557->5556/tcp, 0.0.0.0:81->8000/tcp         81dj_weixin
python:3.6eeks          0.0.0.0:5556->5556/tcp, 0.0.0.0:82->8000/tcp         82dj_educa
nginx:1.14days          0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp             web-nginx-80
mongo:4.0.onths         0.0.0.0:27017->27017/tcp                             mongo4-27017
redis:4-alonths         0.0.0.0:6379->6379/tcp                               redis-6379
jkarlos/gionths         0.0.0.0:2222->22/tcp                     git-server-source-code-repos
mysql:5.7 eeks          33060/tcp, 0.0.0.0:5004->3306/tcp                    mysql57-5004

rabbitmq:3onths         4369/tcp, 0.0.0.0:5672->5672/tcp, 5671/tcp, 25672/tcp, 0.0.0.0:15672->15672/tcp   rabbit5672
```

### 要点

```
1. 在内存不够的情况下，需要开启swap
2. django app映射到不同的本机外部端口，可以是80, 81等，也可以是8000, 8001等
3. nginx解析域名，指向不同的端口
4. redis，mongo，mysql，等都可以开多个实例，映射到不同端口即可
5. 线上生产系统不要把redis/mysql等端口开放到公网ip，应该仅限于内网访问
```

### nginx

```
确定服务端口，通常情况下监听80和443端口即可，支持http和https
nginx官方镜像的文件目录是/usr/share/nginx/html，将自已的文件目录mount到该目录即可
nginx官方镜像的配置文件目录是/etc/nginx/conf.d，将自已的配置文件目录mount到该目录
对于个人开发测试等用途，没有镜像分发需求，直接docker run起container即可

docker run                                                                      \
        --name web-nginx-80                                                     \
        -v /root/docker-op/nginx-test/content:/usr/share/nginx/html             \
        -v /root/docker-op/nginx-test/conf:/etc/nginx/conf.d                    \
        -d                                                                      \
        -p 0.0.0.0:80:80                                                        \
        -p 0.0.0.0:443:443                                                      \
        nginx:1.14.2-alpine
```

支持多站点的配置

```
在前面提到的nginx配置文件夹中，针对每个site写一个配置文件，每增加一个site，简单增加一个配置文件即可
例如有以下5个配置文件，每个配置文件都支持了一个域名/子域名的web服务
当你要取消某个站点的服务时，简单的将名字改掉或删掉对应的配置文件即可
web-82.conf							# 一个应用跑在本机的82端口上，nginx转发相应的请求到该端口
webhook-8001.conf  			# 另一个叫做webhook的应用配置跑在本机的 8001端口，ningx将对应的请求转发到该端口
wx-web-81.conf					# 一个跑在 81端口上的微信公众号服务
not_use_web-84      		# 一个不再使用的配置文件
```

配置文件示例：

```
# this is a testing config for site: http://demo.hhxx.me
# copy this config to container:/etc/nginx/conf.d

  server {
    client_max_body_size 20M;
    listen       80;
    server_name  83.hhxx.me demo.hhxx.me;
    charset utf-8,gbk;
    access_log  /var/log/nginx/access.log  main;

    # pass requests for dynamic content to rails/turbogears/zope, et al
    location / {
#       return 200 'web-83';
#       default_type "text/html; charset=UTF-8";
      proxy_pass      http://10.0.0.13:83/;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For "$http_x_forwarded_for, $realip_remote_addr";
      proxy_set_header Host $host;

    }
  }

# 注意这个配置是将请求转发到本机的83端口，因为一个docker封装的python/django应用被映射到83端口
# 其中 return 200 'web-83' 和 default_type，可用于测试nginx是否正确提供了期望的服务
```

### python3/Django应用

对于python/django应用，官方镜像默认源文件位于/usr/src/app目录

将自已的程序源文件目录mount到该目录即可

这里的PIP_CONF是为了解决python包下载速度太慢，配置了国内的镜像源

按照自已的喜好，可选阿里云或腾讯云的镜像源都可以。

```
# create a docker container named : pydev_

SOURCE_CODE_DIR=/root/docker-op/py_dev/code_repos/github_fei/fei
ENV_FILE_FILE=/root/docker-op/py_dev/code_repos/github_fei_env/env_fei
PIP_CONF=/root/docker-op/py_dev/pip-conf

docker run                                                                      \
        --name  83dj_fei                                                        \
        --env-file ${ENV_FILE_FILE}                                             \
        -v ${SOURCE_CODE_DIR}:/usr/src/app                                      \
        -v ${PIP_CONF}:/root/.pip                                               \
        -dit                                                                    \
        -p 0.0.0.0:83:8000                                                      \
        -p 0.0.0.0:5553:5556                                                    \
        python:3.6-stretch                                                      \
        sh -c "cd /usr/src/app &&  pip install --no-cache-dir --default-timeout=150 -r  requirements.txt &&  python manage.py runserver 0.0.0.0:8000 --insecure "


```

### mysql

对于mysql官方镜像源，默认的data dir是 /var/lib/mysql，默认的配置目录是 /etc/mysql/conf.d

将自已的数据目录和配置目录写好就可以了

mysql的端口如果开放公网访问的话（个人测试或开发一般会这么干），考虑把端口号改成 3306以外的端口，减少被扫描爆破的风险。

```
MYSQL_DATA_DIR="/root/docker-op/mysql57/data_mysql57_5004"
MYSQL_CONF_DIR="/root/docker-op/mysql57/conf.d"
docker run --name mysql57-5004                                                          \
                -e MYSQL_ROOT_PASSWORD=Vpassword123456789 -d                            \
                -v $MYSQL_DATA_DIR:/var/lib/mysql                                       \
                -v $MYSQL_CONF_DIR:/etc/mysql/conf.d                     								\
                -p 0.0.0.0:3456:3306                                                    \
                mysql:5.7
```



### redis

redis的配置和上面差不多，都是了解下配置文件目录，然后就可以写好相应的脚本了。

```
CONTAINER_NAME="redis-6379"

docker run                                                                              \
        -v ${REDIS_CONF_FILE}:/usr/local/etc/redis/redis.conf                           \
        -d                                                                              \
        -p 0.0.0.0:6379:6379                                                            \
        --name ${CONTAINER_NAME}                                                        \
        redis:4-alpine                                                                  \
        redis-server /usr/local/etc/redis/redis.conf
```

### rabbitmq

rabbitmq也一样，就是注意开放管理端口的话，需要再映射多一个管理端口

这里也是可以把默认端口改成其它端口。

```
# This will start a RabbitMQ container listening on the default port of 5672.

docker run -d --hostname my-rabbit                      \
        -p 0.0.0.0:5672:5672                            \
        -p 0.0.0.0:15672:15672                          \
        --name rabbit5672 rabbitmq:3
```

## 自建git server

git server官方没有镜像，可以找其它人制作的镜像，也可以自已自制一个。

git server本身没啥特别的，一般碰到麻烦的无非就是配ssh/sshd的时候出状况。

```
# 这里我用了一个别人自制的镜像 jkarlos/git-server-docker
HOST_REPO_DIR="/home/data/source-code-repos"
CONTAINER_DIR="/home/git/source_code"

SSH_KEYS_DIR="/root/docker-op/git-server/ssh_keys"
CONTAINER_SSH_KEYS_DIR="/home/git/.ssh"

docker run -d                                                                   \
        --name git-server-source-code-repos                                     \
        -p 2222:22                                                              \
        -v ${HOST_REPO_DIR}:${CONTAINER_DIR}                                    \
        -v ${SSH_KEYS_DIR}:${CONTAINER_SSH_KEYS_DIR}                            \
        jkarlos/git-server-docker
```

**docker很方便，也需要注意一些地方：**

```
可以为container设定--restart=always
google云服务器上预装的docker，设定是自动更新，如果container没有自动 restart，那么每次docker更新之后你就会奇怪为什么container都挂掉了！
```



## 腾讯云redis的一个简单测试

三个redis

```
1. 1C1G ECS上，docker 里运行的redis实例（本机）		（成都一区内网一）
2. 1C1G redis实例，腾讯云上的redis实例						（成都二区内网二）
3. 4C8G ECS上，docker 里运行的redis实例						（成都一区内网一）
即三个实例，其中1和3在同地同区同一内网，2在同地同区另一内网
```
**测试结果**
实例 1

```
        # 本机
        64 bytes from 10.0.0.13: icmp_seq=1 ttl=64 time=0.051 ms
        64 bytes from 10.0.0.13: icmp_seq=2 ttl=64 time=0.047 ms
        start bench redis1
        Duration: 5.584269046783447
```

实例 2

```
        # 同地址域不同区的一个redis实例
        # redis-cli --latency -h 10.0.2.4 -p 6379
        # min: 1, max: 7, avg: 1.56 (343 samples)^C
        # 这个延迟达到1.56，也是相当的高；不过和两台同子网内的延迟比起来，似乎又不算历害了
        start bench redis2金
        Duration: 52.816078186035156
```

实例 3

```
        # 同区（成都一区）内同子网的另一台主机
        # 64 bytes from 10.0.0.22: icmp_seq=3 ttl=63 time=1.76 ms
        # 64 bytes from 10.0.0.22: icmp_seq=4 ttl=63 time=1.72 ms
        # 同子网内，这个延迟高的有点离谱
        start bench redis3
        Duration: 57.26516246795654
```

有点出乎意料的结果：

```
    仅从set来看，这个内网延迟很有点高；这么高的延迟，get都不用测了
    对于redis，连接池看来还是很有必要的，随便延迟高一点的话，完全发挥不出来它的优势
```





