# 最常用工作流程

0. git clone 项目URL(http/https/ssh) # 从远程库克隆到本地，并自动checkout最新版，每个项目只需1次。
1. git pull # 从远程库更新本地库，每天工作开始必做
1. 增删改文件
1. git stage filenames # 将增删改纳入暂存区(stage)
1. git commit -m "提交说明" # 提交到本地库
1. git push # 将本地库内容推送到远程库，每天工作结束必做

# 删除、改名/移动和恢复

**shell的rm(删除)和mv(改名/移动)**

如果使用shell命令rm删除文件、mv移动/改名文件，这都属于游离于git跟踪之外的。

```
mv old new   # 改名
mv new old   # 恢复

rm file   # 删除文件
git checkout file  # 恢复：从本地库重新取过来，但修改丢失了，所以用这个方法也可以废弃修改
或：git restore file   # 好像效果和上一命令一样
```

**用Git命令删除文件**

```
git rm file # 删除文件并纳入暂存区(与rm file; git stage file等效)，所以恢复方法为：
git restore --staged file # 从暂存区恢复为未暂存的删除，然后用下一命令恢复删除)
git restore file # 恢复删除的文件file
```

**用Git命令改名/移动文件**

```
git mv old new # 移动/改名文件并纳入暂存区(与mv old new; git stage old new等效)，所以恢复方法为：
git restore --stage old new # 从暂存区恢复为未暂存的删除，然后用下一命令恢复删除)
git restore old  # 恢复文件old
rm new
```

# 增加、修改和恢复

**增加文件：**

```
git add file # 增加文件后将增加的文件纳入暂存区(与git stage file等效)
git restore --staged file # 从暂存区恢复为未跟踪的，然后就可以删除它
或：git reset HEAD file # 好像跟上一命令功能一样
rm file # 删除
```

**修改文件：**

```
git stage file # 修改文件后将修改的文件纳入暂存区
git restore --staged file # 从暂存区恢复为未跟踪的，然后可以继续修改它
git restore file # 恢复被修改过的文件
```

# 提交到本地库与回退

`git commit -m "提交说明"` # 入本地库

如果发现错了想回退：

```
git log -3 --stat # 查看最近3次提交，并stat显示修改了哪些文件
git reset --hard HEAD^(回退1个commit，2个^回退2个commit) 或 用commitID(只需前7位)代替HEAD^
# 如果回退错了，要回到最新，就只能reset到远程的origin/master了：
git reset --hard origin/master
```

# 同步到远程库与回退

`git push`将本地库推送到远程库。

如果发现错了想回退，就得强制push了：

```
git log -3 --stat # 查看最近3次提交，并stat显示修改了哪些文件
git reset --hard HEAD^(回退1个commit，2个^回退2个commit) 或 用commit_id(只需前7位)代替HEAD^
git push --force # git push会提示本地落后，如果要废弃本地回退，可先git pull再git push，否则必须--force
```

# 其他命令

- git status  # 查看变化情况，stage之前必做，要常看
- git clone --depth 1 项目URL  # 只克隆最新版，用于不需要关注旧版本时
- git log file  # 查看file的所有提交(版本)记录，如果不写file，则显示本项目所有提交，可加参数-n，显示最近n次提交
- git diff commitID1 commitID2 file  # 查看两次提交间file的差异
- git checkout commitID  # 检出某个旧提交版本
- git checkout master # 重新检出最新版，github可能是main(git status可以看到是main还是master)

#  冲突与解决

多人clone/pull了相同的版本，分别修改后push，可能会发生冲突：

**最小冲突：**

1. 两人分别编辑了不同文件后push
1. 两人都删除了同一文件
1. 两人删除了不同的文件

这3种情况冲突都不大，地一个push的人没问题，第二个push的人会收到提示无法push，需要：

```
git pull # 先把第一个人的更新同步下来
git push # 然后直接push即可
```

**两人分别编辑了同一文件后push**

先push的人没问题，后push的人会收到提示无法push，需要`git pull`先把第一个人的更新同步下来，这时会提示合并冲突于哪些文件。

- 如果两人的修改在位置上不冲突，会自动合并;
- 如果两人的修改位置冲突，自动合并会失败。

无论哪种情况，需要检查这个冲突文件，检查自动合并情况、或编辑这个文件手工合并，然后再commit、push。

**甲编辑并push，乙删除并push了同一文件**

无论谁先push，后push者失败，需要：

```
git pull  # 先同步第一个人的更新
git add file 或 git rm file # 决定合并后是保留还是删除
git commit -m "说明"
git push
```
