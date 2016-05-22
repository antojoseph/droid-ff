import os
USR_HOME_DIR = os.path.expanduser('~')

#tools and symbols for the fuzzer
ndkstack = "/opt/Arsenal/android-ndk-r11c/ndk-stack"
addr2line = "/opt/Arsenal/android-ndk-r11c/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi-addr2line"
symbols = USR_HOME_DIR+"/droid-ff/symbols"

#folders for the fuzzer
path_for_confirmed_samples = USR_HOME_DIR+"/droid-ff/confirmed_crashes/"
path_for_crash_samples = USR_HOME_DIR+"/droid-ff/crashes/"
path_to_generated_samples = USR_HOME_DIR+"/droid-ff/generated_samples_folder/"
path_to_save_logcat= USR_HOME_DIR+"/droid-ff/logcat.txt"
path_to_dex_fixer = USR_HOME_DIR+"/droid-ff/bin/dexRepair"
path_to_mutated_dex = USR_HOME_DIR+"/droid-ff/generated_samples_folder/"
path_to_mutation_sample = USR_HOME_DIR+"/droid-ff/mutation_sample/"

#android binary which needs to be fuzzed
target_android_executable = "/system/xbin/dexdump"