#create maps
faroe.krill.df <- read.table("http://folk.uib.no/nzlkj/data/faroe.krill.txt", sep=",", header=T)
head(faroe.krill.df)

library(ggmap)
faroe <- get_map(location = c(lon = -5.578105, lat = 61.928955), zoom = 7, maptype = "satellite")
map1 <- ggmap(faroe)
map1

#Add sampling stations showing amount
#of krill at each of them:
map1 <- map1 + geom_point(data=faroe.krill.df, aes(Longitude, Latitude, size=Krill.m2),shape=19, col="red")
map1