# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/herve/Documents/gr-nordic_38

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/herve/Documents/gr-nordic_38/build

# Utility rule file for nordic_docstrings.

# Include any custom commands dependencies for this target.
include python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/compiler_depend.make

# Include the progress variables for this target.
include python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/progress.make

python/nordic/bindings/CMakeFiles/nordic_docstrings: python/nordic/bindings/docstring_status

python/nordic/bindings/docstring_status:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/herve/Documents/gr-nordic_38/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Adding docstrings into nordic pybind headers ..."
	cd /home/herve/Documents/gr-nordic_38/build/python/nordic/bindings && /usr/bin/python3 /home/herve/Documents/gr-nordic_38/docs/doxygen/update_pydoc.py sub --json_path /home/herve/Documents/gr-nordic_38/build/python/nordic/bindings/extracted_docstrings.json --bindings_dir /home/herve/Documents/gr-nordic_38/python/nordic/bindings/docstrings --output_dir /home/herve/Documents/gr-nordic_38/build/python/nordic/bindings --filter gr::nordic

nordic_docstrings: python/nordic/bindings/CMakeFiles/nordic_docstrings
nordic_docstrings: python/nordic/bindings/docstring_status
nordic_docstrings: python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/build.make
.PHONY : nordic_docstrings

# Rule to build all files generated by this target.
python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/build: nordic_docstrings
.PHONY : python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/build

python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/clean:
	cd /home/herve/Documents/gr-nordic_38/build/python/nordic/bindings && $(CMAKE_COMMAND) -P CMakeFiles/nordic_docstrings.dir/cmake_clean.cmake
.PHONY : python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/clean

python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/depend:
	cd /home/herve/Documents/gr-nordic_38/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/herve/Documents/gr-nordic_38 /home/herve/Documents/gr-nordic_38/python/nordic/bindings /home/herve/Documents/gr-nordic_38/build /home/herve/Documents/gr-nordic_38/build/python/nordic/bindings /home/herve/Documents/gr-nordic_38/build/python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : python/nordic/bindings/CMakeFiles/nordic_docstrings.dir/depend

