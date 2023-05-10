# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_roboassembly_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED roboassembly_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(roboassembly_FOUND FALSE)
  elseif(NOT roboassembly_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(roboassembly_FOUND FALSE)
  endif()
  return()
endif()
set(_roboassembly_CONFIG_INCLUDED TRUE)

# output package information
if(NOT roboassembly_FIND_QUIETLY)
  message(STATUS "Found roboassembly: 1.0.0 (${roboassembly_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'roboassembly' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${roboassembly_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(roboassembly_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${roboassembly_DIR}/${_extra}")
endforeach()
