# study_note

## Git

```
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

```
ssh-keygen -t rsa -C "hexiaomingvip@icloud.com"
cat ~/.ssh/id_rsa.pub
ssh -T git@github.com
git remote -v
git remote set-url origin git@github.com:SpencerHoGD/awesome.git

ssh config
Host 51
	HostName 148.70.171.51
	User ubuntu
	Port 22

[SSH个人配置过程](https://www.cnblogs.com/readleafblackrain/p/3970735.html)

type to use:
ssh 51
```

find / -name sshd
检查发现 /usr/sbin/sshd 是存在的，那么，有没有包含进去路径呢
setup ssh
	在云服务器控制台上复制mac设置好的公钥
	先把公钥文件内容复制到authorized_keys上
	cat id_rsa.pub >> authorized_keys
	修改sshd配置文件
	sudo vim /etc/ssh/sshd_config 
when i remake the remote system ubuntu, how should I ssh the remote from mac?
	* I should vim /$HOME/.ssh/known_hosts, and delete the old host key, and reconnect with ssh username@ip.



## vim

配置vim文件

cd #到~
mkdir .vim #有就不用新建.vim文件夹
cd .vim
vim vimrc #新建配置文件

vimtutor 是一个很全面的介绍

[vim教程网，一个95后程序媛做的教程](https://vimjc.com)
[vim列块操作](https://blog.csdn.net/hexiechina2010/article/details/46907149)
[vim配置，阮一峰](http://www.ruanyifeng.com/blog/2018/09/vimrc.html)

### vim search
/ search cmd
n next one
N last one

### vim scroll window
^E - scroll the window down
^Y - scroll the window up
^F - scroll Forward one page
^B - scroll Backward one page
H - move cursor to the highest of the window
M - move cursor to the middle of the window
L - move cursor to the bottom of the window
gg - go to the top of the file
G - go to the end of the file

### vim inline movement

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

### vim视窗操作
vim可以在一个界面里打开多个窗口进行编辑，这些编辑窗口成为vim的视窗。
打开的方法有很多种，比如可以用：
命令行模式下输入：
- :new
- :sp or sp 1.md
- :vsp or vsp 2.md

### 视窗移动
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


## ubuntu

sudo apt update
sudo apt upgrade


    获取当前在您的系统上运行的服务列表：

systemctl | grep running

    要停止服务，请输入以下命令，比如我要停止apache运行，则用下面的命令，替换为要停止的服务apache2的名称：

systemctl stop apache2



[在Ubuntu 18.04系统中启用SSH登录的方法](https://ywnz.com/linuxjc/2347.html)

输入sudo apt install openssh-server，发现已经安装好了。

sudo service ssh status


## 箴言

轻财足以聚人，律己足以服人，量宽足以得人，身先足以率人。

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
n
删除匿名用户：删除 y
n
mysql -u root -p

##  archlinux

### install X

sudo pacman -S xorg xorg-server
sudo pacman -Qs lightdm


