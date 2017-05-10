#!/usr/bin/env bash
DIR=$1
en_mod=/projdata/alpage2/hmartine/tools/en_form_upos.turbomodel_svm_mira/en_train_form_upos.conll.model
de_mod=/projdata/alpage2/hmartine/tools/de_form_upos.turbomodel_svm_mira/de_train_form_upos.conll.model
fr_mod=/projdata/alpage2/hmartine/tools/fr_form_upos.turbomodel_svm_mira/fr_train_form_upos.conll.model
es_mod=/projdata/alpage2/hmartine/tools/es_form_upos.turbomodel_svm_mira/es_train_form_upos.conll.model

bash parse_source_formpos.sh $DIR/TEDdev.de-en.data.filtered.withids $de_mod de
bash parse_source_formpos.sh $DIR/TEDdev.en-de.data.filtered.withids $en_mod en
bash parse_source_formpos.sh $DIR/TEDdev.en-fr.data.filtered.withids $en_mod en
bash parse_source_formpos.sh $DIR/TEDdev.es-en.data.withids $es_mod es
bash parse_source_formpos.sh $DIR/TEDdev2.es-en.data.withids $es_mod es

bash parse_source_formpos.sh $DIR/DiscoMT2017.de-en.test.data.filtered.final $de_mod ed
bash parse_source_formpos.sh $DIR/DiscoMT2017.en-de.test.data.filtered.final $en_mod en
bash parse_source_formpos.sh $DIR/DiscoMT2017.en-fr.test.data.filtered.final $en_mod en
bash parse_source_formpos.sh $DIR/DiscoMT2017.es-en.test.data.filtered.final $es_mod es

bash parse_source_formpos.sh $DIR/all.de-en.withids $de_mod de
bash parse_source_formpos.sh $DIR/all.en-fr.withids $en_mod en
bash parse_source_formpos.sh $DIR/all.en-de.withids $en_mod en
bash parse_source_formpos.sh $DIR/all.es-en.withids $fr_mod fr

