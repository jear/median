Slurm master node install

```
sudo adduser -u 1111 munge --disabled-password --gecos ""
sudo adduser -u 1121 slurm --disabled-password --gecos ""

sudo apt-get install libmunge-dev libmunge2 munge -y 
sudo systemctl enable munge 
sudo systemctl start munge 
munge -n | unmunge | grep STATUS 

sudo mkdir /storage

sudo cp /etc/munge/munge.key /storage/ 
sudo chown munge /storage/munge.key 
sudo chmod 400 /storage/munge.key 

# ubuntu 18.04
sudo apt-get install git gcc make ruby ruby-dev libpam0g-dev libmariadb-client-lgpl-dev libmysqlclient-dev mariadb-server build-essential libssl-dev -y 

# ubuntu 20.04
sudo apt-get install git gcc make ruby ruby-dev libpam0g-dev libmariadb-client-lgpl-dev-compat libmysqlclient-dev mariadb-server build-essential libssl-dev -y 

sudo gem install fpm 

# Ubuntu 18
sudo systemctl enable mariadb 
sudo systemctl start mariadb
sudo mysql -u root 

create database slurm_acct_db; 
create user 'slurm'@'localhost'; 
set password for 'slurm'@'localhost' = password('change_me'); 
grant usage on *.* to 'slurm'@'localhost'; 
grant all privileges on slurm_acct_db.* to 'slurm'@'localhost'; 
flush privileges; 
exit 

 
sudo -i
cd /storage

wget https://download.schedmd.com/slurm/slurm-20.02.5.tar.bz2 
tar xvjf slurm-20.02.5.tar.bz2 
cd slurm-20.02.5/ 
./configure --prefix=/tmp/slurm-build --sysconfdir=/etc/slurm --enable-pam --with-pam_dir=/lib/x86_64-linux-gnu/security/ --without-shared-libslurm 
make && make contrib && make install 

cd ..

sudo fpm -s dir -t deb -v 1.0 -n slurm-20.02.5 --prefix=/usr -C /tmp/slurm-build . 
sudo dpkg -i slurm-20.02.5_1.0_amd64.deb 

sudo mkdir -p /etc/slurm /etc/slurm/prolog.d /etc/slurm/epilog.d /var/spool/slurm/ctld /var/spool/slurm/d /var/log/slurm 
sudo chown slurm /var/spool/slurm/ctld /var/spool/slurm/d /var/log/slurm 


git clone https://github.com/jear/median.git

grep -i pass median/median-slurm-install-conf/conf/slurmdbd.conf
StoragePass=change_me

grep ControlMachine median/median-slurm-install-conf/conf/slurm.conf
ControlMachine=slurm18

sudo cp /storage/median/median-slurm-install-conf/conf/slurmdbd.service /etc/systemd/system/ 
sudo cp /storage/median/median-slurm-install-conf/conf/slurmctld.service /etc/systemd/system/ 

sudo cp /storage/median/median-slurm-install-conf/conf/slurmdbd.conf /etc/slurm/ 
sudo cp /storage/median/median-slurm-install-conf/conf/slurm.conf /etc/slurm/ 

sudo systemctl enable slurmdbd 
sudo systemctl enable slurmctld 

sudo systemctl stop slurmdbd 
sudo systemctl daemon-reload 
sudo systemctl status slurmdbd 
sudo systemctl status slurmctld 

sudo systemctl start slurmdbd 
sudo systemctl status slurmdbd 

sudo systemctl stop slurmctld 
sudo systemctl daemon-reload 
sudo systemctl start slurmctld 
sudo systemctl status slurmctld 

 ll /run/slurm*
-rw-r--r-- 1 slurm root 6 Apr 27 21:40 /run/slurmctld.pid
-rw-r--r-- 1 slurm root 6 Apr 27 21:40 /run/slurmdbd.pid


 

```
