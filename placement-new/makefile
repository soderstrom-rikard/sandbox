BIN=placement-new
SRC=main.cpp
FLAGS=-g -fsanitize=address -fsanitize=leak -fsanitize=undefined -fsanitize=shift -fsanitize=shift-exponent  \
         -fsanitize=shift-base -fsanitize=integer-divide-by-zero -fsanitize=unreachable -fsanitize=vla-bound \
         -fsanitize=null -fsanitize=return -fsanitize=signed-integer-overflow -fsanitize=bounds              \
         -fsanitize=bounds-strict -fsanitize=alignment -fsanitize=object-size -fsanitize=float-divide-by-zero\
         -fsanitize=float-cast-overflow -fsanitize=nonnull-attribute -fsanitize=returns-nonnull-attribute    \
         -fsanitize=bool -fsanitize=enum -fsanitize=vptr -fsanitize-address-use-after-scope                  \
         -fsanitize-undefined-trap-on-error

${BIN}: ${SRC}
	g++ --std=c++1z ${FLAGS} -o $@ ${SRC}

memcheck callgrind: ${BIN}
	valgrind --tool=$@ ./${BIN}

test: memcheck callgrind

clean:
	git clean -fd
           -fsanitize-recover=style -fasan-shadow-offset=number  -fsanitize-sections=s1,s2,...  -fsanitize-undefined-trap-on-error  -fbounds-check
