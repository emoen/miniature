do.boxplot <- function(dataset, response, predictor) {
p1 <- ggplot(data=dataset, aes(x=predictor, y=response))
p1 <- p1 + geom_boxplot()
return (p1)

}

do.boxplot(rats.df, Body.mass, Sex)