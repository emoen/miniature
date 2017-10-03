rats.df <- read.table("rats.txt", header=T) #header - variables has header names - True

#sep="" - space, sep="\t" - tab, sep="," - comma, sep=";"
rats.df <- read.table("rats.txt", header=T, dec=".", sep";", na.string="NA")

rats.df <- read.table(header=T, text="
Sex Body.mass
female 240.62
female 235.55
female 249.91
female 258.42
female 272.92
male 361.29
male 353.17
male 347.15
male 353.11
male 347.75")

#after import
str(rats.df)
head(rats.df)
tail(rats.df)

View(rats.df)
plot(Body.mass~Sex, data=rats.df)

rats.lm <- lm(Body.mass~Sex, data=rats.df)

##in ggplot
library(ggplot2)
#aes - estetics
p1 <- ggplot(data=rats.df, aes(x=Sex, y=Body.mass))
p1 <- p1 + geom_boxplot()
p1

summary(rats.lm)

p1 <- ggplot(demo.df, aes(Speed, Stop.distance))
p1 <- p1 + geom_point()
p1 <- p1 + theme_gray(base_size=24)
p1 <- p1 + labs(x="body mass", y="Sex")
p1
p1 <- p1 + geom_smooth(method="lm", formula = y~x)
p1