CC=gcc
CFLAGS= -Wall -Werror -g 
LIBS=-lcunit -lpthread -lm
INCLUDE_HEADERS_DIRECTORY=-Iheaders
SRC=src/stack.c src/producteurs-consomateur.c src/philosophe.c
OBJ=stack.o
LIB_PATH=-L /bin

main:
	@$(CC) -c $(SRC) #$(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@$(CC) philosophe.o -o philosophe.exe $(CFLAGS)
	@echo "\n Successfully compiled philosophe.c. \n"

	@$(CC) producteurs-consomateur.o -o producteurs-consomateur.exe $(OBJ) 
	@echo "\n Successfully compiled producteurs-consomateur.c. \n"

clean:
	@rm -f *.o
	@rm -f *.exe

debug: 
	@g++ -c $(SRC) #$(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@g++ -o philosophe.exe philosophe.o $(CFLAGS)
	@echo "\n Successfully compiled philosophe.c (DEBUG). \n"

	@g++ -o producteurs-consomateur.exe $(OBJ) producteurs-consomateur.o
	@echo "\n Successfully compiled producteurs-consomateur.c (DEBUG). \n"
