import os
USR_HOME_DIR = os.path.expanduser('~')
DROID_FF_PATH = USR_HOME_DIR + "/Desktop/MobileSec/fixDroid-ff/droid-ff"

#tools and symbols for the fuzzer
ndkstack= USR_HOME_DIR + "/Programs/android-ndk/ndk-stack"
addr2line = USR_HOME_DIR + "/Programs/android-ndk/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi-addr2line"
symbols = DROID_FF_PATH + "/symbols"

#folders for the fuzzer
path_for_confirmed_samples = DROID_FF_PATH + "/confirmed_crashes/"
path_for_crash_samples = DROID_FF_PATH + "/crashes/"
path_to_generated_samples = DROID_FF_PATH + "/generated_samples_folder/"
path_to_save_logcat= DROID_FF_PATH + "/logcat.txt"
path_to_mutated_dex = DROID_FF_PATH + "/generated_samples_folder/"
path_to_mutation_sample = DROID_FF_PATH + "/mutation_sample/"
path_to_fuzzer_binaries = DROID_FF_PATH + "/bin/"
path_to_dex_fixer = DROID_FF_PATH + "/bin/dexRepair"
path_to_thridparty = DROID_FF_PATH + "/third_party/"
path_to_unique_crashes = DROID_FF_PATH + "/unique_crashes/"
#android binary which needs to be fuzzed
target_android_executable = "/system/xbin/dexdump"
