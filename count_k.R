library("tm")
library("ldatuning")
docs <- Corpus(DirSource("/PATH/corpus/Finnish"))
dtm <- DocumentTermMatrix(docs)
result <- FindTopicsNumber(
  dtm,
  topics = c(2,3,4,5,6,7,8,9,10,11,12,13,14,15),
  metrics = c("Griffiths2004", "CaoJuan2009", "Arun2010", "Deveaud2014"),
  method = "Gibbs",
  control = list(seed = 77),
  mc.cores = 2L,
  verbose = TRUE
)
save(result,file="/PATH/k_value.Rda")
write.table(result, "/PATH/k_value.tsv", sep="\t")
