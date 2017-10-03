#Start the exercises by setting the working directory for today's session: #
############################################################################
setwd("/home/nzlkj/work/kurs/2017/Innfoeringskurs i R for IMR/exercises/day2")


##############
# Exercise 1 #
##############

#a) Import
rats.df <- read.table("rats.csv", header=T, sep=",", dec=".")
str(rats.df)


#b) Plot
library(ggplot2)
p1 <- ggplot(rats.df, aes(x=Sex, y=Body.mass))
p1 <- p1 + geom_boxplot()
p1 <- p1 + theme_bw(base_size=20)
p1 <- p1 + labs(x="Sex", y="Body mass (g)")
p1

#c) Analysis
t.test(Body.mass~Sex, data=rats.df)



##############
# Exercise 2 #
##############

#a) Import
solving.time.df <- read.table("solving.time.csv", header=T, sep=",", dec=".")
str(solving.time.df)

#b) Plot
p2 <- ggplot(solving.time.df, aes(x=Player, y=Time))
p2 <- p2 + geom_boxplot()
p2 <- p2 + theme_bw(base_size=20)
p2 <- p2 + labs(x="Type of player", y="Time spent (s)")
p2

#c) Analysis
fit2.lm <- lm(Time~Player, data=solving.time.df)
anova(fit2.lm)
summary(fit2.lm)

#Unplanned multiple comparisons post hoc test:
library(multcomp)
mc <- glht(fit2.lm, linfct = mcp(Player="Tukey"), data=solving.time.df)
summary(mc)

#d) Subsetting followed by new plot and analysis
#Creating a new dataset without the squash players by using the subset function
solvtime.df <- subset(solving.time.df, Player!="squash")

#New plot with the new dataset
p2b <- ggplot(solvtime.df, aes(x=Player, y=Time))
p2b <- p2b + geom_boxplot()
p2b <- p2b + theme_bw(base_size=20)
p2b <- p2b + labs(x="Type of player", y="Time spent (s)")
p2b

#New analysis:
t.test(Time~Player, data=solvtime.df)


##############
# Exercise 3 #
##############

#a) Import
tcb.df <- read.table("TCB.csv", header=T, sep=",", dec=".")
str(tcb.df)


#b) Plot
p3 <- ggplot(tcb.df, aes(x=Site, y=CFU))
p3 <- p3 + geom_boxplot()
p3 <- p3 + theme_bw(base_size=20)
p3 <- p3 + labs(x="Location", y="CFU per ml")
p3


#c) Analysis 
fit3.glm <- glm(CFU~Site, family="quasipoisson", data=tcb.df)
anova(fit3.glm, test="F")
#Note! tested with quasipoisson and F-test in case of overdispersion.
summary(fit3.glm)
 


##############
# Exercise 4 #
##############

#a) Import
bluetits.df <- read.table("occurrence.csv", header=T, sep=",", dec=".")
str(bluetits.df)

#b) Plot
library(ggplot2)
p4 <- ggplot(bluetits.df, aes(x=Temp, y=Occurrence))
p4 <- p4 + geom_jitter(height=0.01)
p4 <- p4 + theme_bw(base_size=20)
p4 <- p4 + labs(x="Temperature (\u2103)", y="Occurrence") #The \u2103 is the unicode for degree celsius
p4 <- p4 + geom_smooth(method = "glm", method.args = list(family = "binomial"), formula = y~x)
p4

#c) Analysis 
fit4.glm <- glm(Occurrence~Temp, family="binomial", data=bluetits.df)
anova(fit4.glm, test="Chi")
summary(fit4.glm)



##############
# Exercise 5 #
##############

bplot <- function(dataset, response, predictor)
{
library(ggplot2)
p1 <- ggplot(data=dataset, aes(x=predictor, y=response))
p1 <- p1 + geom_boxplot()
p1 <- p1 + labs(x=deparse(substitute(predictor)), y=deparse(substitute(response)))
#Note! The "deparse(substitute" arguments is to let R change the variables in
#question to be set as a text string. If you just write x=pedictor and
#y=response, the whole content of the variables will be used as axis titles.
p1 <- p1 + theme_bw(base_size=20)
return(p1)
}

