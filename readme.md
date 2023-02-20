
## Connect to remote folder
yum install cifs-utils
------------------------- Method 1 -----------------------------------
mount -t cifs -o username=Dagny,password=Epd2$d4gny! //10.12.201.25/lunar /mnt/SFC
Epd2$d4gny!
https://access.redhat.com/documentation/es-es/red_hat_enterprise_linux/7/html/storage_administration_guide/mounting_an_smb_share#frequently_used_mount_options
https://console.kim.sg/how-to-mount-password-protected-windows-shared-folder-in-ubuntu/

//10.12.201.25/lunar/SFC /mnt/SFC cifs credentials=/home/david/Documents/smbCredentials,iocharset=utf8,sec=ntlm 0 0

//10.12.201.25/lunar/SFC /mnt/SFC cifs username=Dagny,password=Epd2$d4gny!,iocharset=utf8,sec=ntlm 0 0

------------------------- Method 2 -----------------------------------
username=Dagny
password=Epd2$d4gny!

//10.12.201.25/lunar/SFC /mnt/SFC cifs vers=2.0,credentials=/home/david/.smbcredentials,iocharset=utf8,gid=1000,uid=1000,file_mode=0777,dir_mode=0777 0 0

https://www.ceos3c.com/linux/mount-cifs-permission-denied-linux/

## Dependencias
Xampp
pip install watchdog
pip install flask_restful
pip install python-dotenv
pip install waitress

## Daemonize
https://stackoverflow.com/questions/6337119/how-do-you-daemonize-a-flask-application
/etc/systemd/system/

## Autostart Xampp
https://haneefputtur.com/auto-start-xampp-in-centos-6-4.html

## xampp.service
[Unit]
Description = Xampp server

[Service]
ExecStart =/opt/lampp/lampp start
ExecStop =/opt/lampp/lampp stop
Type=forking
  
[Install]
WantedBy = multi-user.target

## xandra_api.service
[Unit]
Description = api to monitor and calculate fbt yield based on log files

[Service]
ExecStart=/usr/local/bin/python3 /usr/local/Foxconn/automation/Xandra-API/xandra_api.py
ExecStop=kill $(lsof -t -i:5000)
Restart=on-failure
  
[Install]
WantedBy = multi-user.target

## Google sheets
david.ascencio.foxconn@gmail.com
Foxconn#231
pip3 install --upgrade google-api-python-client oauth2client
pip3 install gspread