

https://stackoverflow.com/questions/41489692/how-to-search-linux-man-pages-e-g-with-grep


You have to tell grep that `-X` is not an option, but the pattern to look for:

```
man curl | grep -- '-X'
```

`--` indicates the end of options. Without it, grep thinks that `-X` is an option.

Alternatively, you can use `-e` to indicate that what follows is a pattern:

```
man curl | grep -e '-o,'
```

If you want to see the complete man page but skip directly to the first occurrence of `-X`, you can use a command line option to `less`:

```
man curl | less +/-X
```
Typing N repeatedly then takes you to the following occurrences.



```
man curl | grep -a 20 -- '-X'
```
together with the `-a 20` option to read the first 20 lines below each result. This allowed me to quickly find the documentation on the `-X` option without having to scroll down too much. 

