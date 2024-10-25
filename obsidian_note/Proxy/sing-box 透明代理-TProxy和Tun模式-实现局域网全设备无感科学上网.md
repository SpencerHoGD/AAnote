
by: elden
blog:
https://idev.dev/proxy/sing-box-tproxy.html

https://www.youtube.com/watch?v=mvOEesYsGBw&list=PLUelRCCHFxBkgoTlp4GkzMLdjBol59j9u&index=1

### sing-box 配置过程

跟着视频配置

透明代理核心配置是inbounds，outbounds 他配置了一个vless节点

打开官方文档 找到 [Tproxy](https://sing-box.sagernet.org/configuration/inbound/tproxy/)
除了必要的监听字段设置，只需要指定类型为Tproxy 就可以了。

nvim tproxy.yml , 将[Listen Fields](https://sing-box.sagernet.org/configuration/shared/listen/) 的字段拷贝到 yml 文件。
将端口该为12345
启用tcp快速打开 tcp_fast_open
utp分段 udp_fragment 等等，配置如下
```json
{
      "listen": "::",
      "listen_port": 12345,
      "tcp_fast_open": true,
      "tcp_multi_path": false,
      "udp_fragment": true,
      "udp_timeout": "5m",
      "sniff": true,
      "sniff_override_destination": false,
      "sniff_timeout": "300ms",
      "domain_strategy": "prefer_ipv4",
    }

```
