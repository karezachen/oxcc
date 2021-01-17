# author: kareza
# email: kareza@qq.com
# description: 后台启动服务，并进程PID

nohup python3 -u main.py 8080 > server.log 2>&1 &
ps aux | grep '[0-9] python3 -u main.py 8080' | awk '{print $2}' > PID
