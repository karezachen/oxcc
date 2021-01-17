#!bin/bash
# author: kareza
# email: kareza@qq.com
# description: 后台启动服务，并保存进程pid

binpath=$(dirname $0)
nohup python3 -u $binpath/../code/main.py 8080 > $binpath/../logs/server.log 2>&1 &
ps aux | grep '[0-9] python3 .*main.py 8080' | awk '{print $2}' > $binpath/../logs/pid
