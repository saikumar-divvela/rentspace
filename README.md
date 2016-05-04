# rentspace

Technologies: Python, DJango , Mysql
Tools:

TOC

Installing Pip (Python package manager)
    apt-get install python-pip
    apt-get install python-dev libmysqlclient-dev   # Installs python dev libraries

Installing DJango
      pip install django
      pip install django --upgrade
      python -c "import django; print(django.get_version())"
      
Installing Mysql
    apt-get install python-pip
    apt-get install python-dev libmysqlclient-dev
    pip install mysql-python
    sudo mysql_secure_installation
    sudo mysql_install_db
    
Installing workbench
    sudo apt-get install mysql-workbench
    
Uninstall Mysql
    sudo service mysql stop or sudo killall -9 mysql 

    sudo apt-get purge mysql-server mysql-client mysql-common mysql-server-core-5.5 mysql-client-core-5.5
    sudo rm -rf /etc/mysql /var/lib/mysql /var/log/mysql
    sudo apt-get autoremove
    sudo apt-get autoclean

    sudo deluser mysql
    sudo delgroup mysql
