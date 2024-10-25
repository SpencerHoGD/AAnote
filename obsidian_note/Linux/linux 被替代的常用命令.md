
常用命令
```bash
ip a(ddr) # 
ip r(oute) # 显示和修改路由表
ip neigh # 用于查看和管理地址解析协议表（ARP 表）
ss -tuln # 查看网络连接
systemctl reboot
systemctl poweroff
systemctl halt
systemctl start apache2 # 使用 systemctl 代替 service
fdisk /dev/sda # 使用 fdisk 处理 MBR (对于 GPT deprecated)
gdisk /dev/sda # 使用 gdisk 处理 GPT 分区
hostnamectl set-hostname newhostname # 使用 hostnamectl 代替
stat #`df -i` 用于显示文件系统的 inode 使用情况，而 `stat` 提供了更细粒度的文件系统信息。
pgrep apache2 # 查找进程
kill or pkill
systemctl enable mytask.timer # 使用 systemd.timer 创建定时任务 cron被替代
passwd -l 锁定账户
systemctl get-default # 查看运行目标的系统级别
systemctl list-units --type=target # 使用 systemctl 查看计算机的运行软硬件、基本服务情况。
# 使用 ip 命令启用或禁用网络接口
ip link set eth0 up
ip link set eth0 down
timedatectl status # 使用 timedatectl 查看系统时间
useradd
```

在 Linux 中，随着系统和工具的进化，一些常用命令或工具逐渐被标记为过时（deprecated），并由更现代的工具或命令替代。以下是一些已经被弃用或逐渐被替代的常用 Linux 命令和工具：

### 1. **ifconfig**
   - **Deprecated**: 已被标记为弃用。
   - **替代工具**: `ip`
   - 说明: `ifconfig` 用于配置网络接口，现在被更强大且功能丰富的 `ip` 工具取代。`ip` 提供了更详细的网络管理功能。
   - 示例替代:
     ```bash
     # 使用 ip 命令代替 ifconfig
     ip addr 
     ```

### 2. **route**
   - **Deprecated**: 已弃用。
   - **替代工具**: `ip route`
   - 说明: `route` 用于显示和修改路由表，现在由 `ip route` 替代。
   - 示例替代:
     ```bash
     # 使用 ip route 查看路由
     ip route 
     ```

### 3. **netstat**
   - **Deprecated**: 已弃用。
   - **替代工具**: `ss`
   - 说明: `netstat` 用于显示网络连接和监听端口，现由 `ss` 替代，后者更高效且提供更多功能。
   - 示例替代:
     ```bash
     # 使用 ss 查看网络连接
     ss -tuln
     ```

### 4. **arp**
   - **Deprecated**: 已弃用。
   - **替代工具**: `ip neigh`
   - 说明: `arp` 命令用于查看和管理地址解析协议表（ARP 表），已被 `ip` 的子命令 `ip neigh` 取代。
   - 示例替代:
     ```bash
     # 使用 ip 命令代替 arp
     ip neigh
     ```

### 5. **halt, poweroff, reboot**
   - **Deprecated**: 已弃用（部分发行版）。
   - **替代工具**: `systemctl`
   - 说明: 这些命令用于关闭或重启系统，现在推荐使用 `systemctl` 来管理系统电源状态。
   - 示例替代:
     ```bash
     # 使用 systemctl 代替这些命令
     sudo systemctl halt
     sudo systemctl poweroff
     sudo systemctl reboot
     ```

### 6. **service**
   - **Deprecated**: 已弃用（在基于 systemd 的系统中）。
   - **替代工具**: `systemctl`
   - 说明: `service` 命令用于启动、停止或检查服务状态，现已被 `systemctl` 替代，尤其是在使用 `systemd` 的系统中。
   - 示例替代:
     ```bash
     # 使用 systemctl 代替 service
     systemctl start apache2
     ```

### 7. **fdisk (MBR-specific)**
   - **Deprecated**: 在处理 GPT 分区时不推荐使用。
   - **替代工具**: `gdisk` 或 `parted`
   - 说明: `fdisk` 传统上用于管理分区，但它对 GPT 分区表支持有限，推荐使用 `gdisk` 或 `parted` 来处理 GPT 分区。
   - 示例替代:
     ```bash
     # 使用 fdisk 处理 MBR (对于 GPT deprecated)
     fdisk /dev/sda
     
     # 使用 gdisk 处理 GPT 分区
     gdisk /dev/sda
     ```

### 8. **chkconfig**
   - **Deprecated**: 已弃用（在 `systemd` 系统中）。
   - **替代工具**: `systemctl`
   - 说明: `chkconfig` 用于管理系统服务的开机自启动，现由 `systemctl` 替代。
   - 示例替代:
     ```bash
     # 使用 chkconfig 管理服务 (deprecated)
     chkconfig apache2 on
     
     # 使用 systemctl 代替 chkconfig
     systemctl enable apache2
     ```

### 9. **at**
   - **Deprecated**: 部分系统已弃用。
   - **替代工具**: `systemd.timer`
   - 说明: `at` 命令用于计划一次性任务，部分发行版逐渐弃用它，推荐使用 `systemd` 定时器 (`systemd.timer`) 来替代。

### 10. **hostname**
   - **Deprecated**: 部分系统已弃用。
   - **替代工具**: `hostnamectl`
   - 说明: `hostname` 用于查看和设置主机名，现在推荐使用 `hostnamectl` 命令，特别是在 `systemd` 系统中。
   - 示例替代:
     ```bash
     # 使用 hostnamectl 代替
     hostnamectl set-hostname newhostname
     ```


