# This is my study note!
# Git

## command

```
git config --list --show-origin
git config --global user.name "hxm_mac"
git config --global user.name "hexiaomingvip@icloud.com"
git config --global core.editor emacs 
git config --list
git add --help
cd /home/ubuntu/my_project/
git init
touch {1..5}.c LICENSE
git add *.c
git add LICENSE
git commit -m 'initial project version'
git clone https://github.com/SpencerHoGD/time-as-a-friend.git
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
cd #到~
mkdir .vim #有就不用新建.vim文件夹
cd .vim
vim vimrc #新建配置文件


# ubuntu

sudo apt update
sudo apt upgrade
setup ssh
	在云服务器控制台上复制mac设置好的公钥
	先把公钥文件内容复制到authorized_keys上
	cat id_rsa.pub >> authorized_keys
	修改sshd配置文件
	sudo vim /etc/ssh/sshd_config 
when i remake the remote system ubuntu, how should I ssh the remote from mac?
	* I should vim /$HOME/.ssh/known_hosts, and delete the old host key, and reconnect with ssh username@ip.

