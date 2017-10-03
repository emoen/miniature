pinus.df <- read.table("pinus.csv", header=T, dec=",", sep=";", na.string="NA")

#a)
head(pinus.df)

#b) cones depending on sub
p3 <- ggplot(data=pinus.df, aes(x=Sub, y=Cones))
p3 <- p3 + geom_point()
p3

#c) age depending on subspecies
p3 <- ggplot(data=pinus.df, aes(x=Sub, y=Age))
p3 <- p3 + geom_point()
p3

#d) subplots and e)
fit1.lm <- lm(Cones~Age, data=pinus.df)


p3 <- ggplot(data=pinus.df, aes(x=Cones, y=Age))
p3 <- p3 + facet_wrap(~Sub)
p3 <- p3 + geom_smooth(method="lm", formula = y~x)
p3 <- p3 + geom_point()
p3