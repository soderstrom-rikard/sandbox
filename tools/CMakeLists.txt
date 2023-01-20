function(add_tool)
  string(REPLACE " " "_" TOOL_NAME "${CMAKE_PROJECT_NAME}_${ARGV0}${EXTENSION}")
  set(${TOOL_NAME} "${ARGV0}" PARENT_SCOPE)
  add_subdirectory("${ARGV0}")
  list(TRANSFORM SOURCE_FILES PREPEND "${ARGV0}/")

  # Create javascript default target
  add_executable("${TOOL_NAME}" "${SOURCE_FILES}")
  target_include_directories("${TOOL_NAME}" PUBLIC
      "${EXAMPLE_INCLUDES}"
      "${CMAKE_SOURCE_DIR}"
  )
  target_compile_options("${TOOL_NAME}" PUBLIC ${EXAMPLE_CFLAGS} ${SANITIZERS})
  target_link_libraries("${TOOL_NAME}" PUBLIC ${EXAMPLE_LIBRARIES})

endfunction()

add_tool("cli")
