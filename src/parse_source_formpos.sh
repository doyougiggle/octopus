#!/usr/bin/env bash
file=$1
model=$2
lang=$3

python discodata_source_2marmot.py --infile $file --outfile  $file.src  #> $file.src
cd /projdata/alpage2/hmartine/tools/marmot
bash tag_with_marmot.sh  $lang $file.src
cd -
python marmot2turboparser.py --infile $file.src.pos --outfile  $file.src2
cd /projdata/alpage2/hmartine/tools
bash parse_with_turboparser.sh $file.src2 $model
cd -
python parsed_to_inline_notation.py --infile $file.src2.parsed --outfile $file.src.inline
rm $file.src
rm $file.src2