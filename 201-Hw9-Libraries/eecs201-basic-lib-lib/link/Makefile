.PHONY: all
all: app-dynamic app-static

ifeq ($(shell uname),Linux)
dyvar = LD_LIBRARY_PATH=./
else ifeq ($(shell uname),Darwin)
dyvar = DYLD_LIBRARY_PATH=./
endif

app-dynamic:
	gcc -o $@ main.c -L./ -lthingy

app-static:
	gcc -o $@ main.c ./libthingy.a

.PHONY: run-dynamic
run-dynamic: app-dynamic
	$(dyvar) ./app-dynamic

.PHONY: run-static
run-static: app-static
	./app-static

.PHONY: clean
clean:
	rm -f app-dynamic app-static
