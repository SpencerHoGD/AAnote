
https://github.com/Toperlock/sing-box-subscribe?tab=readme-ov-file#页面操作步骤

[[Cloudflare 边缘节点 线路免费vless节点]] 
部署的以下
[订阅地址](https://vless-test-0841.spencerhogd.workers.dev/5d159ecc-d825-429a-8839-1b52bba0ff4a)
~~有sing-box的地址，可以不用转换，连连看

已经用docker 安装了

现在试试python env 试一下

项目clone到了mm:$HOME/github

'\'后面不能有空格
```
docker run -d \
--restart=unless-stopped \
--privileged \
--network=host \
--name sbox-sub \
sbox-sub
```


本地python执行脚本命令：

```
python main.py
```

或者你可以直接带template_index参数选定模板，0表示第一个模板(no flask不支持此参数)

```
python main.py --template_index=0
```

支持Docker
server mm  # 192.168.1.6
cd ~/github/sing-box-subscribe
```
docker build --tag 'sing-box' .
docker run -p 5000:5000 sing-box:latest
```
