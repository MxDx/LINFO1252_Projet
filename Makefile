CC=gcc
CFLAGS= -Wall -Werror -g 
LIBS= -lpthread -lm
INCLUDE_HEADERS_DIRECTORY=-Iheaders
SRC=src/*.c src/attente_active/*.c src/Posix/*.c
TST=test/*.c
TAS=attente_active/*.c
OBJ=stack.o 
AA=test-and-test-and-set.o semaphore.o

main:
	@make clean
	@$(CC) -c $(SRC) $(LIBS) #$(CFLAGS)
	@$(CC) -c $(TST) $(LIBS) #$(CFLAGS)
	@$(CC) -c $(TAS) $(LIBS) #$(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@$(CC) -o philosophe.exe philosophe.o $(CFLAGS) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled philosophe.c. \n"

	@$(CC) -o philosophe_AA.exe philosophe_AA.o $(AA) $(CFLAGS) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled philosophe_AA.c. \n"

	@$(CC) -o producteurs-consomateur.exe $(OBJ) producteurs-consomateur.o $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled producteurs-consomateur.c. \n"

	@$(CC) -o producteurs-consomateur_AA.exe $(OBJ) producteurs-consomateur_AA.o $(AA) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled producteurs-consomateur_AA.c. \n"

	@$(CC) -o lecteurs-ecrivains.exe lecteurs-ecrivains.o $(CFLAGS) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled lecteurs-ecrivains.c. \n"

	@$(CC) -o lecteurs-ecrivains_AA.exe lecteurs-ecrivains_AA.o $(AA) $(CFLAGS) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled lecteurs-ecrivains_AA.c. \n"

	@$(CC) -o test_tas.exe test_tas.o test-and-set.o $(CFLAGS) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled test_tas.c. \n"

	@$(CC) -o test_tatas.exe test_tatas.o test-and-test-and-set.o $(CFLAGS) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled test_tatas.c. \n"

	@$(CC) -o test_btatas.exe test_btatas.o backoff-test-and-test-and-set.o $(CFLAGS) $(LIBS) $(INCLUDE_HEADERS_DIRECTORY)
	@echo "\n Successfully compiled test_btatas.c. \n"


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
	@g++ -g -c $(TST) $(LIBS) #$(CFLAGS)
	@g++ -g -c $(TAS) $(LIBS) #$(CFLAGS)
	@echo "\n Successfully compiled all source files. \n" 
	
	@g++ -g -o philosophe.exe philosophe.o $(CFLAGS)
	@echo "\n Successfully compiled philosophe.c (DEBUG). \n"

	@g++ -g -o producteurs-consomateur.exe $(OBJ) producteurs-consomateur.o
	@echo "\n Successfully compiled producteurs-consomateur.c (DEBUG). \n"

	@g++ -g -o producteurs-consomateur_AA.exe $(OBJ) producteurs-consomateur_AA.o $(AA) 
	@echo "\n Successfully compiled producteurs-consomateur_AA.c (DEBUG). \n"

	@g++ -g -o test_semaphore.exe $(OBJ) test_semaphore.o $(AA) 
	@echo "\n Successfully compiled test_semaphore.c (DEBUG). \n"

zip:
	@make clean
	@cd ..
	@zip -r project.zip ./*
	@echo "\n Successfully zipped the project. \n"
