
command:

```
sing-box run -c xxx.json
curl www.google.com
```

先将[[sing-box 1.8.0+版本迁移指南，Rule Set配置使用]] 里的客户端配置copy to raspi
debian12 mm:~/sing-box-data/client.json

first, look at "experimental":
之前这段是集成在 'clash_api' 里面的

接下来要看的是 'route' 路由配置

不再使用之前的 `geoip` `geosite` 的配置，未来会删除

增加了 `rule_set` 规则集的字段，这是一个数组，可以定义多个

经过艰难的设置，sing-box-raspi-client-cfg.json 成功了
scp 到 raspi 上，重命名为 config.json 

