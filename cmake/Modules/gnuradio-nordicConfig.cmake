find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_NORDIC gnuradio-nordic)

FIND_PATH(
    GR_NORDIC_INCLUDE_DIRS
    NAMES gnuradio/nordic/api.h
    HINTS $ENV{NORDIC_DIR}/include
        ${PC_NORDIC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_NORDIC_LIBRARIES
    NAMES gnuradio-nordic
    HINTS $ENV{NORDIC_DIR}/lib
        ${PC_NORDIC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-nordicTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_NORDIC DEFAULT_MSG GR_NORDIC_LIBRARIES GR_NORDIC_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_NORDIC_LIBRARIES GR_NORDIC_INCLUDE_DIRS)
