
github:
[MHSanaei/3x-ui: Xray panel supporting multi-protocol multi-user expire day & traffic & ip limit (Vmess & Vless & Trojan & ShadowSocks & Wireguard) (github.com)](https://github.com/MHSanaei/3x-ui)

bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)


面板：
Username: hxm
Password: keepass

Username: ffjQLABCsU
Password: bUT48Q7wSN
Port: 49252
WebBasePath: qz1q9dN64VKSoXV



me.liamho.top

66.225.228.161

08b8e71b-09fb-4930-b6b5-a7b8c903c3d
08b8e71b

a52998390d815dfcd5e5dea67f1f3ab351148
spencerhogd@Gmail.com

/root/me.liamho.top/fullchain.pem
/root/me.liamho.top/privkey.pem

面板登录：
申请3x-ui的18  SSL 证书后
cloudflare DNS 代理状态的小云朵关掉，才能使用证书，因为只是DNS代理，没有涉及到


面板设置关键：

x-ui，先申请18的SSL, 在申请19的cloudflare SSL
填入相同的域名，例如：m.liamho.top

设置好面板上的uuid，再填入yaml

```yaml
  - {name: us-la, server: 66.225.228.161, port: 443, client-fingerprint: randomized, type: vmess, uuid: c3a536df-de94-4d2a-90d8-8214431e931a, alterId: 0, cipher: auto, tls: true, tfo: false, skip-cert-verify: false, network: ws, ws-opts: {path: /c3a536df, headers: {Host: m.liamho.top}}}
```