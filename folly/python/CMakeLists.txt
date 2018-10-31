set(CMAKE_MODULE_PATH
    "/home/ubuntu/upstream/scikit-build/skbuild/resources/cmake"
    ${CMAKE_MODULE_PATH})

find_package(Cython REQUIRED)

set(CYTHON_FLAGS "--fail-fast")

include_directories(${CMAKE_CURRENT_BINARY_DIR})


add_cython_target(folly
                  executor.pyx)


