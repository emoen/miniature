tcb.df <- read.table("TCB.csv", header=T, dec=",", sep=";", na.string="NA")
str(tbc.df)

#b)
p4 <- ggplot(data=tcb.df, aes(x=Site, y=CFU))
p4 <- p4 + geom_smooth(method="lm", formula = y~x)
p4 <- p4 + geom_point()
p4