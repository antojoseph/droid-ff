#!/usr/bin/env bash
pip install pyZZUF
pip install adb_android

#folders for the fuzzer
mkdir -p $HOME"/myfuzzer/fuzzer"
mkdir -p $HOME"/myfuzzer/fuzzer/confirmed_crashes/"
mkdir -p $HOME"/myfuzzer/fuzzer/crashes/"
mkdir -p $HOME"/myfuzzer/fuzzer/generated_samples_folder/"
