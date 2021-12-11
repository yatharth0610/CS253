#!/bin/bash

lis=($(ls));
file1=${lis[0]};
file2=${lis[1]};
file3=${lis[2]};

bash $file1 < test1 &
bash $file2 < test2 &
bash $file3 < test3 &

