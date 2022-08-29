---
title: docker常用操作
---

# 从hub.docker.com取image

hub.docker.com是docker公司提供的docker images存储服务，所有大家共享的image都在hub上可以直接拉取使用，包括各大厂商产品的官方image。

```
docker pull dockername:tag
```

忽略:tag时自动拉取最新版本:latest，但这不是好方法，升级可能导致兼容性问题。

# 运行

```
docker run [OPTIONS] IMAGE:TAG [COMMAND] [ARG...]
```

OPTIONS选项：

- -d: 后台运行
- -v 宿主机目录:内部目录 将宿主机目录映射到容器内部目录
- -p 素主机端口:内部端口 将宿主机端口映射到容器内部端口，外部才能访问
- -it 交互模式
- --name=容器名 给容器起个名字，便于访问
- --rm 容器停止运行时删除容器(否则容器一直存在)

COMMAND ARGs：启动容器并运行容器中的命令

# 其他常用命令

```
docker ps # 查看运行中的容器
docker ps -a # 查看所有存在的容器(包括stop的)
docker stop 容器名或容器ID # 停止容器
docker rm  容器名或容器ID # 删除容器
docker images # 查看所有本地的image
docker rmi image名或imageID # 删除image
docker inspect 容器名或ID # 查看容器信息

```

# 进入到容器中

进入已运行的容器中并运行/bin/sh，可交互操作

```
docker exec -it 容器名或ID /bin/sh
```

运行镜像并进入容器，并运行/bin/sh，可交互操作

```
docker run -it --rm --entrypoint=/bin/sh 镜像名或ID
```

# 制作image

1. 编辑Dockerfile镜像定义文件

2. 根据Dockerfile做出image文件

```
docker build --pull --rm  -f "Dockerfile" --target 分段名 -t imagename:tag .
```

3. 推送到hub上

```
# 将本地的镜像名和tag打上hub的用户名/镜像/tag
docker tag imgname1:tag1 username/imgname:tag

# 推送到hub上自己的帐号中，可共享
docker push username/imgname:tag
```

# docker compose 启停

docker compose是本地编排工具，可以按定义的顺序启动多个容器，象多台服务器一样互相调用访问，形成一个系统。

```
# 按当前目录的docker-compose.yml启动，-d为后台运行
docker compose up -d
# 将按当前目录docker-compose.yml定义启动的一组容器停止并删除
docker compose down
# 将按当前目录docker-compose.yml定义启动的一组容器停止，不删除容器
docker compose stop
# 将按当前目录docker-compose.yml定义启动过但停止未删除的一组容器重新启动
docker compose start
```

# docker的网络

每个启动的容器相当于一台带网卡的服务器：

- 宿主机可以直接访问容器的内部ip
- 容器之间需要定义网络才能互相通信
- 容器的内部IP需要映射到宿主机才能被别的机器访问
- 用compose设定比较方便一组容器互相访问，不必放出来的端口应保持在docker内部网络上不映射出来。

# docker的文件卷

如果没有文件卷也没有映射到本地目录，容器运行后的数据将在容器被删除时消失，要持久化需要：

- docker -v 可以映射本地目录到容器内部目录(或文件)
- 也可以给容器建立一个文件卷来持久化数据

```
docker volume ls # 查看宿主机上所有docker卷
docker volume rm 卷名 # 删除宿主机上的docker文件卷
```





