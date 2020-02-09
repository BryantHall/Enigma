#getwd()

#read in data
dataF = read.csv("SamplesFreq.csv")
head(dataF)

#parse out spaces and nulls
#dataF = dataF[dataF != " "]
dataF = dataF[dataF != ""]
dataF = data.frame(dataF)
###
plot = with(dataF, table(dataF))
barplot(plot, col=rainbow(25))
###

write.csv(dataF,"dataF.csv")

total = c(ï..Sample2, Sample1)
plot = with(dataF, table(ï..Sample2))
barplot(plot, col=rainbow(2))

#look at data
sample1 = with(dataF, dataF[ï..Sample == "S1",])
sample1

sample2 = with(dataF, dataF[ï..Sample == "S2",])
sample2


#sample1 = dataF[1:4,2:51]
#sample1

#test barplot
plot = with(dataF, table(ï..SampleS1))
barplot(plot, col=rainbow(2))

plot = with(dataF, table(LineNumber))
barplot(plot, col=rainbow(5))

#horizontal barplot
plot = with(dataF, table("S1", 3:51))
barplot(plot)

s = c(dataF[1:4,3:51])
#barplot(s)
barplot(s,names.arg = s)