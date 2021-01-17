#!bin/bash
# author: kareza
# email: kareza@qq.com
# description: 停止服务，删除保存的进程pid，并将server.log重命名为当前日期

binpath=$(dirname $0)
pid=$(cat $binpath/../logs/pid)
date=$(date +%F)

kill $pid
rm -f $binpath/../logs/pid
mv $binpath/../logs/server.log $binpath/../logs/$date.log
