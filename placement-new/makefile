BIN=placement-new
SRC=main.cpp

${BIN}: ${SRC}
	g++ --std=c++14 -o $@ ${SRC}

memcheck callgrind: ${BIN}
	valgrind --tool=$@ ./${BIN}

test: memcheck callgrind
