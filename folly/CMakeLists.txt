add_library(
    follybenchmark
    Benchmark.cpp
)
target_link_libraries(follybenchmark PUBLIC folly)
apply_folly_compile_options_to_target(follybenchmark)
install(
  TARGETS follybenchmark
  EXPORT folly
  RUNTIME DESTINATION ${BIN_INSTALL_DIR}
  LIBRARY DESTINATION ${LIB_INSTALL_DIR}
  ARCHIVE DESTINATION ${LIB_INSTALL_DIR}
)

add_subdirectory(experimental/exception_tracer)

if (PYTHON_EXTENSIONS)
  # Create tree of symbolic links in structure required for successful
  # compliation by Cython.
  #   - must be in path named same as extension

  set(_cybld "${CMAKE_CURRENT_BINARY_DIR}/cybld")
  include_directories(${PYTHON_INCLUDE_DIRS}
                      ${CMAKE_SOURCE_DIR}
                      ${CMAKE_BINARY_DIR}
  )
  file(MAKE_DIRECTORY "${_cybld}/folly")
  foreach(_src
    "executor.pxd"
    "executor.pyx"
    "futures.pxd"
    "range.pxd"
    "__init__.pxd"
    "AsyncioExecutor.h")
    add_custom_command(OUTPUT "${_cybld}/folly/${_src}" ALL
      COMMAND
        ${CMAKE_COMMAND} -E create_symlink
        ${CMAKE_CURRENT_SOURCE_DIR}/python/${_src}
        "${_cybld}/folly/${_src}"
      COMMENT
        "Linking ${CMAKE_CURRENT_SOURCE_DIR}/python/${_src} "
        "to ${_cybld}/folly/${_src}"
    )

  endforeach()

  add_custom_command(OUTPUT "${_cybld}/folly/executor.cpp"
    COMMAND ${CYTHON_EXE} --fast-fail -3 --cplus
      ${_cybld}/folly/executor.pyx -o "${_cybld}/folly/executor.cpp"
    COMMENT "Generating executor.cpp using Cython"
    DEPENDS
      "${_cybld}/folly/executor.pyx"
      "${_cybld}/folly/executor.pxd"
      "${_cybld}/folly/futures.pxd"
      "${_cybld}/folly/range.pxd"
      "${_cybld}/folly/__init__.pxd"
      "${_cybld}/folly/AsyncioExecutor.h"
  )

  python_add_module(executor "${_cybld}/folly/executor.cpp")
  target_link_libraries(executor folly_pic folly_deps)

  install(
    FILES ${_cybld}/folly/executor_api.h
    DESTINATION ${INCLUDE_INSTALL_DIR}/folly/python
    COMPONENT dev
  )

  # Install Folly Python Bindings
  install(CODE "
    execute_process(COMMAND
    python3 ${CMAKE_CURRENT_SOURCE_DIR}/setup.py install
    WORKING_DIRECTORY ${_cybld})")
endif ()
