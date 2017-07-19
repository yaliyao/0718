#!/bin/bash

fname="dht22sensor.sh.csv"
echo "datetime,temperature*,humidity%"

while true
do
    while true
    do
        temp=$(cat /sys/bus/iio/devices/iio\:device0/in_temp_input 2> /dev/null)
        if [[ $? -eq 0 ]]
        then
            break
        fi        
    done
    
    while true
    do
        hum=$(cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input 2> /dev/null)
        if [[ $? -eq 0 ]]
        then
            break
        fi        
    done

    dt=$(date +'%Y-%m-%d %H:%M:%S')
    temp=$(echo "scale=1; $temp/1000" | bc)
    hum=$(echo "scale=1; $hum/1000" | bc)

    # just output to screen
    echo "$dt,$temp,$hum"
    
    # output to screen and file
    #echo "$dt,$temp,$hum" | tee -a $fname

    sleep 10
done

