from adb_android import adb_android
import search
import fuzzerConfig

def start():
    adb_android.pull("/data/local/tmp/logcat.txt",fuzzerConfig.path_to_save_logcat)
    search.process(fuzzerConfig.path_to_save_logcat)
