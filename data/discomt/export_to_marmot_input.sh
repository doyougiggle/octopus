for file in `ls *cleaned`
do
cat $file |cut -f1,2,4 > $file.marmot
done
