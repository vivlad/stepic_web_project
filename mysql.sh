sudo /etc/init.d/mysql restart
mysql -uroot -e "create database myproject;"
mysql -uroot -e "CREATE USER 'enth'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'enth'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
sudo /etc/init.d/mysql restart