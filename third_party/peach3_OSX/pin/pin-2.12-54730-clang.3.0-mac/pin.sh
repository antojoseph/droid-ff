#!/bin/bash
# get the directory of this script
origin=$0
# If it does not begin with /, then it is relative to the current working directory
if [ "${origin:0:1}" != "/" ]; then
    origin=$PWD/$origin
fi
origin=`dirname $origin`

# If variables we are going to modify are set, save the value. They will be restored 
# after the injector starts
if [ -n "${DYLD_LIBRARY_PATH+x}" ]
then
    export PIN_APP_DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH
    export PIN_DYLD_RESTORE_REQUIRED=t
fi

exec "$origin"/ia32/bin/pinbin -p64 "$origin"/intel64/bin/pinbin "${@}"


