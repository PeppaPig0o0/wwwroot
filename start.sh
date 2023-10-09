#!/bin/bash

# 启动第一个uWSGI应用程序
uwsgi -i /www/wwwroot/peppa/peppa/peppa.ini &

# 等待一段时间（例如5秒，根据实际情况调整）
sleep 5

# 启动第二个uWSGI应用程序
uwsgi -i /www/wwwroot/job/job/job.ini &

# 防止脚本退出，以保持容器运行
tail -f /dev/null
