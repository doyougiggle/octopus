#!/usr/bin/env bash



DIR=/projdata/alpage2/hmartine/data/discomt17/toparse/train/es-en
target_mod=/projdata/alpage2/hmartine/tools/en_lemma_petrov.turbomodel_svm_mira/en_train_lemma_petrov.conll.model
source_mod=/projdata/alpage2/hmartine/tools/de_form_upos.turbomodel_svm_mira/es_train_form_upos.conll.model
source_lang=es

for file in `ls $DIR/*withids`
do
bash parse_target_lemmapetrov.sh $file $target_mod
bash parse_source_formpos.sh $file $source_mod $source_lang
done
