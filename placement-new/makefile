CPP=g++
BIN=placement-new
SRC=main.cpp
CPP_ARGS=--std=c++14 -Wall -Weffc++ -Wpedantic

${BIN}: ${SRC}
	${CPP} ${CPP_ARGS} -o $@ ${SRC}

memcheck callgrind: ${BIN}
	valgrind --tool=$@ ./${BIN}

static-analysis: ${SRC}
	cppcheck ${SRC}

test: memcheck callgrind static-analysis
