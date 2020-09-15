# study_note


<!-- TOC GFM -->

* [idea](#idea)
* [Git](#git)
* [SSH](#ssh)
* [vim](#vim)
    - [vim search](#vim-search)
    - [vim replacement](#vim-replacement)
    - [vim scroll window](#vim-scroll-window)
    - [vim inline movement](#vim-inline-movement)
    - [vim视窗操作](#vim视窗操作)
    - [视窗移动](#视窗移动)
    - [ubuntu](#ubuntu)
* [NewLinux](#newlinux)
* [archlinux](#archlinux)
    - [install X](#install-x)
    - [lightdm](#lightdm)
    - [yay](#yay)
    - [linux 脚本](#linux-脚本)
    - [dwm](#dwm)
    - [pacths](#pacths)
* [其他](#其他)
    - [箴言](#箴言)
    - [经典故事-制度的力量](#经典故事-制度的力量)
* [股票](#股票)
    - [北斗卫星](#北斗卫星)
    - [游资](#游资)
        + [龙飞虎](#龙飞虎)
    - [充电桩](#充电桩)
    - [太阳能板](#太阳能板)
* [TODO](#todo)

<!-- /TOC -->


## idea

解决问题app

## Git

```sh
git config --list --show-origin
git config --global user.name "hxm_mac"
git config --global user.email "hexiaomingvip@icloud.com"
git config --global core.editor vim
git config --list
git add --help
cd /home/ubuntu/my_project/
git init
touch {1..5}.c LICENSE
git add *.c
git add LICENSE
git commit -m 'initial project version'
git clone https://github.com.cnpmjs.org/SpencerHoGD/AAnote.git
git status
```

[初次使用git配置以及git如何使用ssh密钥（将ssh密钥添加到github）](https://www.cnblogs.com/superGG1990/p/6844952.html)

## SSH

```sh
ssh-keygen -t rsa -C "hexiaomingvip@icloud.com"
cat ~/.ssh/id_rsa.pub
ssh -T git@github.com
git remote -v
git remote set-url origin git@github.com:SpencerHoGD/awesome.git
```

ssh config

```sh
Host 51
	HostName 148.70.171.51
	User ubuntu
	Port 22
```

```
[SSH个人配置过程](https://www.cnblogs.com/readleafblackrain/p/3970735.html)
type to use:
ssh 51

find / -name sshd

检查发现 /usr/sbin/sshd 是存在的，那么，有没有包含进去路径呢

setup ssh

在云服务器控制台上复制mac设置好的公钥

先把公钥文件内容复制到authorized_keys上

cat id_rsa.pub >> authorized_keys

修改sshd配置文件

sudo vim /etc/ssh/sshd_config 

when i remake the remote system ubuntu, how should I ssh the remote from mac?

I should vim /$HOME/.ssh/known_hosts, and delete the old host key, and reconnect with ssh username@ip.
```


## vim

vimtutor 是一个很全面的介绍

[vim教程网，一个95后程序媛做的教程](https://vimjc.com)

[vim列块操作](https://blog.csdn.net/hexiechina2010/article/details/46907149)

[vim配置，阮一峰](http://www.ruanyifeng.com/blog/2018/09/vimrc.html)

### vim search

```
/ search cmd
n next one
N previous one
```

### vim replacement

:%s /alskdf/alskdjf g

### vim scroll window

```
^E - scroll the window down
^Y - scroll the window up
^F - scroll Forward one page
^B - scroll Backward one page
H - move cursor to the highest of the window
M - move cursor to the middle of the window
L - move cursor to the bottom of the window
gg - go to the top of the file
G - go to the end of the file
```

### vim inline movement

```
w - move to the head of next word
b - move to the head of backward word
e - move to the tail of next word
ge - move to the head backward word

f - find and move to the right on the letter # 3fa
F - find and move to the left on the letter
t - find and move to the right before the letter
T - find and move to the left before the letter
; - do it once again
, - do it once again in reverse direction
```

### vim视窗操作

vim可以在一个界面里打开多个窗口进行编辑，这些编辑窗口成为vim的视窗。

打开的方法有很多种，比如可以用：

命令行模式下输入：

```
- :new
- :sp or sp 1.md
- :vsp or vsp 2.md
```

### 视窗移动

```
- Ctrl+w   q : quit
- Ctrl+w   o : open new window on top
- Ctrl+w   O : open new window on top
- Ctrl+w   j : move to the down window
- Ctrl+w   k : move to the up window
- Ctrl+w   h : move to the left window
- Ctrl+w   l : move to the right window
- Ctrl+w   J : move current window down
- Ctrl+w   k : move current window up
- Ctrl+w   H : move current window left
- Ctrl+w   L : move current window right
- Ctrl+w   - : - the height of the window
- Ctrl+w   + : + the heigit of the window

创建加密文档
vim -x filename

外部命令
:ls
:rm FILENAME 
;w FILENAME : 另存为
```


### ubuntu

sudo apt update
sudo apt upgrade

获取当前在您的系统上运行的服务列表：

`systemctl | grep running`

要停止服务，请输入以下命令，比如我要停止apache运行，则用下面的命令，替换为要停止的服务apache2的名称：

`systemctl stop apache2`

[在Ubuntu 18.04系统中启用SSH登录的方法](https://ywnz.com/linuxjc/2347.html)

输入sudo apt install openssh-server，发现已经安装好了。

sudo service ssh status




## NewLinux

1. sudo apt update
2. sudo apt upgrade
3. 安装zsh, sudo apt install zsh
4. 安装 oh-my-zsh, 是一个美化插件,[gitub, oh-my-zsh](https://github.com/robbyrussell/oh-my-zsht). 好看的同时，以很简洁的方式告诉你很多有用的信息。 
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
上面是github上的安装命令。
5. 把自己的配置文件从github上克隆下来。（那么，我也要自己建一个仓库设置配置文件）。
6. 先把覆盖.zshrc,
	 ``` 
	cp -f .config/.zshrc ~/
	```
7. sudo ufw status

sudo ufw allow OpenSSH

sudo ufw enable

sudo ufw status

安装apache2

sudo apt install apache2 -y

sudo ufw app list

sudo ufw allow in "Apache Full"

浏览器输入ip地址或者域名就可以访问了。

默认index页面在 /var/www/html/index.html

sudo apt install mysql-server

rootuser Ni111

sudo mysql_secure_installation

删除匿名用户：删除 y

mysql -u root -p

## archlinux

sudo systemctl list-unit-files

tlp #笔记本电脑省电？

### install X

sudo pacman -S xorg xorg-server

### lightdm

sudo pacman -Qs lightdm

sudo vim /etc/lightdm/lightdm.conf # 编辑配置文件

sudo systemctl enable lightdm

sudo systemctl start lightdm # 可以直接启动试一试

pacman -Qs yay

### yay

yay -S google-chrome

### linux 脚本

### dwm

tar -zxvf # 解压

### pacths


## 其他

### 箴言

轻财足以聚人，律己足以服人，量宽足以得人，身先足以率人。

### 经典故事-制度的力量

- 故事一：合格率的检查制度

二战期间，美国空军降落伞的合格率为99.9%，这就意味着从概率上来说，每一千个跳伞的士兵中会有一个因为降落伞不合格而丧命。

军方要求厂家必须让合格率达到100%才行。

厂家负责人说他们竭尽全力了，99.9%已是极限，除非出现奇迹。

军方（也有人说是巴顿将军）就改变了检查制度，每次交货前从降落伞中随机挑出几个，让厂家负责人亲自跳伞检测。

从此，奇迹出现了，降落伞的合格率达到了百分之百。

- 故事二：付款方式

英国将澳洲变成殖民地之后，因为那儿地广人稀，尚未开发，英政府就鼓励国民移民到澳洲，可是当时澳洲非常落后，没有人愿意去。

英国政府就想出一个办法，把罪犯送到澳洲去。

这样一方面解决了英国本土监狱人满为患的问题，另一方面也解决了澳洲的劳动力问题。

还有一条，他们以为把坏家伙们都送走了，英国就会变得更美好了。

英国政府雇佣私人船只运送犯人，按照装船的人数付费，多运多赚钱。

很快政府发现这样做有很大的弊端，就是罪犯的死亡率非常之高，平均超过了百分之十，最严重的一艘船死亡率达到了惊人的百分之三十七。

政府官员绞尽脑汁想降低罪犯运输过程中的死亡率，包括派官员上船监督，限制装船数量等等，却都实施不下去。

最后，他们终于找到了一劳永逸的办法，就是将付款方式变换了一下：

“由根据上船的人数付费改为根据下船的人数付费。船东只有将人活着送达澳洲，才能赚到运送费用。”

新政策一出炉，罪犯死亡率立竿见影地降到了百分之一左右。

后来船东为了提高生存率还在船上配备了医生。


- 故事三：抽水马桶的清洁标准

某日本高级酒店，检测客房抽水马桶是否清洁的标准是：由清洁工自己从马桶中舀一杯水喝一口。

可以想象，这样的马桶会干净到什么程度。

故事四：粥的分配制度

七个人住在一起，每天分一大桶粥。

要命的是，粥每天都是不够的。

一开始，他们抓阄决定谁来分粥，每天轮一个。

于是乎，每周下来，他们只有一天是饱的，就是自己分粥的那一天。

后来他们开始推选出一个口口声声道德高尚的人出来分粥。

大权独揽，没有制约，也就会产生腐败。

大家开始挖空心思去讨好他，互相勾结，搞得整个小团体乌烟瘴气。

然后大家开始组成三人的分粥委员会及四人的评选委员会，互相攻击扯皮下来，粥吃到嘴里全是凉的。

最后想出来一个方法：

“轮流分粥，但分粥的人要等其它人都挑完后拿剩下的最后一碗。为了不让自己吃到最少的，每人都尽量分得平均，就算不平，也只能认了。”

大家快快乐乐，和和气气，日子越过越好。


- 故事五：互助与共赢的天堂

有一位行善的基督教徒，去世后向上帝提出一个要求，要求上帝领去参观地狱和天堂，看看究竟有什么区别。

到了地狱，看到一张巨大的餐桌，摆满丰盛的佳肴。

心想：地狱生活挺不错的。

过一会儿，用餐的时间到了……

只见一群骨瘦如柴，奄奄一息的人围坐在香气四溢的肉锅前，只因手持的汤勺把儿太长，尽管他们争着抢着往自己嘴里送肉，可就是吃不到，又馋又急又饿。

上帝说，这就是地狱。

他们走进另一个房间，这里跟地狱一般无二，同样飘溢着肉汤的香气，同样手里拿着的是特别长的汤勺。

但是，这里的人个个红光满面，精神焕发。原来他们个个手持特长勺把肉汤喂进对方嘴里。

上帝说，这就是天堂。

同样的人，不同的制度，可以产生不同的文化和氛围以及差距巨大的结果。

一个好的制度可以使人的坏念头受到抑制，而坏的制度会让人的好愿望四处碰壁。

建立起将结果和个人责任和利益联系到一起的制度，能解决很多社会问题。

这就是制度的力量。


## 股票

### 北斗卫星

### 游资

#### 龙飞虎

> 换手决定高度，很多游资票都是靠板板换手前进的

### 充电桩

### 太阳能板


## TODO

- [x] vim markdown preview
- [ ] learn tmux
- [x] learn fish: not for now
- [x] learn fzf: **not fully understand**, later.
- [x] learn vimium: a browser add-on job done
- [x] learn Node.js: use pacman package node to build darkreader.
    - [x] npm install
    - [x] npm run release
- [x] learn Node.js: use pacman package node to build darkreader.
- [x] miniconda
    - [x] read the conda docs
- [x] GIMP: photo manipulation
- [x] evince pdf jpg...reader.
    - [x] used for ranger default pdf reader
- [x] set zsh autosuggestion shotcut '<c-l>'
- [x] zsh scroll shotcut: shift + PgUp
- [x] alsamixer: about sound
- [x] [saladict](https://github.com/crimx/ext-saladict) try to built from
  source code with conda: done.clone the newest repo, and follow the
  instrations. conda no help
- [ ] 鸿蒙os2.0


