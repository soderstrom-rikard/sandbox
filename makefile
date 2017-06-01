BIN=bitpacker
SRC=main.cpp

${BIN}: ${SRC}
	g++ --std=c++14 -o $@ ${SRC}

memcheck callgrind: ${BIN}
	valgrind --tool=$@ ./${BIN}

objdump: ${BIN}
	objdump -S ${BIN} > ${BIN}-elf.asm

test: memcheck callgrind objdump

clean:
	rm -f ${BIN} ${BIN}-elf.asm callgrind.out.*
