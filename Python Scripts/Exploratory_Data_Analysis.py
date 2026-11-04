# File reading and dataset slicing
df = pd . read_csv ( ’ 50 _Startups_dataset . csv ’)
df_c = df [ df [ ’ State ’ ]== ’ California ’]
# Summary Statistics
df . describe ( include = ’ all ’)
df_c . describe ( include = ’ all ’)
# Numeric Histograms ( Statewise and Overall )
df [ ’ Profit ’ ]. hist ( bins =10 , color = ’ yellow ’ , edgecolor = ’ green ’ ,
grid = False )
plt . title ( ’ All ␣ Startups ’)
plt . show ()
# Scatter Matrix
colours = df [ ’ State ’ ]. map ({ ’ New ␣ York ’: ’ red ’ , ’ Florida ’: ’ blue ’ ,
’ California ’: ’ green ’ })
pd . plotting . scatter_matrix ( df [[ ’ Profit ’ , ’ Marketing ␣ Spend ’ , ’
Administration ’ , ’R & D ␣ Spend ’]] , c = colours , figsize =(10 , 10)
)
plt . show ()
# Statewise Scatter Matrix
# For New York City based Startups
pd . plotting . scatter_matrix ( df_y [[ ’ Profit ’ , ’ Marketing ␣ Spend ’ , ’
Administration ’ , ’R & D ␣ Spend ’]] , c = ’ red ’ , figsize =(8 , 8) )
plt . show ()
# Correlation Matrix
df_numeric = df [[ ’ Profit ’ , ’ Marketing ␣ Spend ’ , ’ Administration ’ , ’
R & D ␣ Spend ’ ]]
corr_matrix_all = df_numeric . corr ()
13
sns . heatmap ( corr_matrix_all , annot = True , cmap = ’ inferno ’)
plt . show ()
# Florida Based Startups Correlation Matrix
df_f_numeric = df_y [[ ’ Profit ’ , ’ Marketing ␣ Spend ’ , ’ Administration
’ , ’R & D ␣ Spend ’ ]]
corr_matrix_florida = df_f_numeric . corr ()
sns . heatmap ( corr_matrix_florida , annot = True , cmap = ’ inferno ’)
plt . show ()
# Statewise Boxplots
plt . figure ( figsize =(10 , 6) )
sns . boxplot ( x = ’ State ’ , y = ’R & D ␣ Spend ’ , data = df , palette = ’ Set2 ’)
plt . title ( ’R & D ␣ Spend ␣ vs . ␣ State : ␣ Visualizing ␣ Location ␣ Influence ’
)
plt . grid ( axis = ’y ’ , linestyle = ’ -- ’ , alpha =0.7)
plt . show ()