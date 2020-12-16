#!/bin/bash
# Author : ZBN SOAR
# Web : https://zbn.io

if [ -z "$1" ]
then
    docker build -t zbn_soar:latest .
    docker run -v $PWD/init_sql:/docker-entrypoint-initdb.d -v $PWD/conf.d:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=root --name zbn_mysql -d mysql:5.7
    docker run --name zbn_redis -d redis
    docker run --name zbn --link zbn_redis:zbn_redis --link zbn_mysql:zbn_mysql -p0.0.0.0:8888:8888 -d zbn_soar:latest
elif [ $1 == "-n" ]
then
    docker pull registry.cn-shanghai.aliyuncs.com/3vil/zbn_soar:latest
    docker tag registry.cn-shanghai.aliyuncs.com/3vil/zbn_soar:latest zbn_soar:latest
    docker run -v $PWD/init_sql:/docker-entrypoint-initdb.d -v $PWD/conf.d:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=root --name zbn_mysql -d mysql:5.7
    docker run --name zbn_redis -d redis
    docker run --name zbn --link zbn_redis:zbn_redis --link zbn_mysql:zbn_mysql -p0.0.0.0:8888:8888 -d zbn_soar:latest
elif [ $1 == "-u" ]
then
    docker rm -f zbn
    docker start zbn_mysql zbn_redis
    docker pull registry.cn-shanghai.aliyuncs.com/3vil/zbn_soar:latest
    docker tag registry.cn-shanghai.aliyuncs.com/3vil/zbn_soar:latest zbn_soar:latest
    docker run --name zbn --link zbn_redis:zbn_redis --link zbn_mysql:zbn_mysql -p0.0.0.0:8888:8888 -d zbn_soar:latest

else
   echo "没有符合的条件"
fi