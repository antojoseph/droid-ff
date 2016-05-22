import os

def start():
    # sample_path = raw_input("Provide path to a pit file :")
    # only for testing, uncomment in prod
    pit_path = "third_party/peach3/pits/wav.xml"
    num_sample = raw_input("Provide the number of Samples to be Generated : ")
    # make threading dynamic , for now sticking to 4 threads
    # number_of_threads = raw_input("Number of Threads to be used :")
    # ./peach - -range 0, 100 pits/wav.xml
    result = os.system("third_party/peach3/peach --range 0,"+num_sample+" "+pit_path)
