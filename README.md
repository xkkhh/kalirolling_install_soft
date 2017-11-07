asus笔记本网卡硬件关闭执行命令:

echo "options asus_nb_wmi wapf=4" | tee /etc/modprobe.d/asus_nb_wmi.conf

改更新源:

编辑 vim /etc/apt/sources.list 删除所有，添加以下两段
deb https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

更新系统命令:apt update && apt upgrade && apt dist-upgrade && apt autoremove

root用户无声音：
leafpad 编辑 /etc/default/pulseaudio 写入以下两行即可(不存在会自动创建)
#root下是默认关闭声卡驱动的
PULSEAUDIO_SYSTEM_START=1
DISALLOW_MODULE_LOADING=0

搜狗输入法的安装:

首先 apt-get install fcitx

http://pinyin.sogou.com/linux/

dpkg -X sogoupinyin_XXXXXX_amd64.deb sogou

dpkg -e sogoupinyin_XXXXXX_amd64.deb sogou/DEBIAN

vim sogou/DEBIAN/control

删除:libopencc2 | libopencc1, fcitx-libs (>= 4.2.7), fcitx-libs-qt (>= 4.2.7)

dpkg-deb -b sogou sogou.deb

dpkg -i sogou.deb

rm -rf /etc/apt/sources.list.d/*

wps的安装:

下载字体库:https://pan.baidu.com/s/1eSoLzjk

下载ibpng12-0的依赖包:http://ftp.tw.debian.org/debian/pool/main/libp/libpng/libpng12-0_1.2.49-1+deb7u2_amd64.deb

下载wps:http://wps-community.org/download.html

dpkg -i libpng12-0_1.2.49-1+deb7u2_amd64.deb

dpkg -i wps-office_xxxxxxx~xxx_amd64.deb

unzip  linux-wps-office-fonts.zip

cp wps-office/* /usr/share/fonts/

flash的安装:

https://get.adobe.com/cn/flashplayer/ 选择.tar.gz版本

tar -zxvf flash_player_npapi_linux.x86_64.tar.gz

cp libflashplayer.so /usr/lib/mozilla/plugins/

cp -r usr/* /usr/
网易云音乐的安装:

选择deepin版本 http://music.163.com/#/download

我下载的是 http://s1.music.126.net/download/pc/netease-cloud-music_1.0.0-2_amd64_deepin15.deb
gdebi netease-cloud-music_1.0.0-2_amd64_deepin15.deb

vim /usr/share/applications/netease-cloud-music.desktop
修改Exec=netease-cloud-music %U
为Exec=netease-cloud-music %U --no-sandbox

docker的安装:

新文件:vim /etc/apt/sources.list.d/backports.list

添加:deb http://http.debian.net/debian wheezy-backports main

执行:apt-get update && apt-get install apt-transport-https ca-certificates && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

新文件:vim /etc/apt/sources.list.d/docker.list

添加:deb https://apt.dockerproject.org/repo debian-wheezy main

执行 :apt-get update && apt-cache policy docker-engine && apt-get install docker-engine

启动服务:service docker start

运行测试列子:docker run hello-world

qq的安装:

使用的wine qq

wine插件下载:http://dl.winehq.org/wine/
winetricks-zh：https://github.com/hillwoodroc/winetricks-zh/archive/master.zip

1.winetricks-zh

2.wine-mono(插件地址下载最新的)

3.wine-gecko（插件地址下载最新的）

4.W2KSP4_EN.EXE https://pan.baidu.com/s/1dFLC4al

5.InstMsiW.exe https://pan.baidu.com/s/1dFLC4al

6.simsun.ttc

7.zh.reg

64位kali先执行:dpkg --add-architecture i386

winecfg

mkdir /usr/share/fonts/windows/

cd ~/.wine/drive_c/windows/fonts
ln -s /usr/share/fonts/windows/simsun.ttc simsun.ttc
ln -s /usr/share/fonts/windows/simsun.ttc simfang.ttc

修改 ~/.wine/system.reg
装好字体后，还要修改一下 Wine 的注册表设置，指定与字体相关的设置：
gedit ~/.wine/system.reg
（一定要使用 gedit 或其他支持 gb2312/utf8
编码的编辑器修改这些文件，否则文件中的中文可能变乱码）
搜索： LogPixels
找到的行应该是：[System\\CurrentControlSet\\Hardware
Profiles\\Current\\Software\\Fonts]
将其中的：
"LogPixels"=dword:00000060
改为：
"LogPixels"=dword:00000070
搜索： FontSubstitutes
找到的行应该是：[Software\\Microsoft\\Windows
NT\\CurrentVersion\\FontSubstitutes]
将其中的：
"MS Shell Dlg"="Tahoma"
"MS Shell Dlg 2″="Tahoma"
改为：
"MS Shell Dlg"="SimSun"
"MS Shell Dlg 2″="SimSun"

修改 ~/.wine/drive_c/windows/win.ini
gedit ~/.wine/drive_c/windows/win.ini
在文件末尾加入：
[Desktop]
menufontsize=13
messagefontsize=13
statusfontsize=13
IconTitleSize=13

regedit zh.reg

从Windows目录下的Fonts里的simsun.ttc复制到/home/user/.wine/drive_c/windows/fonts里面

存放两个msi文件的目录下打开终端，执行：wine msiexec /i wine-mono-X.X.X.msi

wine msiexec /i wine_gecko-X.XX-x86.msi

unzip winetricks-zh-master.zip

mv winetricks-zh-master /opt/

chmod -R a+x /opt/winetricks-zh-master

cp /opt/winetricks-zh-master/winetricks-zh /usr/bin/

apt-get install cabextract

mkdir -p ~/.cache/winetricks/win2ksp4/

mkdir -p ~/.cache/winetricks/msls31/

cp W2KSP4_EN.EXE ~/.cache/winetricks/win2ksp4/
cp InstMsiW.exe ~/.cache/winetricks/msls31/

winetricks-zh qq

接下来它会自动下载QQ8.9.1和vcran6、文泉驿字体等，这里的vranc6的安装程序还是乱码的
这里的Ja就是确定，Nein就是取消，点击Ja。
 
添加桌面图标:cp ~/.local/share/applications/wine/Programs/腾讯软件/QQ/腾讯QQ.desktop ~/Desktop/
 