### 11. **df -i**
   - **Deprecated**: 不直接弃用，但在某些系统上已减少使用。
   - **替代工具**: `stat`
   - 说明: `df -i` 用于显示文件系统的 inode 使用情况，而 `stat` 提供了更细粒度的文件系统信息。

### 12. **pidof**
   - **Deprecated**: 已弃用（部分系统）。
   - **替代工具**: `pgrep`
   - 说明: `pidof` 用于查找进程 ID，而 `pgrep` 提供更灵活和更强大的进程查找功能。
   - 示例替代:
     ```bash
     # 使用 pidof 查找进程 (deprecated)
     pidof apache2
     
     # 使用 pgrep 代替
     pgrep apache2
     ```

### 13. **killall5**
   - **Deprecated**: 已弃用（部分系统）。
   - **替代工具**: `kill`
   - 说明: `killall5` 是 SysV 风格的命令，用于杀死所有进程，而 `kill` 或 `pkill` 提供了更多控制选项。

### 14. **cron.daily, cron.weekly, cron.monthly**
   - **Deprecated**: 被替代，尤其在 `systemd` 系统中。
   - **替代工具**: `systemd.timer`
   - 说明: 传统的 `cron` 作业已逐渐被 `systemd` 的定时器机制 (`systemd.timer`) 取代，后者提供更强的计划任务管理。
   - 示例替代:
     ```bash
     # 使用 systemd.timer 创建定时任务
     systemctl enable mytask.timer
     ```

### 15. **usermod -L (锁定账户)**
   - **Deprecated**: 在某些系统中，使用 `passwd` 锁定账户更为推荐。
   - **替代工具**: `passwd -l`
   - 说明: `usermod -L` 用于锁定用户账户，`passwd -l` 是更现代的方法。

### 16. **runlevel**
   - **Deprecated**: 在 `systemd` 系统中弃用。
   - **替代工具**: `systemctl get-default`
   - 说明: `runlevel` 命令用于查看当前的运行级别，`systemctl` 提供了更现代化的方式来管理和查看系统目标（runlevel 的替代）。
   - 示例替代:
     ```bash
     # 使用 runlevel 查看运行级别 (deprecated)
     runlevel
     
     # 使用 systemctl 查看默认目标
     systemctl get-default
     ```

### 17. **halt --force**
   - **Deprecated**: 被 `systemctl` 替代。
   - **替代工具**: `systemctl poweroff --force`
   - 说明: `halt --force` 用于强制系统关闭，现在建议使用 `systemctl` 来管理系统关闭行为。
   - 示例替代:
     ```bash
     # 使用 halt --force (deprecated)
     halt --force
     
     # 使用 systemctl 强制关闭系统
     systemctl poweroff --force
     ```

### 18. **init**
   - **Deprecated**: 已弃用（在 `systemd` 系统中）。
   - **替代工具**: `systemctl`
   - 说明: `init` 是 SysV 风格的初始化工具，现在由 `systemd` 替代。
   - 示例替代:
     ```bash
     # 使用 init 改变运行级别 (deprecated)
     init 3
     
     # 使用 systemctl 改变系统目标
     systemctl isolate multi-user.target
     ```

### 19. **who -r**
   - **Deprecated**: 部分系统中弃用。
   - **替代工具**: `systemctl`
   - 说明: `who -r` 用于查看当前运行级别，`systemctl` 提供了类似功能。
   - 示例替代:
     ```bash
     # 使用 who -r 查看运行级别 (deprecated)
     who -r
     
     # 使用 systemctl 查看默认目标
     systemctl list-units --type=target
     ```

### 20. **ifup/ifdown**
   - **Deprecated**: 被 `ip` 和 `nmcli` 逐渐取代。
   - **替代工具**: `ip` 或 `nmcli`
   - 说明: `ifup` 和 `ifdown` 用于启用和禁用网络接口，现在推荐使用 `ip` 或 NetworkManager 的 `nmcli` 命令。
   - 示例替代:
     ```bash
     # 使用 ifup/ifdown 启用或禁用网络 (deprecated)
     ifup eth0
     ifdown eth0
     
     # 使用 ip 命令
     sudo ip link set eth0 up
     sudo ip link set eth0 down
     
     # 或使用 nmcli 命令
     nmcli device connect eth0
     nmcli device disconnect eth0
     ```

### 21. **hwclock**
   - **Deprecated**: 部分发行版已弃用。
   - **替代工具**: `timedatectl`
   - 说明: `hwclock` 用于管理硬件时钟，而 `timedatectl` 提供了更现代的系统时钟和时间同步管理工具。
   - 示例替代:
     ```bash
     # 使用 hwclock 查看硬件时钟 (deprecated)
     hwclock --show
     
     # 使用 timedatectl 查看系统时间
     timedatectl status
     ```

### 22. **adduser**
   - **Deprecated**: 部分发行版弃用。
   - **替代工具**: `useradd`
   - 说明: 在某些系统中，`adduser` 被弃用，推荐使用原生的 `useradd` 命令。

### 23. **service --status-all**
   - **Deprecated**: 被 `systemctl` 替代。
   - **替代工具**: `systemctl list-units`
   - 说明: `service --status-all` 用于查看系统服务的状态，而 `systemctl list-units` 提供了更现代化的服务管理方法。

