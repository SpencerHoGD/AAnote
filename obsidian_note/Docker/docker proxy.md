## 使用方法②

**一键设置镜像加速：**修改文件 /etc/docker/daemon.json（如果不存在则创建）
  
  /etc/docker/daemon.json
  
**修改JSON文件 更改为以下内容 然后保存**
  
  {"registry-mirrors": ["https://dockerpull.com"]}
  
**保存好之后 执行以下两条命令**
  
```sh
sudo systemctl daemon-reload #重载systemd管理守护进程配置文件
sudo systemctl restart docker #重启 Docker 服务
```