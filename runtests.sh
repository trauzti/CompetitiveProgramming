#!/bin/sh 

for f in $(ls tests/*.py)
do 
    if [[ $(basename $f) != "__init__.py" ]]
    then
        PYTHONPATH=$(pwd) python $f
    fi
done
