# CMake generated Testfile for 
# Source directory: /home/herve/Documents/gr-nordic_38/python/nordic
# Build directory: /home/herve/Documents/gr-nordic_38/build/python/nordic
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(qa_nordic_rx "/usr/bin/sh" "qa_nordic_rx_test.sh")
set_tests_properties(qa_nordic_rx PROPERTIES  _BACKTRACE_TRIPLES "/usr/local/lib/cmake/gnuradio/GrTest.cmake;119;add_test;/home/herve/Documents/gr-nordic_38/python/nordic/CMakeLists.txt;43;GR_ADD_TEST;/home/herve/Documents/gr-nordic_38/python/nordic/CMakeLists.txt;0;")
add_test(qa_nordic_tx "/usr/bin/sh" "qa_nordic_tx_test.sh")
set_tests_properties(qa_nordic_tx PROPERTIES  _BACKTRACE_TRIPLES "/usr/local/lib/cmake/gnuradio/GrTest.cmake;119;add_test;/home/herve/Documents/gr-nordic_38/python/nordic/CMakeLists.txt;44;GR_ADD_TEST;/home/herve/Documents/gr-nordic_38/python/nordic/CMakeLists.txt;0;")
subdirs("bindings")
