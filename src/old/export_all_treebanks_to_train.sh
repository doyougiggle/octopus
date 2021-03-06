% export to the right format to train with turboparser
% form.upos and lemma.petrov


BASE=/Users/hmartine/proj/octopus/data/discomt

for lang in  en es fr de
do
    for section in dev train
    do
        FILENAME=$BASE/$lang-ud-$section.conllu
        python udcleaned2turboparser.py --infile $FILENAME --wordmode form --posmode upos |cat -s > "$lang"_"$section"_form_upos.conll
        python udcleaned2turboparser.py --infile $FILENAME --wordmode lemma --posmode petrov |cat -s > "$lang"_"$section"_lemma_petrov.conll
    done
done