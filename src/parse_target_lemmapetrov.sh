#!/usr/bin/env bash
file=$1
model=$2

python discodata_target_2turboparser.py --infile $file > $file.tmp
cd /projdata/alpage2/hmartine/tools
bash parse_with_turboparser.sh $file.tgt $model
cd -
python parsed_to_inline_notation.py --infile $file.tgt.parsed > $file.tgt.inline
rm $file.tgt