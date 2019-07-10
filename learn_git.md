# Git command example

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

```
ssh-keygen -t rsa -C "hexiaomingvip@icloud.com"
cat ~/.ssh/id_rsa.pub
ssh -T git@github.com
git remote -v
git remote set-url origin git@github.com:SpencerHoGD/awesome.git

```