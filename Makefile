CC=gcc
CFLAGS= -Wall -Werror -g 
LIBS= -lpthread -lm
INCLUDE_HEADERS_DIRECTORY=-Iheaders
SRC=src/*.c
OBJ=stack.o

main:
	@make clean
	@$(CC) -c $(SRC) $(LIBS) #$(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@$(CC) -o philosophe.exe philosophe.o $(CFLAGS) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled philosophe.c. \n"

	@$(CC) -o producteurs-consomateur.exe $(OBJ) producteurs-consomateur.o $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled producteurs-consomateur.c. \n"

	@$(CC) -o lecteurs-ecrivains.exe lecteurs-ecrivains.o $(CFLAGS) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled lecteurs-ecrivains.c. \n"

clean:
	@rm -f *.o
	@rm -f *.exe
	@rm -f *.log
	@rm -f *.csv
	@rm -f *.zip
	@echo "\n Successfully cleaned all files. \n"

test:
	@bash experiments.sh

debug: 
	@make clean
	@g++ -g -c $(SRC) $(LIBS) #$(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@g++ -g -o philosophe.exe philosophe.o $(CFLAGS)
	@echo "\n Successfully compiled philosophe.c (DEBUG). \n"

	@g++ -g -o producteurs-consomateur.exe $(OBJ) producteurs-consomateur.o
	@echo "\n Successfully compiled producteurs-consomateur.c (DEBUG). \n"

zip:
	@make clean
	@cd ..
	@zip -r project.zip ./*
	@echo "\n Successfully zipped the project. \n"
