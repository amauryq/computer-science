# Find text in files
find / -type f -exec grep -H 'text-to-find-here' {} \;

# SSH Tunneling

ssh -f -L 2222:remote-host:22 localhost -N
ssh-keygen
ssh-copy-id localhost

# NSLookup

nslookup google.com
dig google.com
dig redhat.com MX +noall +answer
dig redhat.com NS +short
dig -x <ip-address>

# Encrypt a File System

yum install ecryptfs-utils
lsmod | grep ecryptfs
modprobe ecryptfs
lsmod | grep ecryptfs
usermod -a -G ecryptfs <user>
ecryptfs-setup-private

# Setting and Using Static Routes

route add -net 172.17.0.0 netmask 255.255.0.0 gw 192.168.1.195

# Background Foreground and NOHUP In a Nutshell

nohup sleep 5 > output.txt &

# Package Dependencies

sudo yum install yum-utils yum-plugin-downloadonly
yumdownloader openssh-server
# See packages dependencies
rpm -qR openssh-server
rpm -qpR openssh-server-6.6.1p1-25.el7_2.x86_64.rpm
# rpm dependencies
repoquery --requires --resolve openssh-server
# Method in debian based systems
sudo apt-get install -d openssh-server
sudo aptitude why openssh-server
sudo apt-cache showpkg openssh-server
sudo apt-cache rdepends openssh-server

# Customizing Appearance and Color of Prompt

ls -la /etc/skel
export PS1="\[\e[1;32m\][\u@\h ~]$ "


# Video Conversions on the Command Line with Handbrake

HandBrakeCLI -i sample.mkv -o sample.mp4 --preset="Normal"

# Console Logging with Script Utility (documentation help)

script mylog.log
# Do things in console
exit
script -a mylog.log
script -f mylog.log

# Terminal Administration with Tilda

sudo apt-get install tilda

# Bash: The Comma Is Your Friend

sentence=DIE Another dAY
echo ${sentence,}
-> dIE Another dAY
echo ${sentence,,}
->die another day
echo ${sentence,,,}
-> DIE Another dAY

touch filename{1,2,3,4,5}
# 5 files wil be created with name filename1..filename5

mv filename.{old,new}
# move filename.old to filename.new

# Bash Aliases and Escapes

alias lm='ls -lart --color=yes | more'
alias
unalias lm
alias ls='ls --color=auto'
\ls

# How Netstat Can Be Used to Compromise Your System

netstat -at | -au | -ant | -tnl | -nlpt (sudo) | -s | -rn (default gw) | -i (network interfaces) | -ie | -ct | -g | -atpn | -ale

# How Nmap Can Be Used to Compromise Your System

nmap -vv localhost
netstat -rn (default gw)
nmap -vv <default-gw>
nmap -sP -vv 192.168.1.0/24
nmap -sV <ip-addr>

# Bash Sourcing External Files

Inside bash script you can write
source /path/to/source/config.ini

# MD5 Checksums and How to Use Them

md5sum file1 file2 file3 > files.md5
md5sum -c file.md5

# User Keylogger

vi /etc/skel/.bash_profile
add ath the end: script -f -q -a /home/${USER}/user.log

# Setting Local and Global Java Environment Variables

# Get timestamp in bash

```bash
now=$(($(date +%s%N)/1000000))
echo $now
```