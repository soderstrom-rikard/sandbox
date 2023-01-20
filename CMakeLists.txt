cmake_minimum_required(VERSION 3.23)

# set the project name and version
project(filecast VERSION 0.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

if (DEFINED BUILD_WITH_SANITIZERS)
  set(SANITIZERS
           "-fsanitize=address"
           "-fsanitize=leak"
           "-fsanitize=undefined"
           "-fsanitize=shift"
           "-fsanitize=shift-exponent"
           "-fsanitize=shift-base"
           "-fsanitize=integer-divide-by-zero"
           "-fsanitize=unreachable"
           "-fsanitize=vla-bound"
           "-fsanitize=null"
           "-fsanitize=return"
           "-fsanitize=signed-integer-overflow"
           "-fsanitize=bounds"
           "-fsanitize=alignment"
           "-fsanitize=object-size"
           "-fsanitize=float-divide-by-zero"
           "-fsanitize=float-cast-overflow"
           "-fsanitize=nonnull-attribute"
           "-fsanitize=returns-nonnull-attribute"
           "-fsanitize=bool"
           "-fsanitize=enum"
           "-fsanitize=vptr"
           "-fsanitize-address-use-after-scope"
    )
    add_link_options(
      "-fsanitize=address"
      "-fsanitize=undefined"
    )
  message(STATUS "building with SANITIZERS=${SANITIZERS}")
else()
  set(SANITIZERS "")
  message(STATUS "building without SANITIZERS=${SANITIZERS}")
endif()


if (${CMAKE_CXX_COMPILER} MATCHES "em\\+\\+$")
  set(EXTENSION ".html")
  add_compile_options("-fexceptions")
  add_link_options("-fexceptions")
  message(STATUS "building with emscripten")
else()
  set(EXTENSION ".native")
  message(STATUS "building with native (or user defined)")
endif()

add_subdirectory("libraries")
add_subdirectory("tools")
