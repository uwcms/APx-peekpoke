all: peek poke

poke: poke.c
	$(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)

peek: peek.c
	$(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)

clean:
	-rm -f peek poke *.rpm
