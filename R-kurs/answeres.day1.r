# url: http://folk.uib.no/nzlkj/IMRkurs/exercises/day1/answers.day1.r
##############
# Exercise 1 #
##############

#a) R as a calculator, simple addition and subtraction
######################################################
2+4
6-4

#b) R as a calculator, finding the area and volume of a sphere
###############################################################

#Area:
4*pi*15^2

#Volume:
4/3*pi*15^3

#c) Dealing with objects and functions
#######################################
a <- c(2,4,6)
b <- c(2.4, 2.7, 3.5)
c <- c("s", "e", "g")
a
b
c

x <- c(2,5,8,10,2,6,8)
y <- c(1:7)
x
y

length(x)
summary(x)
sum(y)

z<-c(x,y)
z

mean(z)
median(z)
var(z)
hist(z)

##############
# Exercise 2 #
##############

#a) Import of data
###################
setwd("/home/nzlkj/work/kurs/2017/Innfoeringskurs i R for IMR/exercises/day1")

stop.df <- read.table("stopping.distance.csv", header=T, sep=",", dec=".")

#b) Having a look at structure of the dataset
#############################################
str(stop.df)

#c) Plot for the relationship between speed and stopping distance
#################################################################
library(ggplot2)
p1 <- ggplot(stop.df, aes(x=Speed, y=Stop.distance))
p1 <- p1 + geom_point()
p1 <- p1 + theme_bw(base_size=20)
p1 <- p1 + labs(x="Speed (km/h)", y="Stopping distance (m)")
p1

#d) Add regression line with 95% conf. int.
p1 <- p1 + geom_smooth(method=lm, formula=y~x)
p1



##############
# Exercise 3 #
##############

#a) Import of data and check imported dataset
#############################################
pinus.df <- read.table("pinus.csv", header=T, sep=",", dec=".")
head(pinus.df)

#b) Plot of number of cones depending on subspecies
###################################################
p2 <- ggplot(pinus.df, aes(x=Sub, y=Cones))
p2 <- p2 + geom_boxplot()
p2 <- p2 + theme_bw(base_size=20)
ytitle <- expression(paste("Subspecies of ", italic("Pinus sylvestris")))
p2 <- p2 + labs(x=ytitle, y="Number of cones")
p2

#c) Plot age depending on subspecies
####################################
p2b <- ggplot(pinus.df, aes(x=Sub, y=Age))
p2b <- p2b + geom_boxplot()
p2b <- p2b + theme_bw(base_size=20)
ytitle <- expression(paste("Subspecies of ", italic("Pinus sylvestris")))
p2b <- p2b + labs(x=ytitle, y="Age (years)")
p2b

#d) Plot number of cones depending on age, where the plot are split in a subplot for each subspecies
#####################################################################################################
p2c <- ggplot(pinus.df, aes(x=Age, y=Cones))
p2c <- p2c + geom_point()
p2c <- p2c + theme_bw(base_size=20)
p2c <- p2c + labs(x="Age (years)", y="Number of cones")
p2c <- p2c + facet_wrap(~Sub)
p2c

#e) Regression lines with CI
p2c <- p2c + geom_smooth(method=lm, formula=y~x)
p2c



##############
# Exercise 4 #
##############

#a) Import of data and check structure
######################################
tcb.df <- read.table("TCB.csv", header=T, sep=",", dec=".")
str(tcb.df)

#b) Plot of CFU depending on location
######################################
p3 <- ggplot(tcb.df, aes(x=Site, y=CFU))
p3 <- p3 + geom_boxplot()
p3 <- p3 + theme_bw(base_size=20)
p3 <- p3 + labs(x="Site", y="CFU")
p3



##############
# Exercise 5 #
##############

#a) Data import and a screen print of the whole dataset
########################################################
sl.df <- read.table("Store.lungegaardsvann.csv", header=T, sep=",", dec=".")
sl.df


#b) Making a map of the study area with sampling locations shown
################################################################

#Loading required library (must be installed):
library(ggmap)

#Defining location and map type:
kart <- get_map(location = c(lon=5.343955, lat=60.38229), zoom=15, maptype="satellite")

#Creating basic map:
map.SL <- ggmap(kart)

#Adding axis titles and increase text size of plot:
map.SL <- map.SL + labs(x="Longitude", y="Latitude")
map.SL <- map.SL + theme_bw(base_size=20)

#Adding sampling locations indicated with location number
map.SL <- map.SL + geom_text(data=sl.df, aes(Longitude, Latitude, label=Location), size=6, col="red")
map.SL


#c) A plot with location number on the x-axis and CFU on the y-axis
####################################################################
p4 <- ggplot(data=sl.df, aes(Location, CFU))
p4 <- p4 + geom_point(size=3)
p4 <- p4 + theme_bw(base_size=20)
p4 <- p4 + geom_abline(slope=0, intercept=50, col="green", lwd=2)
p4 <- p4 + geom_abline(slope=0, intercept=100, col="red", lwd=2)
p4

