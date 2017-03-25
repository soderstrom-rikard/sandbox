BIN=pure-virtual-interface
SRC=main.cpp

${BIN}: ${SRC}
	g++ --std=c++14 -o $@ ${SRC}

memcheck callgrind: ${BIN}
	valgrind --tool=$@ ./${BIN}

test: memcheck callgrind

clean:
	rm -f ${BIN} callgrind.out.*
