CC=gcc
CFLAGS= -Wall -Werror -g 
LIBS=-lcunit -lpthread -lm
INCLUDE_HEADERS_DIRECTORY=-Iheaders

main:
	@$(CC) src/philosophe.c -o philosophe $(CFLAGS)

clean:
	rm -f *.o
	rm -f *.out
	rm -f *.exe
	rm -f *.so
	rm -f *.a
	rm -f *.d
	rm philosophe