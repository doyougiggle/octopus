for file in `ls *conllu`
do
cat $file |grep -v "^#"|egrep -v "\d+\-" > $file.cleaned
done
