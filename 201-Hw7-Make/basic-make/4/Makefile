# Variables
CC = gcc
BIN = sum30
SRCS = $(wildcard src/*.c)

# Default target
all: $(BIN)

# Rule to build the executable
$(BIN): $(SRCS)
	$(CC) $^ -o $@

# Phony targets
.PHONY: all clean

# Clean up
clean:
	rm -f $(BIN)
