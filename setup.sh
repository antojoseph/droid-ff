#!/usr/bin/env bash
pip install pyZZUF
pip install adb_android

#folders for the fuzzer
mkdir $HOME"/myfuzzer/fuzzer/confirmed_crashes/"
mkdir $HOME"/myfuzzer/fuzzer/crashes/"
mkdir $HOME"/myfuzzer/fuzzer/generated_samples_folder/"
