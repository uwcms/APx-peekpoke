CFLAGS := $(CFLAGS) -Wall

all: peek poke

poke: poke.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LDLIBS)

peek: peek.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LDLIBS)

clean:
	-rm -f peek poke *.rpm
