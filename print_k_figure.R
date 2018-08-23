library("ldatuning")
result <- read.table(file = 'k_value.tsv', sep = '\t', header = TRUE)
bitmap("plot.tiff", height = 12, width = 17, units = 'cm', 
       type = "tifflzw", res = 300)
FindTopicsNumber_plot(result)
dev.off
