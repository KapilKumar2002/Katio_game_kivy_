# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
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
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg

# Include any dependencies generated for this target.
include CMakeFiles/wrjpgcom.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/wrjpgcom.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/wrjpgcom.dir/flags.make

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o: CMakeFiles/wrjpgcom.dir/flags.make
CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o: wrjpgcom.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o"
	/home/keps/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=armv7-none-linux-androideabi16 --gcc-toolchain=/home/keps/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64 --sysroot=/home/keps/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o   -c /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/wrjpgcom.c

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/wrjpgcom.dir/wrjpgcom.c.i"
	/home/keps/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=armv7-none-linux-androideabi16 --gcc-toolchain=/home/keps/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64 --sysroot=/home/keps/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/wrjpgcom.c > CMakeFiles/wrjpgcom.dir/wrjpgcom.c.i

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/wrjpgcom.dir/wrjpgcom.c.s"
	/home/keps/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=armv7-none-linux-androideabi16 --gcc-toolchain=/home/keps/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64 --sysroot=/home/keps/.buildozer/android/platform/android-ndk-r23b/toolchains/llvm/prebuilt/linux-x86_64/sysroot $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/wrjpgcom.c -o CMakeFiles/wrjpgcom.dir/wrjpgcom.c.s

# Object files for target wrjpgcom
wrjpgcom_OBJECTS = \
"CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o"

# External object files for target wrjpgcom
wrjpgcom_EXTERNAL_OBJECTS =

wrjpgcom: CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o
wrjpgcom: CMakeFiles/wrjpgcom.dir/build.make
wrjpgcom: CMakeFiles/wrjpgcom.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable wrjpgcom"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/wrjpgcom.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/wrjpgcom.dir/build: wrjpgcom

.PHONY : CMakeFiles/wrjpgcom.dir/build

CMakeFiles/wrjpgcom.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/wrjpgcom.dir/cmake_clean.cmake
.PHONY : CMakeFiles/wrjpgcom.dir/clean

CMakeFiles/wrjpgcom.dir/depend:
	cd /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /home/keps/VScodeProjects/Katio/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/CMakeFiles/wrjpgcom.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/wrjpgcom.dir/depend

