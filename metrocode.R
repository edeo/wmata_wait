library(jsonlite)

Sys.time()


metrodata <- data.frame()
i <- 1

while (i < 100) {
  print(i)
  i = i+1
  newdata <- fromJSON("https://api.wmata.com/StationPrediction.svc/json/GetPrediction/ALL?api_key=bce6ec600e2342f28bc7751435ac0f52")
  x <-newdata$Trains
  x$time <- Sys.time()
  x <- x[which( x$Min == 'BRD'| x$Min == 'ARR'), ]
  metrodata <- rbind(metrodata, x)
  Sys.sleep(2)
}

result <- metrodata[order(metrodata$LocationCode, metrodata$Line,metrodata$Group,metrodata$time),]

for i in range(len(data)):
  item = data[i]
before = i-1
prior = data[before]
data[i].append(item[8]==prior[8])

for i in range(length(x)) :
    item = data[i]
    before = i-1
    prior = data[before]
    data[i].append(item[8]==prior[8])

rdf <-(1:nrow(df))

data$newcolumn <- 0

for (i in 1:nrow(data)) {
  n <- power.prop.test( p1 = data[i,5], p2 = data[i,6], sig.level=.1, power = .8, alternative = "one.sided")
  data$newcolumn[i] <- n
}
head(data)

df$check <-0
  
for (number in rdf){x <- df[number,9]==df[number-1,9]}

for (number in rdf){print(number-1)}

x$`1`[10]==x$`2`[10]

dlply(df,.(id),c)
xy.list <- split(df, seq(nrow(df)))

