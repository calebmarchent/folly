



execute_process(COMMAND cython --version
	        RESULT_VARIABLE _cython_retcode
                OUTPUT_VARIABLE _cython_output
		ERROR_VARIABLE _cython_output
                OUTPUT_STRIP_TRAILING_WHITESPACE)

if (${_cython_retcode} EQUAL 0)
  message(STATUS "Found Cython ${_cython_output}")
else ()
  message(STATUS "Found Cython NOT FOUND")
endif ()
