from adb_android import adb_android
import fuzzerConfig
import subprocess
import os
import thread
import time
def copy_gdb_server_to_device():
	adb_android.push(fuzzerConfig.path_to_thridparty+"android_gdb/gdbserver","/data/local/tmp/")


def adb_forward():
    os.system("adb forward tcp:5039 tcp:5039")
    


def start():
	copy_gdb_server_to_device()
	adb_forward()

def start_gdb_server_in_device():
        out = adb_android.shell("/data/local/tmp/gdbserver :5039 /system/xbin/dexdump /data/local/tmp/crash.dex")
        print out

def start_gdb_in_pc():
	out = os.system(fuzzerConfig.path_to_thridparty+"android_gdb/gdb")
	print out

start()
try:
        thread.start_new_thread(start_gdb_server_in_device,())
	time.sleep(2)
        thread.start_new_thread(start_gdb_in_pc,())
except:
        print "unable to start threads"



time.sleep(5)
