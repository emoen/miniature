# rats.xls
rats.df <- read.table("rats.csv", header=T, dec=",", sep=";", na.string="NA")
str(rats.df)

# b) plot
p1 <- ggplot(data=rats.df, aes(x=Sex, y=Body.mass))
p1 <- p1 + geom_boxplot()
p1

# c) H0: bodymass is same regardless Sex
#fit1.lm <- lm(Body.mass~Sex, data=rats.df)
#summary(fit1.lm)
# P value for H0: 2.83e-11

t.test(Body.mass~Sex, data=rats.df) # p-value = 2.512e-05