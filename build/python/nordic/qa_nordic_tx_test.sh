#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir="/home/herve/Documents/gr-nordic_38/python/nordic"
export GR_CONF_CONTROLPORT_ON=False
export PATH="/home/herve/Documents/gr-nordic_38/build/python/nordic":"$PATH"
export LD_LIBRARY_PATH="":$LD_LIBRARY_PATH
export PYTHONPATH=/home/herve/Documents/gr-nordic_38/build/test_modules:$PYTHONPATH
/usr/bin/python3 /home/herve/Documents/gr-nordic_38/python/nordic/qa_nordic_tx.py 
