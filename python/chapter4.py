english = 'Monday', 'Tuesday', 'Wednesday';
french = 'Lundi', 'Mardi', 'Mercredi';
dict( zip(english, french) );

rows = range(1,10);
cols = range(2,10);

cells = [(row, col) for row in rows for col in cols];

numbers = [1, 3, 5]; #list
position = 0;
while position < len(numbers):
    number = numbers[position];
    if(number % 2 == 0 ):
        print("Found even number", number);
        break;
    position += 1;
else:
    print("No even number found");


# for文

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter'];

for rabbit in rabbits:
    print(rabbit);

#dict

word = "letters";
letter_counts = {letter: word.count(letter) for letter in set(word)}; #setにすることにより重複作業を減らし効率化
print(letter_counts);

#generator

number_thing = (number for number in range(1,22));

for number in number_thing:
    print(number);

try_again = list(number_thing);
print(try_again);

#def

def do_nothing():
    pass;
do_nothing();

def make_a_sound():
    print("quack");
make_a_sound();

def echo(anything):
    return anything + ' ' + anything;
any_messages = input("plz enter messages : ");
print(echo(any_messages));