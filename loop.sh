#!/bin/bash


while read f; do 
   docker rmi -f $f   
   echo $f 'image is deleted'
done <dockerid.txt 
