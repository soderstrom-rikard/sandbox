BIN=double-linked-list-nostl
SRC=main.cpp
INCLUDES=dlist.hpp

${BIN}: ${SRC} ${INCLUDES}
	g++ --std=c++14 -g -O0 -o $@ ${SRC}

memcheck callgrind: ${BIN}
	valgrind --tool=$@ ./${BIN}

objdump: ${BIN}
	objdump -S ${BIN} > ${BIN}-elf.asm

test: memcheck callgrind objdump

clean:
	rm -f ${BIN} ${BIN}-elf.asm callgrind.out.*
