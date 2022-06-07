import os
import fuzzerConfig

def start():
    for file in os.listdir(fuzzerConfig.path_for_confirmed_samples):
        os.remove(file)
    for file in os.listdir(fuzzerConfig.path_for_crash_samples):
        os.remove(file)
    for file in os.listdir(fuzzerConfig.path_to_generated_samples):
        os.remove(file)
    print "Removed all generated files!"