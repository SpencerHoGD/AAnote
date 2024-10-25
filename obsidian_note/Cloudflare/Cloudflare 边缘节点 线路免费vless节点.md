

https://v2rayssr.com/worker-vless.html
https://github.com/V2RaySSR/Free-VLESS/?tab=readme-ov-file
https://github.com/zizifn/edgetunnel
Cloudflare Workers

复制v2rayssr, github 上的代码，改掉uuid，deploy。这个代码不行，换下面的
https://github.com/cmliu/edgetunnel/blob/main/_worker.js


在设置，添加域和路由，加上自定义域 vm.liamho.top
双击概述里的自定义域，可以访问。

uuid填到后面，可以访问配置文件。

```
https://vless-test-0841.spencerhogd.workers.dev/5d159ecc-d825-429a-8839-1b52bba0ff4a
```

```
/5d159ecc-d825-429a-8839-1b52bba0ff4a
```

将配置文件复制到v2rayN，没有连接成功，再说？

优选ip

104.16.119.181

```
  
################################################################
Subscribe / sub 订阅地址, 支持 Base64、clash-meta、sing-box 订阅格式
---------------------------------------------------------------
快速自适应订阅地址:
https://fe9b5676-a2aa-4b6a-8257-cd2dd0910205.8c98ef2b-bee2-470b-b759-9f5efbc10812.freeddns.org/vless-test-0841.spencerhogd.workers.dev/5d159ecc-d825-429a-8839-1b52bba0ff4a
https://fe9b5676-a2aa-4b6a-8257-cd2dd0910205.8c98ef2b-bee2-470b-b759-9f5efbc10812.freeddns.org/vless-test-0841.spencerhogd.workers.dev/5d159ecc-d825-429a-8839-1b52bba0ff4a?sub

Base64订阅地址:
https://fe9b5676-a2aa-4b6a-8257-cd2dd0910205.8c98ef2b-bee2-470b-b759-9f5efbc10812.freeddns.org/vless-test-0841.spencerhogd.workers.dev/5d159ecc-d825-429a-8839-1b52bba0ff4a?b64
https://fe9b5676-a2aa-4b6a-8257-cd2dd0910205.8c98ef2b-bee2-470b-b759-9f5efbc10812.freeddns.org/vless-test-0841.spencerhogd.workers.dev/5d159ecc-d825-429a-8839-1b52bba0ff4a?base64

clash订阅地址:
https://fe9b5676-a2aa-4b6a-8257-cd2dd0910205.8c98ef2b-bee2-470b-b759-9f5efbc10812.freeddns.org/vless-test-0841.spencerhogd.workers.dev/5d159ecc-d825-429a-8839-1b52bba0ff4a?clash

singbox订阅地址:
https://fe9b5676-a2aa-4b6a-8257-cd2dd0910205.8c98ef2b-bee2-470b-b759-9f5efbc10812.freeddns.org/vless-test-0841.spencerhogd.workers.dev/5d159ecc-d825-429a-8839-1b52bba0ff4a?sb
https://fe9b5676-a2aa-4b6a-8257-cd2dd0910205.8c98ef2b-bee2-470b-b759-9f5efbc10812.freeddns.org/vless-test-0841.spencerhogd.workers.dev/5d159ecc-d825-429a-8839-1b52bba0ff4a?singbox
---------------------------------------------------------------
################################################################
edgetunnel 配置信息
---------------------------------------------------------------
HOST: vless-test-0841.spencerhogd.workers.dev
UUID: 5d159ecc-d825-429a-8839-1b52bba0ff4a
FKID: 5a6476b3-515c-e2ce-ccf5-1dce8adb53af
UA: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36

CFCDN（访问方式）: 无法访问, 需要您设置 proxyIP/PROXYIP ！！！

您的订阅内容由 内置 addresses/ADD* 参数变量提供
ADD（TLS优选域名&IP）: 
  Join.my.Telegram.channel.CMLiussss.to.unlock.more.premium.nodes.cf.090227.xyz#加入我的频道t.me/CMLiussss解锁更多优选节点
  visa.cn:443
  www.visa.com:8443
  cis.visa.com:2053
  africa.visa.com:2083
  www.visa.com.sg:2087
  www.visaeurope.at:2096
  www.visa.com.mt:8443
  qa.visamiddleeast.com
  time.is
  www.wto.org:8443
  chatgpt.com:2087
  icook.hk
  [2606:4700::]#IPv6
ADDNOTLS（noTLS优选域名&IP）: 
  usa.visa.com:2095
  myanmar.visa.com:8080
  www.visa.com.tw:8880
  www.visaeurope.ch:2052
  www.visa.com.br:2082
  www.visasoutheasteurope.com:2086

SUBAPI（订阅转换后端）: https://SUBAPI.fxxk.dedyn.io
SUBCONFIG（订阅转换配置文件）: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_MultiMode.ini
---------------------------------------------------------------
################################################################
v2ray
---------------------------------------------------------------
vless://5d159ecc-d825-429a-8839-1b52bba0ff4a@visa.cn:80?encryption=none&security=&sni=vless-test-0841.spencerhogd.workers.dev&fp=randomized&type=ws&host=vless-test-0841.spencerhogd.workers.dev&path=%2F%3Fed%3D2560#edgetunnel
---------------------------------------------------------------
################################################################
clash-meta
---------------------------------------------------------------
- type: vless
  name: edgetunnel
  server: visa.cn
  port: 80
  uuid: 5d159ecc-d825-429a-8839-1b52bba0ff4a
  network: ws
  tls: false
  udp: false
  sni: vless-test-0841.spencerhogd.workers.dev
  client-fingerprint: randomized
  ws-opts:
    path: "/?ed=2560"
    headers:
      host: vless-test-0841.spencerhogd.workers.dev
---------------------------------------------------------------
################################################################
telegram 交流群 技术大佬~在线发牌!
https://t.me/CMLiussss
---------------------------------------------------------------
github 项目地址 Star!Star!Star!!!
https://github.com/cmliu/edgetunnel
---------------------------------------------------------------
################################################################
```