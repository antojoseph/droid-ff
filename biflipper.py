from pyZZUF import *
import os.path
import threading


def test_flipping():
    for x in range(100, 200):
        print pyZZUF(str(x)).mutate()


def open_file_and_return_bite_array(path):
    with open(path, "rb") as sampleFile:
        f = sampleFile.read()
        b = bytearray(f)

    return b


def thread_it(fuzz_range_start, fuzz_range_end, number_of_samples, data_to_be_flipped, extension):
    for x in range(0, int(number_of_samples)):
        zzuf = pyZZUF(data_to_be_flipped)
        # Random seed (default 0)
        zzuf.set_seed(9)
        # Bit fuzzing ratio (default 0.004)
        zzuf.set_ratio(0.91)
        # Only fuzz bytes at offsets within <ranges>
        zzuf.set_fuzz_bytes([[fuzz_range_start, fuzz_range_end]])
        # zzuf.set_fuzz_bytes([[0, 3], [6, EOF]])
        # Fuzzing mode <mode> ([xor] set unset)
        zzuf.set_fuzz_mode(FUZZ_MODE_XOR)
        with open("generated_samples_folder/" + "sample" + str(x) + "-" + str(fuzz_range_start) + "-" + str(
                fuzz_range_end) + extension, 'wb') as output:
            output.write(zzuf.mutate())


def flipp():
    # sample_path = raw_input("Provide path to a sample file :")
    # only for testing, uncomment in prod
    sample_path = "mutation_sample/sample.dex"
    num_sample = raw_input("Provide the number of Samples to be Generated : ")
    # make threading dynamic , for now sticking to 4 threads
    # number_of_threads = raw_input("Number of Threads to be used :")
    extension = os.path.splitext(sample_path)[1]

    data_to_be_flipped = open_file_and_return_bite_array(sample_path)
    arr_len = len(data_to_be_flipped)
    sample_count_per_thread = int(num_sample) / 4

    try:
        one = threading.Thread(target=thread_it,
                               args=(0, arr_len / 4, sample_count_per_thread, data_to_be_flipped, extension,))
        two = threading.Thread(target=thread_it,
                               args=(arr_len / 4, arr_len / 2, sample_count_per_thread, data_to_be_flipped, extension,))
        three = threading.Thread(target=thread_it, args=(
        arr_len / 2, arr_len / 4 + arr_len / 2, sample_count_per_thread, data_to_be_flipped, extension,))
        four = threading.Thread(target=thread_it, args=(
        arr_len / 4 + arr_len / 2, arr_len, sample_count_per_thread, data_to_be_flipped, extension,))
        one.start()
        two.start()
        three.start()
        four.start()
    except Exception, e:
        print e


        # for testing flipping , mostly comment the line underneath
        # test_flipping()
        # run the bitflipper
        # flipp()
