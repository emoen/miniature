tcb.df <- read.table("Store.lungegaardsvann.csv", header=T, dec=",", sep=";")
str(tbc.df)

#b)


#functino
volume.sphere <- function(radius) {
if ( radius < 0 )
stop("asdf")
if (missing(radius))
stop("aadsf")
a <- (4/3)*pi*radius^3
return(a)
}

volume.sphere(15)

#prediktor - x aksen, response - y akse

#tukey test	
#maximum likelyhood test - poisson 	
