#!/usr/bin/python
from os import listdir
from os.path import isfile, join
import subprocess as sub
from adb_android import adb_android
import fuzzerConfig

# change this


def start():
    clear_logcat()
    fix_my_dex()

def clear_logcat():
    adb_android.shell("logcat -c")

def save_logs():
    adb_android.shell("logcat -d > /data/local/tmp/logcat.txt")

def fix_my_dex():
    onlyfiles = [f for f in listdir(fuzzerConfig.path_to_mutated_dex) if isfile(join(fuzzerConfig.path_to_mutated_dex, f))]
    for x in range(len(onlyfiles)):
        #os.system(path_to_dex_fixer+" -I "+onlyfiles[x])
        fixed_dex = onlyfiles[x]
        p = sub.Popen([fuzzerConfig.path_to_dex_fixer, '-I', fuzzerConfig.path_to_mutated_dex+fixed_dex], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()
        print output
        run_on_android_emulator(fixed_dex+"_repaired.dex")

def run_on_android_emulator(fixed_dex):
    print fixed_dex

    #adb logcat -c to clear logs from logcat

    adb_android.push(fuzzerConfig.path_to_mutated_dex+fixed_dex, '/data/local/tmp/')
    adb_android.shell('log -p F -t CRASH_LOGGER SIGSEGV : '+fixed_dex)
    adb_android.shell(fuzzerConfig.target_android_executable+' /data/local/tmp/'+fixed_dex)
    adb_android.shell("rm /data/local/tmp/"+fixed_dex)
    save_logs()


#def re_mount():
#	remount_cmd="adb shell mount -o remount,rw /system"
#	os.system(remount_cmd)

#def push_shellscript():
#	psh_shellscript_cmd="adb push exec_me.sh /system/bin/"
#	os.system(psh_shellscript_cmd)
#	os.system("adb shell chmod 777 /system/bin/exec_me.sh")


#re_mount()
#push_shellscript()

#for x in range(0,600000):
#	fname="fuzzed_"+str(x)+".png"
#	psh_cmd="adb push /home/anto/Desktop/fuzzed_files/data/"+fname+" /system/bin/pngtest.png"
#	print psh_cmd
#	os.system(psh_cmd)
#	os.system("adb shell /system/bin/exec_me.sh")
#	time.sleep(1)
