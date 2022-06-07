import os
import fuzzerConfig

new_crashes = []

#Move files to triage folder
def move_crashes_to_triage():
    try:
        for x in range(0,len(new_crashes)):
            print new_crashes[x]

            if  os.path.isfile(fuzzerConfig.path_to_generated_samples+new_crashes[x]):
                os.rename(fuzzerConfig.path_to_generated_samples+new_crashes[x], fuzzerConfig.path_for_crash_samples+new_crashes[x])
    except Exception, e:
        print str(e)

def process(filename):
    offset_line_to_file = 2
    f = open(filename, "r")
    lines = f.readlines()

    #parse every line of the current log
    print "Total Number of lines " +str(len(lines))
    for x in range(0, len(lines)):

            strings = ("SIGSEGV", "SIGSEGV", "SIGFPE","SIGILL")
            if any(s in lines[x - offset_line_to_file] for s in strings):
              if "F/libc" in lines[x]:
                if "F/CRASH_LOGGER" in lines[x - offset_line_to_file]:
                    new_crashes.append(lines[x - offset_line_to_file][32:].strip())

    move_crashes_to_triage()