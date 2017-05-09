#!/usr/bin/env bash
file=$1
model=$2

python discodata_target_2turboparser.py --infile $file > $file.tmp
cd /projdata/alpage2/hmartine/tools
bash parse_with_turboparser.sh $file.tmp $model
cd -
python parsed_to_inline_notation.py $file.tmp > $file.parsed
rm $file.tmp