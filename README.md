# OXCC

## 服务验证

在启动服务之前，需要先进行token验证。
> 功能已存在于code中，如何使用待开发

## 快捷使用

启动服务

```shell
python3 -m venv oxcc_env
source oxcc_env/bin/activate
pip install -r requirement.txt
python handle/main.py 80
```

停止服务
```shell
ps aux | grep "handle/main.py" | grep -v grep | awk '{print $2}' | xargs kill -9
```
