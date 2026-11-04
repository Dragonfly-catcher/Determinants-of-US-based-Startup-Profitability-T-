df_dummies = pd . get_dummies ( df , columns =[ ’ State ’] , drop_first =
True )
print ( df_dummies )
# Creating the X matrix
X = df_dummies . drop ([ ’ Profit ’ , ’ Unnamed : ␣ 0 ’] , axis =1) . astype (
float )
X = sm . add_constant ( X )
# Define the Y vector
y = df_dummies [ ’ Profit ’ ]. astype ( float )
model = sm . OLS (y , X ) . fit ()
print ( model . summary () )
# Refined Model
X_new = df [ ’R & D ␣ Spend ’]
model_refined = sm . OLS (y , X_new ) . fit ()
print ( model_refined . summary () )
# Alternative Model
X_last = df [[ ’R & D ␣ Spend ’ , ’ Marketing ␣ Spend ’ ]]
model_last = sm . OLS (y , X_last ) . fit ()
print ( model_last . summary () )