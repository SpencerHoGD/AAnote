- [ ] move ~/filelist.md to ~/.config/nvim/filelist.md
- [ ] change i3 font and size
- [ ] read i3 user guide
    [i3-user-guide](https://i3wm.org/docs/userguide.html#_opening_terminals_and_moving_around) read i3 user guide
- [ ] add three add on to the git repo
- [ ] hwdetect

- [ ] snow flake

chan ping jingli
design thinking
jingyi chuangye
mingjie guanli


cpu temperature

```sh
cat /sys/class/thermal/thermal_zone0/temp

or

echo $[$(cat /sys/class/thermal/thermal_zone0/temp)/1000]°

watch -n 0.1 echo CPU: $[$(cat /sys/class/thermal/thermal_zone0/temp)/1000]°
```


- hardinfo
- betterlockscreen

[i3lock](https://github.com/i3/i3lock)


- scratchpad

move the currently focused window to the scratchpad

'bindsym $mod+Shift+minus move scratchpad'

Show the next scratchpad window or hide the focused scratchpad window.

If there are multiple scratchpad windows, this command cycles through them.

'bindsym $mod+minus scratchpad show'

