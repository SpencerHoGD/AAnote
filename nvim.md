
<!-- TOC GFM -->

* [TOC](#toc)
* [Custom Snippets](#custom-snippets)
    - [Markdown](#markdown)
    - [10.1 Record and playback commands](#101-record-and-playback-commands)
    - [10.2 Substitution](#102-substitution)
    - [10.3 Command ranges](#103-command-ranges)
    - [10.4 The global command](#104-the-global-command)
    - [10.5 Visual block mode](#105-visual-block-mode)
    - [10.6 Reading and writing part of a file](#106-reading-and-writing-part-of-a-file)
    - [10.7 Formatting text](#107-formatting-text)
    - [10.8 Changing case](#108-changing-case)
    - [10.9 Using an external program](#109-using-an-external-program)
    - [11.1 Basic recovery](#111-basic-recovery)
    - [11.2 Where is the swap file?](#112-where-is-the-swap-file)
    - [11.3 Crashed or not?](#113-crashed-or-not)
    - [11.4 Further reading](#114-further-reading)
    - [12.1 Replace a word](#121-replace-a-word)
    - [12.2 Change "Last, First" to "First Last"](#122-change-last-first-to-first-last)
    - [12.3 Sort a list](#123-sort-a-list)
    - [12.4 Reverse line order](#124-reverse-line-order)
    - [12.5 Count words](#125-count-words)
    - [12.6 Find a man page](#126-find-a-man-page)
    - [12.7 Trim blanks](#127-trim-blanks)
    - [12.8 Find where a word is used](#128-find-where-a-word-is-used)
    - [20.1 Command line editing](#201-command-line-editing)
    - [20.2 Command line abbreviations](#202-command-line-abbreviations)
    - [20.3 Command line completion](#203-command-line-completion)
    - [20.4 Command line history](#204-command-line-history)
    - [20.5 Command line window](#205-command-line-window)
    - [21.1 Suspend and resume](#211-suspend-and-resume)
    - [21.2 Executing shell commands](#212-executing-shell-commands)
    - [21.3 Remembering information; ShaDa](#213-remembering-information-shada)
    - [21.4 Sessions](#214-sessions)
    - [21.5 Views](#215-views)
    - [21.6 Modelines](#216-modelines)
    - [22.1 The file explorer](#221-the-file-explorer)
    - [22.2 The current directory](#222-the-current-directory)
    - [22.3 Finding a file](#223-finding-a-file)
    - [22.4 The buffer list](#224-the-buffer-list)
    - [23.1 DOS, Mac and Unix files](#231-dos-mac-and-unix-files)
    - [23.2 Files on the internet](#232-files-on-the-internet)
    - [23.3 Binary files](#233-binary-files)
    - [23.4 Compressed files](#234-compressed-files)
    - [24.1 Making corrections](#241-making-corrections)
    - [24.2 Showing matches](#242-showing-matches)
    - [24.3 Completion](#243-completion)
    - [24.4 Repeating an insert](#244-repeating-an-insert)
    - [24.5 Copying from another line](#245-copying-from-another-line)
    - [24.6 Inserting a register](#246-inserting-a-register)
    - [24.7 Abbreviations](#247-abbreviations)
    - [24.8 Entering special characters](#248-entering-special-characters)
    - [24.9 Digraphs](#249-digraphs)
    - [24.10 Normal mode commands](#2410-normal-mode-commands)
    - [25.1 Breaking lines](#251-breaking-lines)
    - [25.2 Aligning text](#252-aligning-text)
    - [25.3 Indents and tabs](#253-indents-and-tabs)
    - [25.4 Dealing with long lines](#254-dealing-with-long-lines)
    - [25.5 Editing tables](#255-editing-tables)
    - [26.1 Repeating with Visual mode](#261-repeating-with-visual-mode)
    - [26.2 Add and subtract](#262-add-and-subtract)
    - [26.3 Making a change in many files](#263-making-a-change-in-many-files)
    - [26.4 Using Vim from a shell script](#264-using-vim-from-a-shell-script)
    - [27.1 Ignoring case](#271-ignoring-case)
    - [27.2 Wrapping around the file end](#272-wrapping-around-the-file-end)
    - [27.3 Offsets](#273-offsets)
    - [27.4 Matching multiple times](#274-matching-multiple-times)
    - [27.5 Alternatives](#275-alternatives)
    - [27.6 Character ranges](#276-character-ranges)
    - [27.7 Character classes](#277-character-classes)
    - [27.8 Matching a line break](#278-matching-a-line-break)
    - [27.9 Examples](#279-examples)
    - [28.1 What is folding?](#281-what-is-folding)
    - [28.2 Manual folding](#282-manual-folding)
    - [28.3 Working with folds](#283-working-with-folds)
    - [28.4 Saving and restoring folds](#284-saving-and-restoring-folds)
    - [28.5 Folding by indent](#285-folding-by-indent)
    - [28.6 Folding with markers](#286-folding-with-markers)
    - [28.7 Folding by syntax](#287-folding-by-syntax)
    - [28.8 Folding by expression](#288-folding-by-expression)
    - [28.9 Folding unchanged lines](#289-folding-unchanged-lines)
    - [28.10 Which fold method to use?](#2810-which-fold-method-to-use)
    - [29.1 Using tags](#291-using-tags)
    - [29.2 The preview window](#292-the-preview-window)
    - [29.3 Moving through a program](#293-moving-through-a-program)
    - [29.4 Finding global identifiers](#294-finding-global-identifiers)
    - [29.5 Finding local identifiers](#295-finding-local-identifiers)
    - [30.1 Compiling](#301-compiling)
    - [30.2 Indenting C files](#302-indenting-c-files)
    - [30.3 Automatic indenting](#303-automatic-indenting)
    - [30.4 Other indenting](#304-other-indenting)
    - [30.5 Tabs and spaces](#305-tabs-and-spaces)
    - [30.6 Formatting comments](#306-formatting-comments)
    - [31.1 The file browser](#311-the-file-browser)
    - [31.2 Confirmation](#312-confirmation)
    - [31.3 Menu shortcuts](#313-menu-shortcuts)
    - [31.4 Vim window position and size](#314-vim-window-position-and-size)
    - [31.5 Various](#315-various)
    - [32.1 Undo up to a file write](#321-undo-up-to-a-file-write)
    - [32.2 Numbering changes](#322-numbering-changes)
    - [32.3 Jumping around the tree](#323-jumping-around-the-tree)
    - [32.4 Time travelling](#324-time-travelling)
    - [OTHERS](#others)
        + [tab-tabpage](#tab-tabpage)

<!-- /TOC -->
## TOC
/usr/share/nvim/runtime/doc/usr_toc.txt

## Custom Snippets
### Markdown
| Shortcut | What it creates     |
|----------|---------------------|
| `,n`     | ---                 |
| `,b`     | **Bold** text       |
| `,s`     | ~~sliced~~ text     |
| `,i`     | *italic* text       |
| `,d`     | `code block`        |
| `,c`     | big `block of code` |
| `,m`     | - [ ] check mark    |
| `,p`     | picture             |
| `,a`     | [link]()            |
| `,1`     | # H1                |
| `,2`     | ## H2               |
| `,3`     | ### H3              |
| `,4`     | #### H4             |
| `,l`     | --------            |
| `,o`     | 1. 2. 3. 4.         |
| `,r`     | unorder list        |

10 Making big changes
### 10.1 Record and playback commands
### 10.2 Substitution
### 10.3 Command ranges
### 10.4 The global command
### 10.5 Visual block mode
### 10.6 Reading and writing part of a file
### 10.7 Formatting text
### 10.8 Changing case
### 10.9 Using an external program

11 Recovering from a crash
### 11.1 Basic recovery
### 11.2 Where is the swap file?
### 11.3 Crashed or not?
### 11.4 Further reading

12 Clever tricks
### 12.1 Replace a word
### 12.2 Change "Last, First" to "First Last"
### 12.3 Sort a list
### 12.4 Reverse line order
### 12.5 Count words
### 12.6 Find a man page
### 12.7 Trim blanks
### 12.8 Find where a word is used

=====================================================

Editing Effectively

Subjects that can be read independently.

20 Typing command-line commands quickly
### 20.1 Command line editing
### 20.2 Command line abbreviations
### 20.3 Command line completion
### 20.4 Command line history
### 20.5 Command line window

21 Go away and come back
### 21.1 Suspend and resume
### 21.2 Executing shell commands
### 21.3 Remembering information; ShaDa
### 21.4 Sessions
### 21.5 Views
### 21.6 Modelines

22 Finding the file to edit
### 22.1 The file explorer
### 22.2 The current directory
### 22.3 Finding a file
### 22.4 The buffer list

23 Editing other files
### 23.1 DOS, Mac and Unix files
### 23.2 Files on the internet
### 23.3 Binary files
### 23.4 Compressed files

24 Inserting quickly
### 24.1 Making corrections
### 24.2 Showing matches
### 24.3 Completion
- `CTRL-P` complete words (and previous)
- `CTRL-N` choose next
```
- `CTRL-X CTRL-F` file names
- `CTRL-X CTRL-L` whole lines
- `CTRL-X CTRL-D` macro definitions (also in included files)
- `CTRL-X CTRL-I` current and included files
- `CTRL-X CTRL-K` words from a dictionary
- `CTRL-X CTRL-T` words from a thesaurus
- `CTRL-X CTRL-]` tags
- `CTRL-X CTRL-V` Vim command line
```
`CTRL-XF` find filename
filepath = /usr/share/nvim/runtime/doc/usr_24.txt

### 24.4 Repeating an insert
### 24.5 Copying from another line

- `CTRL-Y` duplicating previous line
- `CTRL-E` duplicating next line

```
b_array[i]->s_next = a_array[i]->s_next;
b_array[i]->s_prev = a_array[i]->s_prev; (`CTRL-Y`)
```

### 24.6 Inserting a register

`CTRL-R` {register}
```
r = VeryLongFunction
```

### 24.7 Abbreviations
### 24.8 Entering special characters
### 24.9 Digraphs
### 24.10 Normal mode commands

25 Editing formatted text
### 25.1 Breaking lines
### 25.2 Aligning text
### 25.3 Indents and tabs
### 25.4 Dealing with long lines
### 25.5 Editing tables

26 Repeating
### 26.1 Repeating with Visual mode
### 26.2 Add and subtract
### 26.3 Making a change in many files
### 26.4 Using Vim from a shell script

27 Search commands and patterns
### 27.1 Ignoring case
### 27.2 Wrapping around the file end
### 27.3 Offsets
### 27.4 Matching multiple times
### 27.5 Alternatives
### 27.6 Character ranges
### 27.7 Character classes
### 27.8 Matching a line break
### 27.9 Examples

28 Folding
### 28.1 What is folding?
### 28.2 Manual folding
### 28.3 Working with folds
### 28.4 Saving and restoring folds
### 28.5 Folding by indent
### 28.6 Folding with markers
### 28.7 Folding by syntax
### 28.8 Folding by expression
### 28.9 Folding unchanged lines
### 28.10 Which fold method to use?

29 Moving through programs
### 29.1 Using tags
### 29.2 The preview window
### 29.3 Moving through a program
### 29.4 Finding global identifiers
### 29.5 Finding local identifiers

30 Editing programs
### 30.1 Compiling
### 30.2 Indenting C files
### 30.3 Automatic indenting
### 30.4 Other indenting
### 30.5 Tabs and spaces
### 30.6 Formatting comments

31 Exploiting the GUI
### 31.1 The file browser
### 31.2 Confirmation
### 31.3 Menu shortcuts
### 31.4 Vim window position and size
### 31.5 Various

32 The undo tree
### 32.1 Undo up to a file write
### 32.2 Numbering changes
### 32.3 Jumping around the tree
### 32.4 Time travelling

=====================================================

### OTHERS

`,d` [link](url) contents
[GFM](~/std/html/github-flavored-markdown.html)
[Mastering md](~/std/html/mastering-markdown.html)

#### tab-tabpage

`:help tabe` see help file
shortcut
```
noremap tt :tabe
noremap th :-tabnext
noremap tl :+tabnext
```


