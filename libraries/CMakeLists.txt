function(make_library)
  string(REPLACE " " "_" LIBRARY_NAME "${CMAKE_PROJECT_NAME}_${ARGV0}${EXTENSION}")
  set(${LIBRARY_NAME} "${ARGV0}" PARENT_SCOPE)
  add_subdirectory("${ARGV0}")
  list(TRANSFORM SOURCE_FILES PREPEND "${ARGV0}/")

  # Create javascript default target
  add_library("${LIBRARY_NAME}" "${SOURCE_FILES}")
  target_include_directories("${LIBRARY_NAME}" PUBLIC
      "${LIBRARY_INCLUDES}"
      "${CMAKE_SOURCE_DIR}")
  target_compile_options("${LIBRARY_NAME}" PUBLIC ${LIBRARY_CFLAGS} ${SANITIZERS})
  target_link_libraries("${LIBRARY_NAME}" PUBLIC ${LIBRARY_LIBRARIES})

endfunction()

make_library("delta")
