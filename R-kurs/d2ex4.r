oc.df <- read.table("occurrence.csv", header=T, dec=",", sep=";", na.string="NA")
str(tcb.df)

# b)
p1 <- ggplot(data=oc.df, aes(x=Temp, y=Occurrence))
p1 <- p1 + geom_jitter(height=0.01)
p1 <- p1 + geom_smooth(method = "glm", method.args = list(family = "binomial"), formula = y~x)
p1

# c) 
#H0: The occurrence of blue tit nests does not depend on summer mean temperature.
oc.glm <- glm(Occurrence~Temp, family="binomial", data=oc.df)
anova(oc.glm, test="Chi")
#Note! tested with quasipoisson and F-test in case of overdispersion.
summary(oc.glm)