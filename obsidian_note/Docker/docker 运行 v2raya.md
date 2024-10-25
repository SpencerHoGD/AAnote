
### v2raya

https://v2raya.org/en/docs/prologue/installation/docker/

```

docker run -d \
--restart=always \
--privileged \
--network=host \
--name v2raya \
-e V2RAYA_LOG_FILE=/tmp/v2raya.log \
-e V2RAYA_V2RAY_BIN=/usr/local/bin/v2ray \
-e V2RAYA_NFTABLES_SUPPORT=off \
-e IPTABLES_MODE=legacy \
-v /lib/modules:/lib/modules:ro \
-v /etc/resolv.conf:/etc/resolv.conf \
-v /etc/v2raya:/etc/v2raya \
mzz2017/v2raya
```

```
docker run --help
```
	 -d, --detach        Run container in background and print container ID
	 -e, --env list      Set environment variables
	 -v, --volume list   Bind mount a volume


```
docker run -d \
-p 2017:2017 \
-p 20170-20172:20170-20172 \
--restart=always \
--name v2raya \
-e V2RAYA_V2RAY_BIN=/usr/local/bin/v2ray \
-e V2RAYA_LOG_FILE=/tmp/v2raya.log \
-v /etc/v2raya:/etc/v2raya \
mzz2017/v2raya
```

```
docker container stats v2raya
```
```
docker container stop v2raya 
```
```
docker container rm v2raya
```

```
%s/ \\ / \\/g
```
去掉 '\'后面的一个空格
host mode use iptables:
```
docker run -d \
--restart=always \
--privileged \
--network=host \
--name v2raya \
-e V2RAYA_LOG_FILE=/tmp/v2raya.log \
-e V2RAYA_V2RAY_BIN=/usr/local/bin/v2ray \
-e V2RAYA_NFTABLES_SUPPORT=off \
-e IPTABLES_MODE=legacy \
-v /lib/modules:/lib/modules:ro \
-v /etc/resolv.conf:/etc/resolv.conf \
-v /etc/v2raya:/etc/v2raya \
mzz2017/v2raya
```

do not want to use the global transparent proxy:
```
docker run -d \
-p 2017:2017 \
-p 20170-20172:20170-20172 \
--restart=always \
--name v2raya \
-e V2RAYA_LOG_FILE=/tmp/v2raya.log \
-v /etc/v2raya:/etc/v2raya \
mzz2017/v2raya
```