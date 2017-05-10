#!/usr/bin/env bash



DIR=$1
en_mod=$2/projdata/alpage2/hmartine/tools/en_lemma_petrov.turbomodel_svm_mira/en_train_lemma_petrov.conll.model
de_mod=$2/projdata/alpage2/hmartine/tools/de_lemma_petrov.turbomodel_svm_mira/de_train_lemma_petrov.conll.model
fr_mod=$2/projdata/alpage2/hmartine/tools/fr_lemma_petrov.turbomodel_svm_mira/fr_train_lemma_petrov.conll.model


bash parse_target_lemmapetrov.sh $DIR/TEDdev.de-en.data.filtered.withids $en_mod
bash parse_target_lemmapetrov.sh $DIR/TEDdev.en-de.data.filtered.withids $de_mod
bash parse_target_lemmapetrov.sh $DIR/TEDdev.en-fr.data.filtered.withids $fr_mod
bash parse_target_lemmapetrov.sh $DIR/TEDdev.es-en.data.withids $en_mod
bash parse_target_lemmapetrov.sh $DIR/TEDdev2.es-en.data.withids $en_mod


bash parse_target_lemmapetrov.sh $DIR/DiscoMT2017.de-en.test.data.filtered.final $en_mod
bash parse_target_lemmapetrov.sh $DIR/DiscoMT2017.en-de.test.data.filtered.final $de_mod
bash parse_target_lemmapetrov.sh $DIR/DiscoMT2017.en-fr.test.data.filtered.final $fr_mod
bash parse_target_lemmapetrov.sh $DIR/DiscoMT2017.es-en.test.data.filtered.final $en_mod

bash parse_target_lemmapetrov.sh $DIR/all.de-en.withids $en_mod
bash parse_target_lemmapetrov.sh $DIR/all.en-fr.withids $fr_mod
bash parse_target_lemmapetrov.sh $DIR/all.en-de.withids $de_mod
bash parse_target_lemmapetrov.sh $DIR/all.es-en.withids $en_mod


