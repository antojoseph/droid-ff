import fuzzerConfig
import os


def radamsa_do(sample_path,extension,num_sample):
    for x in range(0,int(num_sample)):
        os.system(fuzzerConfig.path_to_fuzzer_binaries+"radamsa "+sample_path+" -o "+fuzzerConfig.path_to_generated_samples+"sample"+str(x)+extension)

    print "done"

def start():
    print "hi"
    # sample_path = raw_input("Provide path to a sample file :")
    # only for testing, uncomment in prod
    sample_path = fuzzerConfig.path_to_mutation_sample+"sample.dex"
    num_sample = raw_input("Provide the number of Samples to be Generated : ")
    # make threading dynamic , for now sticking to 4 threads
    # number_of_threads = raw_input("Number of Threads to be used :")
    extension = os.path.splitext(sample_path)[1]
    radamsa_do(sample_path,extension,num_sample)