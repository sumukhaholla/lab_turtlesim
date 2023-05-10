# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_roBo_ASSEMBLY_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED roBo_ASSEMBLY_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(roBo_ASSEMBLY_FOUND FALSE)
  elseif(NOT roBo_ASSEMBLY_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(roBo_ASSEMBLY_FOUND FALSE)
  endif()
  return()
endif()
set(_roBo_ASSEMBLY_CONFIG_INCLUDED TRUE)

# output package information
if(NOT roBo_ASSEMBLY_FIND_QUIETLY)
  message(STATUS "Found roBo_ASSEMBLY: 1.0.0 (${roBo_ASSEMBLY_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'roBo_ASSEMBLY' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${roBo_ASSEMBLY_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(roBo_ASSEMBLY_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${roBo_ASSEMBLY_DIR}/${_extra}")
endforeach()
