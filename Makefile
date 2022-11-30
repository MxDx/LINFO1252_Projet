CC=gcc
CFLAGS= -Wall -Werror -g 
LIBS=-lcunit -lpthread -lm
INCLUDE_HEADERS_DIRECTORY=-Iheaders
SRC=src/stack.c src/producteurs-consomateur.c src/philosophe.c
OBJ=stack.o

main:
	@make clean
	@$(CC) -c $(SRC) #$(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@$(CC) -o philosophe.exe philosophe.o $(CFLAGS)
	@echo "\n Successfully compiled philosophe.c. \n"

	@$(CC) -o producteurs-consomateur.exe $(OBJ) producteurs-consomateur.o
	@echo "\n Successfully compiled producteurs-consomateur.c. \n"

clean:
	@rm -f *.o
	@rm -f *.exe

debug: 
	@make clean
	@g++ -g -c $(SRC) #$(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@g++ -g -o philosophe.exe philosophe.o $(CFLAGS)
	@echo "\n Successfully compiled philosophe.c (DEBUG). \n"

	@g++ -g -o producteurs-consomateur.exe $(OBJ) producteurs-consomateur.o
	@echo "\n Successfully compiled producteurs-consomateur.c (DEBUG). \n"
