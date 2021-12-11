#!/bin/bash

chmod 777 q1-cs253.tar.gz;
tar xvfz q1-cs253.tar.gz;
chmod 777 q1-cs253.zip Q1.pdf.gz;
gzip -d Q1.pdf.gz;
mkdir package_files;
unzip q1-cs253.zip -d package_files;
mv q1-cs253.zip package_files/
cd package_files;

lis=($(ls));
chmod 777 ${lis[0]} ${lis[1]};
gzip -d ${lis[0]} ${lis[1]};

other='';
if [[ ${lis[1]} == 'deploy.gz' ]] 
then
    other=${lis[0]};
else 
    other=${lis[1]};
fi
other=${other::-3};
package=$(bash $other | head -n 1 | cut -d " " -f 3);
echo $package;

dirs=($(ls -d */));
chmod 777 ${dirs[0]} ${dirs[1]};
chmod 777 deploy;

file1='';
file2='';

if [[ $(ls ${dirs[0]} | wc -l) == 1 ]] 
then
    file1=${dirs[0]};
    file2=${dirs[1]};
else 
    file1=${dirs[1]};
    file2=${dirs[0]};
fi

bash deploy $file1 $package $file2 191178 > ../submission-q1.txt

