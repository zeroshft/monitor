Simple program to check if specified services are running and start them if they are not.

Meant to be used as a cron job if not using a CM tool.

Usage: 
   Add services as needed to services(). 
   # chmod +x service-monitor.py
   # ./service-monitor.py

For now, the service must be added to chkconfig.
