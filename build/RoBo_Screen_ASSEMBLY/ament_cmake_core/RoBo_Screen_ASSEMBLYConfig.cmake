# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_RoBo_Screen_ASSEMBLY_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED RoBo_Screen_ASSEMBLY_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(RoBo_Screen_ASSEMBLY_FOUND FALSE)
  elseif(NOT RoBo_Screen_ASSEMBLY_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(RoBo_Screen_ASSEMBLY_FOUND FALSE)
  endif()
  return()
endif()
set(_RoBo_Screen_ASSEMBLY_CONFIG_INCLUDED TRUE)

# output package information
if(NOT RoBo_Screen_ASSEMBLY_FIND_QUIETLY)
  message(STATUS "Found RoBo_Screen_ASSEMBLY: 1.0.0 (${RoBo_Screen_ASSEMBLY_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'RoBo_Screen_ASSEMBLY' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${RoBo_Screen_ASSEMBLY_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(RoBo_Screen_ASSEMBLY_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${RoBo_Screen_ASSEMBLY_DIR}/${_extra}")
endforeach()
