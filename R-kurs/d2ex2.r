# a)
solving.df <- read.table("solving.time.csv", header=T, dec=",", sep=";", na.string="NA")
str(solving.df)

# b)
p1 <- ggplot(data=solving.df, aes(x=Player, y=Time))
p1 <- p1 + geom_boxplot()
p1

# c) H0: The time spent solving a mathematical problem is the same for professional chess, squash and tennis players
fit1.lm <- lm(Time~Player, data=solving.df)
anova(fit1.lm)
summary(fit1.lm)
library(multcomp)

#Performing a Tukey HSD multiple comarisons test:
mc <- glht(fit.lm, linfct = mcp(Player="Tukey"), data=solvtime.df)
summary(mc)
#squash - chess == 0   11.6000 P <1e-05
#tennis - chess == 0   11.3967 P <1e-05
#tennis - squash == 0  -0.2033 P  0.987 

# d)
solving.subset.df = subset(solving.df, Player=='tennis' | Player=='chess')
p1 <- ggplot(data=solving.subset.df, aes(x=Player, y=Time))
p1 <- p1 + geom_boxplot()
p1

# WRONG
#fit1.lm <- lm(Time~Player, data=solving.subset.df)
#anova(fit1.lm)
#summary(fit1.lm)
t.test(Time~Player, data=solving.subset.df)
