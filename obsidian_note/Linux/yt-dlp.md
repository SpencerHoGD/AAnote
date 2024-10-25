
下载播放列表其中的一首歌，可以下载播放列表里的全部

```sh
alias ya="yt-dlp -f 'bestaudio/best' --format 'bestaudio[ext!=webm]'"

# Taylor Swift - Fortnight (feat. Post Malone) (Official Music Video) for example:
ya https://www.youtube.com/watch?v=q3zqJs7JUCQ&list=PLMC9KNkIncKuBNgb0KPHnybPM5wKJxTYH&index=38
```

 [How to download only subtitles of videos using youtube-dl](https://superuser.com/questions/927523/how-to-download-only-subtitles-of-videos-using-youtube-dl)
yt-dlp
```
--list-subs
--all-subs --skip-download
--write-auto-sub --skip-download
yt-dlp --skip-download --write-sub --write-auto-sub --sub-lang "en.*"
```
example:
```sh
yt-dlp --skip-download --write-sub --write-auto-sub --sub-lang "en.*" https://www.youtube.com/watch\?v\=mmqDYw9C30I
```

how to convert vtt subtitles into human readable files?
https://www.reddit.com/r/youtubedl/comments/jvn6jx/how_to_convert_vtt_subtitles_into_human_readable/