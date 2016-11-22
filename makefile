# -std=c++11 available since gcc version 4.8.1
# -std=c++14 available since gcc version 5.0, default since 6.1
# -std=c++17 available since gcc version 7.0, not yet default, some aspects still considered experimental
BIN=sdl-intro
SRC=main.cpp
SANITIZERS=$(addprefix -fsanitize=,address leak undefined shift shift-exponent shift-base integer-divide-by-zero unreachable vla-bound null return signed-integer-overflow bounds bounds-strict alignment object-size float-divide-by-zero float-cast-overflow nonnull-attribute returns-nonnull-attribute bool enum vptr)
WARNINGS=$(addprefix -W,all conversion extra shadow strict-aliasing error pedantic pointer-compare old-style-cast)

DEBUG=-ggdb3 -Og

LIBS=$(shell pkg-config --libs sdl2 SDL2_image SDL2_mixer)
INCLUDES=$(shell pkg-config --cflags sdl2 SDL2_image SDL2_mixer)

${BIN}: ${SRC} makefile
	g++ --std=c++17 $(LIBS) $(INCLUDES) $(WARNINGS) $(DEBUG) -o $@ ${SRC}

${BIN}-sane: ${SRC} makefile
	g++ --std=c++17 -lasan $(LIBS) $(INCLUDES) $(WARNINGS) $(SANITIZERS) $(DEBUG) -o $@ ${SRC}

memcheck callgrind: ${BIN}
	valgrind --tool=$@ ./${BIN}

test: memcheck callgrind

clean:
	rm -f ${BIN} callgrind.out.*
