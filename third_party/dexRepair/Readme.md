# Dex Repair

Command line tool to repair Android DEX bytecode files CRC checksum.


## Compile

* Clone this repository
* Install Android NDK if you want to cross-compile for Android devices
* Invoke ```make.sh``` bash script with desired build target
* Executables are copied under the ```bin``` path
* Repair your dirty files :)

## Usage

```
anestisb@deephole:[dexRepair]:
anestisb@deephole:[dexRepair]: bin/dexRepair -h

  -I,  --input-files=DIR : input files dirs (1 level recursion only) or single file
  -h,  --help            : this help
  -v,  --debug=LEVEL     : debug level (0 - FATAL ... 4 - DEBUG), default: '3' (INFO)

anestisb@deephole:[dexRepair]:
anestisb@deephole:[dexRepair]: bin/dexRepair -I /tmp/samples

[INFO] 12 input files have been added to the list
[WARNING] Invalid magic number. Skipping 'samples/invalid_file'
[INFO] 11 our of 12 files have been successfully repaired
[INFO] Repaired DEX files available at '/tmp/samples'
```

## Changelog

* __0.1.0__ - 14 February 2015
  * Initial commit

## License

```
   Anestis Bechtsoudis <anestis@census-labs.com>
   Copyright 2015 by CENSUS S.A. All Rights Reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```