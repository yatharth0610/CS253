#!/bin/bash

echo "Do you want to perform checks on OS Command Injection as well?"
echo "Press 1 to check for it else press 0"
read overwrite

g++ mitigated.cpp -o a.out;

if [[ overwrite -eq 1 ]] 
then
    mkdir outputs_1; 
    for (( i=1; i <= 10; i=i+1 )) do
    (
    echo "1";
    echo "2";
    echo "1";
    in1=$(cat Test1.in | head -$i | tail -1);
    echo $in1;
    echo "2";
    echo "2";
    echo "1";
    in2=$(cat Test2.in | head -$i | tail -1);
    echo $in2;
    ) | ./a.out > outputs_1/out$i.txt;
    done;
else 
    mkdir outputs;
    for (( i=1; i <= 10; i=i+1 )) do
    (
    echo "0";
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
fi

rm a.out;
