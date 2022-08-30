---
title: Linux常用命令
---

# 基础

linux命令行一般由命令、选项、目标等组成。

命令和选项一般都是英文单词或其缩写。
许多同一选项有长短2种方式，-h 和 --help 都表示获取该命令的帮助，但有些选项只有其一。
短格式的选项经常可以合并输入，比如ls -a -l -t 可以输入为ls -alt。

| | |
|-|-|
| * | 通配符，表示任意个任意字符 |
| ? | 通配符，表示1个任意字符 |
| . | 表示当前目录 |
| .. | 表示上级目录 |
| --help | 命令帮助选项，cheatsheet只给出常用命令参数，详细的参见帮助 |
| > | 输出重定向，将前面程序的数据结果存入后面的文件  |
| >> | 输出附加重定向，将前面程序的数据结果添加到后面的文件中  |
| < | 输入重定向，从后面文件的内容作为前面程序的输入|
| \| | 管道，将前面程序的输出作为后面程序的输入 |

# 目录相关


| | |
|-|-|
| ls | list 查看目录内容 |
| ls -alrt DIR| -a所有all -l详细long -t时间排序time -r逆序reverse |
| pwd | print work directory 查看当前处于哪个目录 |
| cd DIR | change directory 切换目录，不带参数时切换至用户家目录 |
| rm FILE1 FILE2 ... | remove 删除文件，可用通配符\*/?等|
| rm -rf DIR | 删除DIR目录及其下所有文件/子目录。-r递归 -f强制force|
| mv FILE1 DIR/FILE2 | move 移动/改名文件或目录|
| mkdir/rmdir DIR | 创建/删除目录(目录下为空才能rmdir) |

# 文件相关

| | |
|-|-|
| cp FILE1 FILE2 | copy, 复制FILE1到FILE2 |
| cp -af DIR1 DIR2 | 复制目录DIR1及其下所有文件到DIR2 |
| ln -s A B | link 给A(可以是文件或目录)建个软连接(类似快捷方式)B |
| cat FILE | 显示FILE内容 |
| cat FILE1 FILE2 > FILE | 合并两个文件为新文件FILE |
| more/less FILE | 分页查看FILE文件内容，more和less稍有不同 |
| head/tail -n 10 FILE | 显示FILE的头/尾10行内容|
| wc FILE | word count，统计文件的行数、词数等信息 |
| sort FILE | 文件FILE按行排序后输出 |

# 搜索相关

| | |
|-|-|
| find . -name abc | 当前目录下寻找abc文件在哪里 |
| find . \| grep abc | 当前目录下寻找文件名有abc的文件 |
| which 程序名 | 查找程序在哪个目录下(仅能找到在可执行路径的程序) |


# 用户相关

| | |
|-|-|
| chmod +x FILE | 文件有r(read读) w(write写) x(execute执行)三种常用权限，给FILE +x使它能作为程序被运行 |
| chown/chgrp FILE/DIR| chown改变文件或目录的所属人，chgrp改变文件或目录的所属组 |
| sudo adduser user1 | 增加用户user1，需要sudo用超级用户权限执行，后略 |
| deluser user1 | 删除用户user1(但不自动删除家目录/home/user1) |
| usermod -aG group1 user1 | 将user1加入到group1组中 |
| w/who | 查看本机有哪些用户登录着 |

# 网络相关

| | |
|-|-|
| ifconfig | |
| ip addr | |
| route -n | |
| ip route | |


# 软件相关

| | |
|-|-|
| apt install xxx | 从网上软件库安装软件 |
| apt remove xxx | 卸载软件 |
| dpkg -i xxx.deb | 用下载好的安装包安装软件 |
| dpkg -L xxx | 看这个软件包括哪些文件 |

# 系统相关

| | |
|-|-|
| du -d1 -m | disk usage，当前目录下的文件占用多少空间，-m以MB显示，-d1显示1级子目录 |
| df -m | disk free，整个硬盘还有多少空间，-m以MB显示 |
| date | 查看系统时间 |
| ps ax | process status，进程状态|
| kill PID | 杀死某个进程 |
| top | 系统信息：进程、内存、CPU等|
| free | 系统内存空闲情况 |
| reboot | 重启系统 |
| shutdown -h now | 关机 |

# 常用程序

| | |
|-|-|
| tar zcvf xxx.tar.gz xxx1 xxx2 xxx3/ | 将xxx?等文件目录压缩为tar.gz |
| tar zxvf xxx.tar.gz | tar.gz文件解压缩 |
| tar xvf xxx.tar.xz | tar.xz文件解压缩 |
| zip/unzip | 压缩解压zip文件 |
| rar/unrar | 压缩解压rar文件 |
| grep -r abc * | 当前目录所有文件中查找abc字符串，-r表示所有子目录也递归查找 |
| | |
| | |
