# mount usb
```sh
sudo fdisk -l
mkdir /media/usb-drive
mount /dev/sdc1 /media/usb-drive/
mount | grep sdc1 # for example,To check whether your USB drive has been mounted correctly 
cd /media/usb-drive
umount /media/usb-drive
```
## Permanent USB Mount in Linux
https://linuxconfig.org/howto-mount-usb-drive-in-linux
```sh
ls -l /dev/disk/by-uuid/*
# In order to mount your USB in Linux permanently after reboot add the following line into your /etc/fstab config file:
# /dev/disk/by-uuid/8765-4321    /media/usb-drive         vfat    defaults   0   0
mount -a
```

# sing-box
https://github.com/SagerNet/sing-box.git
https://www.youtube.com/watch?v=mvOEesYsGBw&list=PLUelRCCHFxBkgoTlp4GkzMLdjBol59j9u&index=2

### sing-box install.sh
for the script content and inspect what it did.
```sh
#!/bin/bash

set -e -o pipefail

ARCH_RAW=$(uname -m)
case "${ARCH_RAW}" in
    'x86_64')    ARCH='amd64';;
    'x86' | 'i686' | 'i386')     ARCH='386';;
    'aarch64' | 'arm64') ARCH='arm64';;
    'armv7l')   ARCH='armv7';;
    's390x')    ARCH='s390x';;
    *)          echo "Unsupported architecture: ${ARCH_RAW}"; exit 1;;
esac

VERSION=$(curl -s https://api.github.com/repos/SagerNet/sing-box/releases/latest \
    | grep tag_name \
    | cut -d ":" -f2 \
    | sed 's/\"//g;s/\,//g;s/\ //g;s/v//')

curl -Lo sing-box.pkg.tar.zst "https://github.com/SagerNet/sing-box/releases/download/v${VERSION}/sing-box_${VERSION}_linux_${ARCH}.pkg.tar.zst"
sudo pacman -U sing-box.pkg.tar.zst
rm sing-box.pkg.tar.zst
```
### config and run sing-box
config is tun.json

### enable and start
```sh
# Tun模式设置
# Tun模式需要开启ip转发
echo 1 > /proc/sys/net/ipv4/ip_forward #check first
# sing-box配置系统服务
# /etc/systemd/system/sing-box@.service
# script is in repo https://github.com/SagerNet/sing-box/tree/dev-next/release/config/sing-box@.service
vim /etc/systemd/system/sing-box@.service
# and paste content below

[Unit]
Description=sing-box service
Documentation=https://sing-box.sagernet.org
After=network.target nss-lookup.target network-online.target

[Service]
CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_BIND_SERVICE CAP_SYS_PTRACE CAP_DAC_READ_SEARCH
AmbientCapabilities=CAP_NET_ADMIN CAP_NET_BIND_SERVICE CAP_SYS_PTRACE CAP_DAC_READ_SEARCH
ExecStart=/usr/bin/sing-box -D /var/lib/sing-box-%i -c /etc/sing-box/%i.json run
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=10s
LimitNOFILE=infinity

[Install]
WantedBy=multi-user.target

# next
sudo systemctl daemon-reload
mv sing-box /usr/bin/
mkdir /etc/sing-box && mv tun.json /etc/sing-box/

sudo systemctl start sing-box@tun.service
sudo systemctl status sing-box@tun.service
sudo systemctl enable sing-box@tun.service
journalctl -xe
```


## Window manager DWM

```sh
git clone https://git.suckless.org/dwm
```

### dwm complete setup for beginners on Arch linux ( Virtual Box )
https://www.youtube.com/watch?v=6pUDzv49M68

```sh
neofetch
sudo pacman -Sy xorg xorg-xinit # xf86-video-fbdev
# First, identify the graphics card (the Subsystem output shows the specific model):
lspci -v | grep -A1 -e VGA -e 3DO
# Then, install an appropriate driver. You can search the package database for a complete list of open-source video drivers:
sudo pacman -Ss xf86-video
# picom for transparent
sudo pacman -Sy feh picom polybar python-pywal xf86-video-amdgpu arch-wiki-docs
sudo pacman -S ttf-jetbrains-mono 
mkdir suckless
git clone https://git.suckless.org/dwm # and dmenu st
make
sudo make clean install

# need .xintrc file, we useing xorg server
cp /etc/X11/xinit/xinitrc ./.xinitrc # xinitrc is below

startx

xrandr
xrandr --output VGA-1 --mode 1920x1080 # for example

sudo pacman -S thunar # file explore like ranger
```

in the .xinitrc
```sh
xrandr --output VGA-1 --mode 1920x1080 &  # for example
polybar &
~/.fehbg &
picom &
wal -n -R  & # what is it
exec dwm
```

polybar setup example
```sh
#!/bin/bash

# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use
# polybar-msg cmd quit

# Launch Polybar, using default config location ~/.config/polybar/config.ini
polybar mybar 2>&1 | tee -a /tmp/polybar.log & disown

echo "Polybar launched..."
```