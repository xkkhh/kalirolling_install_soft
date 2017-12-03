#!/usr/bin/env python
#encoding:utf-8
#make by xkkhh 
#date:Sun Dec  3 21:09:50 CST 2017

import os
import sys

cmd = os.system

def menu():
    hello='kali_soft_install:\n1.***set_asus_wifi_off\n2.***set_update_sources\n3.***set_root_user_no_sound\n4.***set_sogoupinying\n5.***set_wps\n6.***set_flash\n7.***set_wanyi_cloud_music\n8.***set_docker\n9.***zsh_shell_\nh.***help_mnue\nq or quit or exit to kill the python'
    print hello

def put():
    global chose
    chose = raw_input('>'*5+'<'*5+':')
def asus():
    f = open('/etc/modprobe.d/asus_nb_wmi.conf','w')
    f.write('options asus_nb_wmi wapf=4')
    f.close()

def sources():
    f = open('/etc/apt/sources.list','w')
    f.write('deb https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib\ndeb-src https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib')
    f.close()
    cmd('apt-get update && apt-get upgrade && apt-get dist-upgrade && apt-get autoremove')

def sound():
    f = open('/etc/default/pulseaudio','w')
    f.write('PULSEAUDIO_SYSTEM_START=1\nDISALLOW_MODULE_LOADING=0')
    f.close()

def sogou():
    cmd('apt-get install fcitx && wget http://cdn2.ime.sogou.com/dl/index/1509619794/sogoupinyin_2.2.0.0102_amd64.deb && dpkg -X sogoupinyin_2.2.0.0102_amd64.deb sogou && dpkg -e sogoupinyin_2.2.0.0102_amd64.deb sogou/DEBIAN')
    f = open('sogou/DEBIAN/control','r')
    s = f.read()
    f.close()
    s = s.replace('Depends: fcitx (>= 1:4.2.8.3-3~), fcitx-frontend-gtk2, fcitx-frontend-gtk3, fcitx-frontend-qt4, fcitx-module-kimpanel, im-config, libopencc2 | libopencc1, lsb-release, unzip, zip, x11-utils, fcitx-libs (>= 4.2.7), fcitx-libs-qt (>= 4.2.7), libc6 (>= 2.8), libgcc1 (>= 1:4.1.1), libgdk-pixbuf2.0-0 (>= 2.22.0), libglib2.0-0 (>= 2.16.0), libidn11 (>= 1.13), libnotify4 (>= 0.7.0), libqt4-dbus (>= 4:4.8.0), libqt4-declarative (>= 4:4.8.0), libqt4-network (>= 4:4.8.0), libqtcore4 (>= 4:4.8.0), libqtgui4 (>= 4:4.8.0), libqtwebkit4, libstdc++6 (>= 4.6), libx11-6, zlib1g (>= 1:1.2.0)','Depends: fcitx (>= 1:4.2.8.3-3~), fcitx-frontend-gtk2, fcitx-frontend-gtk3, fcitx-frontend-qt4, fcitx-module-kimpanel, im-config, lsb-release, unzip, zip, x11-utils, libc6 (>= 2.8), libgcc1 (>= 1:4.1.1), libgdk-pixbuf2.0-0 (>= 2.22.0), libglib2.0-0 (>= 2.16.0), libidn11 (>= 1.13), libnotify4 (>= 0.7.0), libqt4-dbus (>= 4:4.8.0), libqt4-declarative (>= 4:4.8.0), libqt4-network (>= 4:4.8.0), libqtcore4 (>= 4:4.8.0), libqtgui4 (>= 4:4.8.0), libqtwebkit4, libstdc++6 (>= 4.6), libx11-6, zlib1g (>= 1:1.2.0)')
    f1 = open('sogou/DEBIAN/control','w')
    f1.write(s)
    f1.close()
    cmd('dpkg-deb -b sogou sogou.deb && dpkg -i sogou.deb && rm -rf /etc/apt/sources.list.d/*')

def wps():
    cmd('wget http://ftp.tw.debian.org/debian/pool/main/libp/libpng/libpng12-0_1.2.49-1+deb7u2_amd64.deb && wget http://kdl1.cache.wps.com/ksodl/download/linux/a21//wps-office_10.1.0.5707~a21_amd64.deb && dpkg -i libpng12-0_1.2.49-1+deb7u2_amd64.deb && dpkg -i wps-office_10.1.0.5707~a21_amd64.deb && unzip wps_symbol_fonts.zip -d wps-office && cp wps-office/* /usr/share/fonts/')

def flash():
    cmd('wget https://fpdownload.adobe.com/get/flashplayer/pdc/27.0.0.187/flash_player_npapi_linux.x86_64.tar.gz &&  tar -zxvf flash_player_npapi_linux.x86_64.tar.gz && cp libflashplayer.so /usr/lib/mozilla/plugins/ && cp -r usr/* /usr/')

def music():
    cmd('wget http://s1.music.126.net/download/pc/netease-cloud-music_1.0.0-2_amd64_deepin15.deb && apt-get install gdebi && gdebi netease-cloud-music_1.0.0-2_amd64_deepin15.deb')
    f = open('/usr/share/applications/netease-cloud-music.desktop','r')
    s = f.read()
    f.close()
    s = s.replace('Exec=netease-cloud-music %U','Exec=netease-cloud-music %U -no-sandbox')
    f1 = open('/usr/share/applications/netease-cloud-music.desktop','w')
    f1.write(s)
    f1.close()

def docker():
    f = open('/etc/apt/sources.list.d/backports.list','w')
    f.write('deb http://http.debian.net/debian wheezy-backports main')
    f.close()
    cmd('apt-get update && apt-get install apt-transport-https ca-certificates && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D')
    f1 = open('/etc/apt/sources.list.d/docker.list','w')
    f1.write('deb https://apt.dockerproject.org/repo debian-wheezy main')
    f1.close()
    cmd('apt-get update && apt-cache policy docker-engine && apt-get install docker-engine')

def zsh():
    cmd('wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh')
menu()
while True:
    put()
    if chose == '1':
        asus()
        continue
    if chose == '2':
        sources()
        continue
    if chose == '3':
        sound()
        continue
    if chose == '4':
        sogou()
        continue
    if chose == '5':
        wps()
        continue
    if chose == '6':
        flash()
        continue
    if chose == '7':
        music()
        continue
    if chose == '8':
        docker()
        continue
    if chose == '9':
        zsh()
        continue
    if chose == 'q' or chose == 'quit' or chose == 'exit':
        break
    if chose == 'h':
        menu()
        continue
    else:
        print 'check you\'s input,h for help!'
        continue
