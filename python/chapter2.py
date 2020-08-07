poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not conld that doth the fire put out
But 'tis the wet that makes it die, no doubt.''';

print(poem[:13]);
print(len(poem));
print(poem.startswith('All'));
word = 'the';
print(poem.find(word));
print(poem.count(word));

setup = 'a duck goes into a bar...';
setup.strip('.');

ym = '2020-07';
print(ym.strip('-'));
print(setup.ljust(10));

#2-1 

min = 60;
answer = min * 60;
print ('1hour is ', answer,'sec');


#2-2

second_per_hour = answer;

#2-3

print(second_per_hour * 24);

#2-4

second_per_day = second_per_hour * 24;
print(second_per_day);

#2-5, 2-6

print(second_per_day / second_per_hour);
print(second_per_day // second_per_hour);
