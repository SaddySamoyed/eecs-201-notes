CXX = g++
CXXFLAGS = -g -Iinc -std=c++11

ifeq ($(shell uname),Linux)
dyvar = LD_LIBRARY_PATH=lib/
else ifeq ($(shell uname),Darwin)
dyvar = DYLD_LIBRARY_PATH=lib/
endif

.PHONY: all
all: app-dynamic app-static

libobj/static/matrix.o: libsrc/matrix.cpp
	mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

libobj/dynamic/matrix.o: libsrc/matrix.cpp
	mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -fPIC -c $< -o $@

lib/libmat.so: libobj/dynamic/matrix.o
	mkdir -p $(dir $@)
	$(CXX) -shared $< -o $@

lib/libmat.a: libobj/static/matrix.o
	mkdir -p $(dir $@)
	ar rcs $@ $<

app-dynamic: main.cpp lib/libmat.so
	$(CXX) $(CXXFLAGS) -o $@ main.cpp -Llib -lmat

app-static: main.cpp lib/libmat.a
	$(CXX) $(CXXFLAGS) -o $@ main.cpp lib/libmat.a

.PHONY: run-static
run-static: app-static
	./app-static

.PHONY: run-dynamic
run-dynamic: app-dynamic
	$(dyvar) ./app-dynamic

.PHONY: clean
clean:
	rm -rf libobj lib
	rm -f app-dynamic
	rm -f app-static
