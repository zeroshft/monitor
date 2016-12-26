##Quick start
git pull https://github.com/zeroshft/service-monitor.git  
add services to services.txt  
chmod +x mon.py  
./mon.py  

##Service monitor
Simple program to check if specified services are running and start them if they are not.
Can be used as a cron job if not using a CM tool.

Tested on Centos 6.5 and 7. 
