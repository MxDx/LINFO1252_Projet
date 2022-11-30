CC=gcc
CFLAGS= -Wall -Werror -g 
LIBS=-lcunit -lpthread -lm
INCLUDE_HEADERS_DIRECTORY=-Iheaders
SRC=src/stack.c
OBJ=stack.o

main:
	@$(CC) -c $(SRC) $(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@$(CC) src/philosophe.c -o philosophe $(CFLAGS)
	@echo "\n Successfully compiled philosophe.c. \n"

	@$(CC) src/producteurs-consomateur.c -o producteurs-consomateur $(OBJ) 

clean:
	@rm -f *.o
	@rm philosophe
	@rm producteurs-consomateur

debug: 
	@$(CC) -c $(SRC) $(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@g++ src/philosophe.c -o philosophe $(CFLAGS)
	@echo "\n Successfully compiled philosophe.c. \n"

	@g++ src/producteurs-consomateur.c -o producteurs-consomateur $(OBJ) # $(CFLAGS)
