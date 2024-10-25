
安装raspi arm64 v2raya的时候，用到了添加的链接

https://v2raya.org/en/docs/prologue/installation/debian/

#### Add public key[](https://v2raya.org/en/docs/prologue/installation/debian/#add-public-key)

`wget -qO - https://apt.v2raya.org/key/public-key.asc | tee /etc/apt/keyrings/v2raya.asc`

#### Add V2RayA software source[](https://v2raya.org/en/docs/prologue/installation/debian/#add-v2raya-software-source)

`echo "deb [signed-by=/etc/apt/keyrings/v2raya.asc] https://apt.v2raya.org/ v2raya main" | tee /etc/apt/sources.list.d/v2raya.list

apt update`

#### Install V2RayA[](https://v2raya.org/en/docs/prologue/installation/debian/#install-v2raya-1)

`sudo apt install v2raya v2ray ## you can install xray package ins`