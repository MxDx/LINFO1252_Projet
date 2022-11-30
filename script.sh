cd "Modest"

for n in  {1..7}
do 
    echo -n "$n threads;" >> test.csv
done
echo  "8 threads;" >> test.csv

for i in  1 2 3 4 5
do 
    for j in 1 2 3 4 5 6 7 8
    do
        make -i -s clean
        echo -n $(/usr/bin/time -f "%e" make -s -j $j 2>&1) >> test.csv 
        echo -n ";" >> test.csv   
    done
    echo "" >> test.csv
done