# rentspace

Website names:
quickstay
estay
eroom
rentspace
oyebasera
eroost
ehoy/hoy


Action items
    -> Check about how to validate Aadhar card using the software provided by police dept or others
    -> How to validate the content provided by service provider (like location info, pictures etc)
        picture/location validation
            1)  check if pic contains illegal content   (this we can do by verifying manually)
            2)  check if the pic actually belongs to house
            3)  validate location (apartment address etc)
            4)  How to take care of security,risk factor or false post for ladies/girl
            5)  To provide safety, giving the contact details of service provider to police etc..
            6)  Verified / Unverified posts
            
    ID card for verification:  AAdhar
        Someone gives some one else's aadhar card, creates a login entry..
        there is no link between aadhar card and mobile number/email id used for login
        Reference number (suppose for apartment, reference number of apt president
                          )
        Identify location using google map
            
    -> Keep legal rules in Terms and conditions
    -> Check with Advocate about terms and conditions


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
