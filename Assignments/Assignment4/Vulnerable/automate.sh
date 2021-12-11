#!/bin/bash

g++ get_secret.cpp -o a.out;
mkdir outputs;
for (( i=1; i <= 10; i=i+1 )) do
(
echo "2";
echo "1";
in1=$(cat Test1.in | head -$i | tail -1);
echo $in1;
echo "2";
echo "2";
echo "1";
in2=$(cat Test2.in | head -$i | tail -1);
echo $in2;
) | ./a.out > outputs/out$i.txt;
done;

rm a.out;
