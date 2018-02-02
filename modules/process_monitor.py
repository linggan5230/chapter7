import win32con
import win32api
import win32security

import wmi
import sys
import os

def log_to_file(message):
    fd = open("process_monitor_log.csv","ab")
    fd.write("%s\r\n" % message)
    fd.close()
    
    return

log_to_file("Time,User,Executable,CommandLine,PID,Parent PID,Privileges")

c = wmi.WMI()

process_watcher = c.Win32_Process.watch_for("creation")

while True:
    try:
        new_process = process_watcher()
        
        proc_owner = new_process.GetOwner()
        proc_owner = "%s\\%s" % (proc_owner[0],proc_owner[2])
        create_date = new_process.CreationDate
        executable = new_process.ExecutablePath
        cmdline = new_process.CommandLine
        pid = new_process.ProcessId
        parent_pid = new_process.ParentProcessId
        privileges = "N/A"
        
        process_log_message = "%s,%s,%s,%s,%s,%s,%s\r\n" % (create_date,proc_owner,executable,cmdline,pid,parent_pid,privileges)
        
        print process_log_message
        
        log_to_file(process_log_message)
    except:
        pass