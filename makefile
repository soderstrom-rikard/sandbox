# -std=c++11 available since gcc version 4.8.1
# -std=c++14 available since gcc version 5.0, default since 6.1
# -std=c++17 available since gcc version 7.0, not yet default, some aspects still considered experimental
BINDIR=bin
BIN=${BINDIR}/elemental-electronics
SANITIZERS=$(addprefix -fsanitize=,address leak undefined shift shift-exponent shift-base integer-divide-by-zero unreachable vla-bound null return signed-integer-overflow bounds bounds-strict alignment object-size float-divide-by-zero float-cast-overflow nonnull-attribute returns-nonnull-attribute bool enum vptr)
WARNINGS=$(addprefix -W,all conversion extra shadow strict-aliasing error pedantic pointer-compare old-style-cast)
DEBUG=-ggdb3 -Og

OBJDIR=obj
COMPILATION_UNITS=main elements
PRECOMPILED_HEADER_UNITS=elements
OBJS=$(addsuffix .o,$(addprefix ${OBJDIR}/,${COMPILATION_UNITS}))
#GCHS=$(addsuffix .h.gch,$(addprefix ${OBJDIR}/,${PRECOMPILED_HEADER_UNITS}))
OBJS_SANE=$(addsuffix -sane.o,$(addprefix ${OBJDIR}/,${COMPILATION_UNITS}))
#GCHS_SANE=$(addsuffix -sane.h.gch,$(addprefix ${OBJDIR}/,${PRECOMPILED_HEADER_UNITS}))
LIBS=$(shell pkg-config --libs sdl2 SDL2_image SDL2_mixer SDL2_ttf)
INCLUDES=$(shell pkg-config --cflags sdl2 SDL2_image SDL2_mixer SDL2_ttf)

${BIN}: ${OBJS} ${GCHS} makefile
	mkdir -p ${BINDIR}
	g++ --std=c++17 $(LIBS) $(INCLUDES) $(WARNINGS) $(DEBUG) -o $@ ${OBJS} ${GCHS}

${OBJDIR}/%.h.gch: %.h
	mkdir -p ${OBJDIR}
	g++ --std=c++17 ${LIBS} ${INCLUDES} ${WARNINGS} ${DEBUG} -o $@ -c $<

${OBJDIR}/%.o: %.cpp
	mkdir -p ${OBJDIR}
	g++ --std=c++17 ${LIBS} ${INCLUDES} ${WARNINGS} ${DEBUG} -o $@ -c $<

${BIN}-sane: ${OBJS_SANE} ${GCHS_SANE} makefile
	mkdir -p ${BINDIR}
	g++ --std=c++17 -lasan $(LIBS) $(INCLUDES) $(WARNINGS) $(SANITIZERS) $(DEBUG) -o $@ ${OBJS_SANE} ${GCHS_SANE}

${OBJDIR}/%-sane.o: %.cpp
	mkdir -p ${OBJDIR}
	g++ --std=c++17 ${LIBS} ${INCLUDES} ${WARNINGS} $(SANITIZERS) ${DEBUG} -o $@ -c $<

${OBJDIR}/%-sane.h.gch: %.h
	mkdir -p ${OBJDIR}
	g++ --std=c++17 ${LIBS} ${INCLUDES} ${WARNINGS} ${DEBUG} -o $@ -c $<

memcheck callgrind: ${BIN}
	valgrind --tool=$@ ./${BIN}

test: memcheck callgrind

purge:
	rm -f ${BIN} callgrind.out.*
	rm -rf ${OBJDIR} ${BINDIR}

clean:
	rm -f ${BIN} callgrind.out.*
