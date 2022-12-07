nbthread=64
two=2

#Each test is done 5 times
#Each test is done with 1, 2, 4, 8, 16, 32, 64 threads
#Each hastag separates the different tests


#Philosophe

for n in 1 2 4 8 16 32 #Create a loop for each number of threads
do 
    echo -n "$n threads;" >> test_philosophe.csv
done
echo  "$nbthread threads;" >> test_philosophe.csv

for ((i=0;i<5;i++))
do 
    for j in 1 2 4 8 16 32 64
    do
        echo -n $(/usr/bin/time -f "%e" ./philosophe.exe $j 2>&1) >> test_philosophe.csv 
        echo -n ";" >> test_philosophe.csv   
    done
    echo "" >> test_philosophe.csv
done

cat test_philosophe.csv



#Philosophe AA

for n in 1 2 4 8 16 32
do 
    echo -n "$n threads;" >> test_philosophe_AA.csv
done
echo  "$nbthread threads;" >> test_philosophe_AA.csv

for ((i=0;i<5;i++))
do 
    for j in 1 2 4 8 16 32 64
    do
        echo -n $(/usr/bin/time -f "%e" ./philosophe_AA.exe $j 2>&1) >> test_philosophe_AA.csv 
        echo -n ";" >> test_philosophe_AA.csv   
    done
    echo "" >> test_philosophe_AA.csv
done

cat test_philosophe_AA.csv


#=============================================================================================================================================


#Producteur Consommateur

for n in 2 4 8 16 32
do 
    echo -n "$n threads;" >> test_producteurs_consommateur.csv
done
echo  "$nbthread threads;" >> test_producteurs_consommateur.csv

for ((i=0;i<5;i++))
do 
    for j in 2 4 8 16 32 64
    do
        #Create a variable prod wich equals to j / 2
        #Variable prod is the number of producers
        prod=$(($j / $two))
        #Create a variable cons wich equals to j - prod so that cons + prod = nbthread
        #Variable cons is the number of consumers
        cons=$(($j - $prod))
        echo -n $(/usr/bin/time -f "%e" ./producteurs-consomateur.exe $prod $cons 2>&1) >> test_producteurs_consommateur.csv 
        echo -n ";" >> test_producteurs_consommateur.csv   
    done
    echo "" >> test_producteurs_consommateur.csv
done

cat test_producteurs_consommateur.csv



#Producteur Consommateur AA

for n in 2 4 8 16 32
do 
    echo -n "$n threads;" >> test_producteurs_consommateur_AA.csv
done
echo  "$nbthread threads;" >> test_producteurs_consommateur_AA.csv

for ((i=0;i<5;i++))
do 
    for j in 2 4 8 16 32 64
    do
        #Create a variable prod wich equals to j / 2
        #Variable prod is the number of producers
        prod=$(($j / $two))
        #Create a variable cons wich equals to j - prod so that cons + prod = nbthread
        #Variable cons is the number of consumers
        cons=$(($j - $prod))
        echo -n $(/usr/bin/time -f "%e" ./producteurs-consomateur_AA.exe $prod $cons 2>&1) >> test_producteurs_consommateur_AA.csv 
        echo -n ";" >> test_producteurs_consommateur_AA.csv   
    done
    echo "" >> test_producteurs_consommateur_AA.csv
done

cat test_producteurs_consommateur_AA.csv


#=============================================================================================================================================


#Lecteurs Ecrivains

for n in 2 4 8 16 32
do 
    echo -n "$n threads;" >> test_lecteurs-Ecrivains.csv
done
echo  "$nbthread threads;" >> test_lecteurs-Ecrivains.csv

for ((i=0;i<5;i++))
do 
    for j in 2 4 8 16 32 64
    do
        #Create a variable prod wich equals to j / 2
        #Variable prod is the number of producers
        #Create a variable cons wich equals to j - prod so that cons + prod = nbthread
        #Variable cons is the number of consumers
        Ecrivains=$(($j / $two))
        Lecteurs=$(($j - $Ecrivains))
        echo -n $(/usr/bin/time -f "%e" ./lecteurs-ecrivains.exe $Lecteurs $Ecrivains 2>&1) >> test_lecteurs-Ecrivains.csv 
        echo -n ";" >> test_lecteurs-Ecrivains.csv   
    done
    echo "" >> test_lecteurs-Ecrivains.csv
done

cat test_lecteurs-Ecrivains.csv



#Lecteurs Ecrivains AA

for n in 2 4 8 16 32
do 
    echo -n "$n threads;" >> test_lecteurs-Ecrivains_AA.csv
done
echo  "$nbthread threads;" >> test_lecteurs-Ecrivains_AA.csv

for ((i=0;i<5;i++))
do 
    for j in 2 4 8 16 32 64
    do
        #Create a variable prod wich equals to j / 2
        #Variable prod is the number of producers
        #Create a variable cons wich equals to j - prod so that cons + prod = nbthread
        #Variable cons is the number of consumers
        Ecrivains=$(($j / $two))
        Lecteurs=$(($j - $Ecrivains))
        echo -n $(/usr/bin/time -f "%e" ./lecteurs-ecrivains_AA.exe $Lecteurs $Ecrivains 2>&1) >> test_lecteurs-Ecrivains_AA.csv 
        echo -n ";" >> test_lecteurs-Ecrivains_AA.csv   
    done
    echo "" >> test_lecteurs-Ecrivains_AA.csv
done

cat test_lecteurs-Ecrivains_AA.csv


#================================================================================================================================================



#TAS

for n in 1 2 4 8 16 32
do 
    echo -n "$n threads;" >> test_tas.csv
done
echo  "$nbthread threads;" >> test_tas.csv

for ((i=0;i<5;i++))
do 
    for j in 1 2 4 8 16 32 64
    do
        echo -n $(/usr/bin/time -f "%e" ./test_tas.exe $j 2>&1) >> test_tas.csv 
        echo -n ";" >> test_tas.csv   
    done
    echo "" >> test_tas.csv
done

cat test_tas.csv

#TATAS

for n in 1 2 4 8 16 32
do 
    echo -n "$n threads;" >> test_tatas.csv
done
echo  "$nbthread threads;" >> test_tatas.csv

for ((i=0;i<5;i++))
do 
    for j in 1 2 4 8 16 32 64
    do
        echo -n $(/usr/bin/time -f "%e" ./test_tatas.exe $j 2>&1) >> test_tatas.csv 
        echo -n ";" >> test_tatas.csv   
    done
    echo "" >> test_tatas.csv
done

cat test_tatas.csv

#BTATAS

for n in 1 2 4 8 16 32
do 
    echo -n "$n threads;" >> test_btatas.csv
done
echo  "$nbthread threads;" >> test_btatas.csv

for ((i=0;i<5;i++))
do 
    for j in 1 2 4 8 16 32 64
    do
        echo -n $(/usr/bin/time -f "%e" ./test_btatas.exe $j 2>&1) >> test_btatas.csv 
        echo -n ";" >> test_btatas.csv   
    done
    echo "" >> test_btatas.csv
done

cat test_btatas.csv

