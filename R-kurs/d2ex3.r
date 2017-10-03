tcb.df <- read.table("tcb.csv", header=T, dec=",", sep=";", na.string="NA")
str(tcb.df)

#b)
p1 <- ggplot(data=tcb.df, aes(x=Site, y=CFU))
p1 <- p1 + geom_point()
p1

# c)
#H0: The amount of TCB in Møllendal river is the same above and below pipeline A

#wrong
tcb.lm = lm(CFU~Site, data=tcb.df)

anova(tcb.lm)
summary(tcb.lm)
# untrue: P = 2.2e-16

# USE:
fit3.glm <- glm(CFU~Site, family="quasipoisson", data=tcb.df)
anova(fit3.glm, test="F")
#Note! tested with quasipoisson and F-test in case of overdispersion.
summary(fit3.glm)


