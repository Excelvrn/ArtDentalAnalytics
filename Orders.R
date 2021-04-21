Dataset <- read.table("/home/excelvrn/Statistics/Orders.txt", header=FALSE, sep="\t", na.strings="NA", dec=",", strip.white=TRUE)

###grepl("ГН", Dataset[,4])
l<-c()
id<-c()
for (i in 1:dim(Dataset)[1]){
	if (grepl("ГН", Dataset[i,4])==TRUE){
		id<-c(id,Dataset[i,3])
	}
}
id
id<-sort(id)


#################
#################
#################
#################
#	Убрать повторы
#################
ido<-c()
last<-0
for (i in 1:length(id)){
	if (i==1) {ido<-c(id[1]); last<-id[1]}
	else if (id[i]!=last){ last <-id[i]; ido<-c(ido,last)}
}
ido

#
#	Записать NA при несовпадении
#
for (i in 1:length(ido)){
	for (ii in 1:dim(Dataset)[1]){
		if (ido[i] == Dataset[ii,3]){idc<-c(idc,ido[i]); dt<-c(dt,Dataset[i,2]) }
	}
}
length(ido)
dt
idc
length(dt);length(ido)

copy<-data.frame(Dataset[,1],Dataset[,2],Dataset[,3],Dataset[,4])
dim(copy)

dcs <-data.frame(Dataset[,3], Dataset[,2])
dcs
length(ido)
dim(copy)
li<-c()
for (i in 1:length(ido)){
	for (i2 in 1:dim(dcs)[1]){
		if (ido[i] == dcs[i2,1])
			li<-c(li,i2)
	}
}
ttt<-data.frame(dcs[1,1], dcs[1,2])
for (i in 1:length(li)) ttt[dim(ttt)[1]+1, ] <-dcs[li[i],]
ttt
length(li)
count<-0
for (i in 2:dim(ttt)[1]){ 
	if (i==2) l<-ttt[2,1]
	else {
		if (l==ttt[i,1])
			count<-count+1
		else {
			print(c(l,count))
			count<-1
			l<-ttt[i,1]
		}
	}
}
with(ttt, Hist(dcs.1..1., scale="frequency", breaks="Sturges", col="darkgray"))

