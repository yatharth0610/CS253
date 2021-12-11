#!/bin/bash
(
data_file='covid_Data.json';
states=($(jq 'keys' $data_file));
states=("${states[@]:1:${#states[@]}-2}");
states=($(echo ${states[@]} | sed 's/,//g'));
csv_file='processed_Covid_Data_191178.csv';
echo "State,District,Confirmed_Cases,Recovery_Rate" >> $csv_file;

for state in ${states[@]};
do 
    max_rate=0;
    max_rate_district='';
    max_district_confirmed=0;
    valid=0;
    IFS=",";
    districts=($(jq ".$state.districts | keys" $data_file));
    tot=${#districts[@]};
    for (( i=0; i<$tot; i++ )); 
    do
        d=${districts[$i]};
        d=$(echo $d | grep -o '".*"');
        if [[ $d != '"Unknown"' && $(jq ".${state}.districts.${d}.total.confirmed|values" $data_file) -ge 5000 ]] 
        then  
            confirmed=$(jq ".${state}.districts.${d}.total.confirmed|values" $data_file);
            recovered=$(jq ".${state}.districts.${d}.total.recovered|values" $data_file);
            rate=$(echo "x=$recovered/$confirmed * 100 + 0.005; scale=2; x/1" | bc -l);
            if [[ $rate>=$max_rate ]] 
            then
                max_rate=$rate;
                max_district_confirmed=$confirmed;
                max_rate_district=$d;
                valid=1;
            fi
        fi
    done 
    if [[ $valid -eq 1 ]] 
    then
        echo "$state,$max_rate_district,$max_district_confirmed,$max_rate" >> $csv_file;
    fi
done 
) 2>error.txt;
