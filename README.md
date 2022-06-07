# Droid-FF : 

Install python dependencies (setup.sh ) and you are good to go.

GDB Server for android :  get it from @ wget https://people.mozilla.org/~nchen/jimdb/jimdb-arm-linux_x64.tar.bz2 
Credits to @ https://wiki.mozilla.org/Mobile/Fennec/Android/GDB


Run the android emulator. (The example with dexdump requires Android 4.4 KitKat)

Run python droif-ff.py

Update the fuzzerConfig.py paths to fit your setup and create four folders for the results, namely:
 - confirmed_crashes
 - crashes
 - generated_samples_folder
 - unique_crashes

Conference Slides : http://conference.hitb.org/hitbsecconf2016ams/wp-content/uploads/2015/11/D1T3-Anto-Joseph-Droid-FF.pdf

If something doesnt work , feel free to create an issue and i will fix / help you with that
 
