make > out.log 2> err.log

for n in  {1..7}
do 
    echo -n "$n threads;" >> test_philosophe.csv
done
echo  "8 threads;" >> test_philosophe.csv

for i in  1 2 3 4 5
do 
    for j in 1 2 3 4 5 6 7 8
    do
        echo -n $(/usr/bin/time -f "%e" ./philosophe.exe $j 2>&1) >> test_philosophe.csv 
        echo -n ";" >> test_philosophe.csv   
    done
    echo "" >> test_philosophe.csv
done