from adb_android import adb_android
from os.path import isfile, join
from os import listdir
import fuzzerConfig


def start():
    onlyfiles = [f for f in listdir(fuzzerConfig.path_for_crash_samples) if isfile(join(fuzzerConfig.path_for_crash_samples, f))]
    for x in range(len(onlyfiles)):
        #clean tombstones
        adb_android.shell("rm /data/tombstones/*")
        #push file to device
        adb_android.push(fuzzerConfig.path_for_crash_samples+onlyfiles[x],"/data/local/tmp")
        #run the file
        adb_android.shell(fuzzerConfig.target_android_executable+' /data/local/tmp/' + onlyfiles[x])
        #collect the crash
        result = adb_android.shell("ls -l /data/tombstones/ | grep tombstone_00")

        if(len(result)<2):
            pass
            #No Tombstones generated , its a false positive
        else:
            adb_android.pull('/data/tombstones/tombstone_00',fuzzerConfig.path_for_confirmed_samples+"tombstone_"+onlyfiles[x])
