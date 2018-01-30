import pandas as pd

directions=[]
#DEMdata is a DataFrame
def D8(DEMdata,startpoint):
	rows,columns = DEMdata.shape
	row=startpoint[0]
	column=startpoint[1]
	maxP=0.0
	P=0.0
	m=0
	n=0
	height=DEMdata.iat[row, column]
	if row >= 0 and row < rows and column < columns and column > 0:
		for i in range(-1,2):
			for j in range(-1,2):
				if (row+i)<rows and (column+j)<columns and (row+i)>=0 and (column+j)>=0:
					if i==0 and j==0:
						pass
					else:
						if (DEMdata.iat[row, column]-DEMdata.iat[row+i, column+j])>0:
							if (i+j)%2==0:
								P=(DEMdata.iat[row, column]-DEMdata.iat[row+i, column+j])/diagonalLength
							else:
								P=(DEMdata.iat[row, column]-DEMdata.iat[row+i, column+j])
							if P>maxP:
								maxP=P
								m=i
								n=j
	if maxP<=0:
		return startpoint
	else:
		row+=m
		column+=n
		directions.append([row,column])
		return D8(DEMdata,[row,column])
