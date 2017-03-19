#!/bin/bash --

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PWD=`pwd`

cd $DIR

for f in `find ./ -type f| grep -v jpg`;
do
    curl -o $f.jpg $(cat $f)
done

