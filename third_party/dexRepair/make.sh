#!/bin/bash

# --{ Android build config }--
# If empty string try to recover from path
NDK=""
#NDK=/Developer/android/android-ndk-r10d/
# --{ End of Android build config }--

readonly MAKE=$(which make)

function usage()
{
  echo "$(basename $0) [gcc|clang|cross-android] (default is gcc)"
  exit 1
}

function build_cross_android()
{
  # Search path for NDK if empty string
  if [[ "$NDK" == "" ]]; then
    for i in $(echo $PATH | tr ":" "\n")
    do
      if echo "$i" | grep -q "android-ndk"; then
        if [ -f $i/ndk-build ]; then
          NDK=$i
        fi
      fi
    done
  fi
  if [[ "$NDK" == "" ]]; then
      echo "[-] Could not detect Android NDK dir"
      exit 1
  fi

  ndk-build clean
  ndk-build
  if [ $? -ne 0 ]; then
    echo "[-] android build failed"
    exit 1
  fi
}

function build_gcc()
{
  make clean -C src
  cc=gcc make -C src
  if [ $? -ne 0 ]; then
    echo "[-] gcc build failed"
    exit 1
  fi
}

function build_clang()
{
  make clean -C src
  CC=clang make -C src
  if [ $? -ne 0 ]; then
    echo "[-] clang build failed"
    exit 1
  fi
}

if [[ "$MAKE" == "" ]]; then
  echo "[-] Missing make utils"
  exit 1
fi

if [ $# -gt 1 ]; then
  echo "[-] Invalid args"
  exit 0
fi

case "$1" in
  "") build_gcc;;
  "gcc") build_gcc;;
  "clang") build_clang;;
  "cross-android") build_cross_android;;
  *) usage;;
esac
 
