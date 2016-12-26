#!/usr/bin/env python2.7
# Simple program to check if specified services are running and start them if they are not.
# Meant to be used as a cron job if not using a CM tool.
# For now, the service must be added to chkconfig.
import os, subprocess

def getservices():
  with open('services.txt') as f:
    service = f.read().splitlines() 
    return service

def main():
  if  os.getuid() !=0:
   exit("Please run as root")
  services = getservices()
  print "Checking:", services
  for x in services:
    try:
      output = subprocess.check_output(['ps', 'aux'])
      if x in output:
        print x,'is already running'
      else:
        print x,'is stopped'
        try:
          subprocess.call("service "+x+" start", shell=True) 
          subprocess.call("service "+x+" status", shell=True)
        except:
          print ('could not start '+x) 
    except:
      exit("The operation failed!")
