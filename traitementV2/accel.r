setwd('Stage')
accelpt=read.table(file="accelpt4.csv",sep=";",header=TRUE)
names(accelpt)
lissage=loess(or~ab,accelpt)
plot(accelpt$ab,accelpt$or,main="",pch=19,col='blue',xlab="Numéro de l'image",ylab="Accélération sans l'unité")
xyfit=predict(lissage, newdata=accelpt$ab)
lines(accelpt$ab,yfit,lwd=4,type='l',col='red')