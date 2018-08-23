/PATH/mallet/bin/mallet import-dir --input corpus/$1 --output $1.mallet --keep-sequence --stoplist-file stoplist.txt
/PATH/mallet/bin/mallet train-topics --input $1.mallet --num-topics 5 --optimize-interval 10 --output-state $1.gz --output-topic-keys $1_topics.txt --output-doc-topics $1_composition.txt
