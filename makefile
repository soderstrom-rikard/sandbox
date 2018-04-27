# -std=c++11 available since gcc version 4.8.1
# -std=c++14 available since gcc version 5.0, default since 6.1
# -std=c++17 available since gcc version 7.0, not yet default, some aspects still considered experimental
BIN=simple-interactive-console
SRC=main.cpp
SANITIZERS=$(addprefix -fsanitize=,address leak undefined)
WARNINGS=$(addprefix -W,all conversion extra shadow strict-aliasing error pedantic pointer-compare)
DEBUG=-ggdb3 -Og
LIBRARIES=$(addprefix -l,readline)

${BIN}: ${SRC} makefile
	g++ --std=c++17 $(WARNINGS) $(SANITIZERS) $(DEBUG) $(LIBRARIES) -o $@ ${SRC}

memcheck callgrind: ${BIN}
	valgrind --tool=$@ ./${BIN}

test: memcheck callgrind

clean:
	rm -f ${BIN} callgrind.out.*
