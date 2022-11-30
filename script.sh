nbthread=3
two=2

make > out.log 2> err.log


#Philosophe
for ((n=1;n<$nbthread;n++))
do 
    echo -n "$n threads;" >> test_philosophe.csv
done
echo  "$nbthread threads;" >> test_philosophe.csv

for ((i=0;i<5;i++))
do 
    for ((j=1;j<=$nbthread;j++))
    do
        echo -n $(/usr/bin/time -f "%e" ./philosophe.exe $j 2>&1) >> test_philosophe.csv 
        echo -n ";" >> test_philosophe.csv   
    done
    echo "" >> test_philosophe.csv
done

#Producteur Consommateur
for ((n=2;n<$nbthread;n++))
do 
    echo -n "$n threads;" >> test_producteurs_consommateur.csv
done
echo  "$nbthread threads;" >> test_producteurs_consommateur.csv

for ((i=0;i<5;i++))
do 
    for ((j=1; j<=$nbthread; j++))
    do
        #Create a variable prod wich equals to j / 2
        prod=$(($j / $two))
        #Create a variable cons wich equals to j - prod
        cons=$(($j - $prod))
        echo -n $(/usr/bin/time -f "%e" ./producteurs-consomateur.exe $prod $cons 2>&1) >> test_producteurs_consommateur.csv 
        echo -n ";" >> test_producteurs_consommateur.csv   
    done
    echo "" >> test_producteurs_consommateur.csv
done

#Lecteurs Ecrivains
for ((n=2;n<$nbthread;n++))
do 
    echo -n "$n threads;" >> test_lecteurs-Ecrivains.csv
done
echo  "$nbthread threads;" >> test_lecteurs-Ecrivains.csv

for ((i=0;i<5;i++))
do 
    for ((j=2; j<=$nbthread; j++))
    do
        Ecrivains=$(($j / $two))
        Lecteurs=$(($j - $prod))
        echo -n $(/usr/bin/time -f "%e" ./lecteurs-ecrivains.exe $Lecteurs $Ecrivains 2>&1) >> test_lecteurs-Ecrivains.csv 
        echo -n ";" >> test_lecteurs-Ecrivains.csv   
    done
    echo "" >> test_lecteurs-Ecrivains.csv
done