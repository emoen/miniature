demo.df <- read.table("http://folk.uib.no/nzlkj/bio300b/stop.txt", header=T)

library(ggplot2)
p1 <- ggplot(demo.df, aes(Speed, Stop.distance))
p1 <- p1 + geom_point()
p1 <- p1 + theme_gray(base_size=24)
p1 <- p1 + labs(x="Speed (km/h)", y="Stopping distance (m)")
p1

fit1.lm <- lm(Stop.distance~Speed, data=demo.df)

summary(fit1.lm)

p1 <- p1 + geom_smooth(method="lm", formula = y~x)
p1