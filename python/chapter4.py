english = 'Monday', 'Tuesday', 'Wednesday';
french = 'Lundi', 'Mardi', 'Mercredi';
dict( zip(english, french) );

rows = range(1,10);
cols = range(2,10);

cells = [(row, col) for row in rows for col in cols]
