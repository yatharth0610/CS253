#!/bin/bash

lis=($(ls));
file1=${lis[0]};
file2=${lis[1]};
file3=${lis[2]};

proc1=($(ps -f | grep "bash ${file1}"));
proc2=($(ps -f | grep "bash ${file2}"));
proc3=($(ps -f | grep "bash ${file3}"));

proc4=($(ps -f --ppid ${proc1[1]}));
proc5=($(ps -f --ppid ${proc2[1]}));
proc6=($(ps -f --ppid ${proc3[1]}));

proc7=($(ps -f --ppid ${proc4[9]}));
proc8=($(ps -f --ppid ${proc5[9]}));
proc9=($(ps -f --ppid ${proc6[9]}));

proc10=($(ps -f --ppid ${proc7[9]}));
proc11=($(ps -f --ppid ${proc8[9]}));
proc12=($(ps -f --ppid ${proc9[9]}));

kill -9 ${proc1[1]};
kill -9 ${proc2[1]};
kill -9 ${proc3[1]};
kill -9 ${proc4[9]};
kill -9 ${proc5[9]};
kill -9 ${proc6[9]};
kill -9 ${proc7[9]};
kill -9 ${proc8[9]};
kill -9 ${proc9[9]};
kill -9 ${proc10[9]};
kill -9 ${proc11[9]};
kill -9 ${proc12[9]};

