#
# Find libglog
#
#  LIBGLOG_INCLUDE_DIR - where to find glog/logging.h, etc.
#  LIBGLOG_LIBRARY     - List of libraries when using libglog.
#  LIBGLOG_FOUND       - True if libglog found.


IF (LIBGLOG_INCLUDE_DIR)
  # Already in cache, be silent
  SET(LIBGLOG_FIND_QUIETLY TRUE)
ENDIF ()

FIND_PATH(LIBGLOG_INCLUDE_DIR glog/logging.h HINTS "/mnt/gvfs/third-party2/glog/9e89cac38a6ad7084c7de3c5a0114dd3acb5cbb9/0.3.2_fb/platform007/fe044ac/include")

FIND_LIBRARY(LIBGLOG_LIBRARY glog HINTS "/mnt/gvfs/third-party2/glog/9e89cac38a6ad7084c7de3c5a0114dd3acb5cbb9/0.3.2_fb/platform007/fe044ac/lib")

# handle the QUIETLY and REQUIRED arguments and set LIBGLOG_FOUND to TRUE if
# all listed variables are TRUE
INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(LIBGLOG DEFAULT_MSG LIBGLOG_LIBRARY LIBGLOG_INCLUDE_DIR)

MARK_AS_ADVANCED(LIBGLOG_LIBRARY LIBGLOG_INCLUDE_DIR)
