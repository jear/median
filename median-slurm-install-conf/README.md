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





```
