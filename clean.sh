#!/usr/bin/env bash
echo "This will delete all your generated files / crashes / etc "

"rm" $HOME"/myfuzzer/fuzzer/confirmed_crashes/*"
"rm" $HOME"/myfuzzer/fuzzer/crashes/*"
"rm" $HOME"/myfuzzer/fuzzer/generated_samples_folder/*"