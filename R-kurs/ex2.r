#http://www.folk.uib.no/nzlkj/IMRkurs/exercises/day1/stopping.distance.xls
stop.distance <- read.table("stopping.distance.csv", header=T, dec=",", sep=";", na.string="NA")

#b
str(stop.distance)

#c
p1 <- ggplot(data=stop.distance, aes(x=Speed, y=Stop.distance))
p1 <- p1 + geom_point()
p1

#d)
# se=F - slå av konfedence interval - Standard Error
fit1.lm <- lm(Stop.distance~Speed, data=stop.distance, se=F)
p1 <- p1 + geom_smooth(method="lm", formula = y~x)
p1