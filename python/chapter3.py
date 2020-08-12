import chapter2;

empty_list = list();
marxes = ['Groucho', 'Chico', 'Harpo'];
print(marxes[-1]);
marxes.append('Zeppo');
print(marxes[:]);
print(', '.join(marxes));
print(marxes[0].strip('o'));

a = [1, 2, 3];
b = a;
a[0] = 111;
print(b[0]);

#tuple 

empty_tuple = ();

marx_tuple = (1, 2, 3);
a, b, c = marx_tuple;
print(a, b);

#dict

empty_dict = {};
bierce = {
    "day" : "A period of twenty-four hours, mostly misspent", 
    "positive" : "Mistaken at the top of one's voice", 
    "misfortune" : "The kind of fortune that never misses"
    };
pythons = {
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Idle' : 'Eric',
    'Jones' : 'Terry',
    'Palin' : 'Michael'
   };

pythons['Gilliam'] = "test";

print(bierce['day']);


drinks = {
    "martini" : {"vodka", "vermouth"},
    "black russian" : {"vodka", "kahlua"},
    "white russian" : {"cream", "kahlua", "vodka"},
    "manhattan" : {"rye", "vermouth", "bitters"},
    "screwdriver" : {"orange juice", "vodka"}
    };

for name, contents in drinks.items():
    print(name);
    print(contents);

rella_list = ["mozzarella", "cinderella", "salmonella"];

for contents in rella_list:
   if contents in "mozzarella":
        print(contents);


# 3-1
year_list = [1996, 1995, 1997, 1998, 1999];
year_list.sort();
print(year_list);

# 3-2
third_birthday = year_list[2];
print(third_birthday);

# 3-3
print(year_list[-1]);

# 3-4
things = ["mozzarella", "cinderella", "salmonella"];

# 3-5
print(things[1].capitalize());

# 3-6
things[0] = things[0].upper();
print(things);

# 3-7
things.pop();
print(things);

# 3-8
surprise = ["Groucho", "Chico", "Harpo"];

# 3-9 difficult discorrect
surprise[-1] = surprise[-1].lower();
sorted_surprise = sorted(surprise[-1], reverse = True);
sorted_surprise = ''.join(sorted_surprise);
surprise[-1] = sorted_surprise.capitalize();
print(surprise[-1]);

surprise = ["Groucho", "Chico", "Harpo"];
surprise[-1] = surprise[-1].lower();
surprise[-1] = surprise[-1][::-1];
surprise[-1] = surprise[-1].capitalize();
print(surprise[-1]);

# 3-10
e2f = {"dog" : "chien", "cat" : "chat", "walrus" : "morse"};
print(e2f);

# 3-11
print(e2f["walrus"]);

# 3-12
""" f2e = {};
    for key, value in e2f.items():
        f2e[value] = key; """

# 内包辞書
f2e = {french : english for english, french in e2f.items()};
print(f2e);
# 3-13
print(f2e["chien"]);

# 3-14
set_e2f = set(e2f.keys());
print(set_e2f);

# 3-15
life = {"animals" : {"cats" : ["Henri", "Grumpy", "Lucy"], "octopi" : {}, "emus" : {}}, "plants" : {}, "other" : {}};

# 3-16
print(life.keys());

#3-17
print(life["animals"]);

#3-18
print(life["animals"]["cats"]);
