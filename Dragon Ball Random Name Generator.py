import random

print("Dragon Ball Random Character Name Generator")
print("Developed By NamesJoeyWheeler")
print("")

chars = 'Goku', 'Bulma', 'Master Roshi', 'Yamcha', 'Krillin', 'Tien', 'Piccolo', 'Gohan', 'Vegeta', 'Trunks', 'Android 18', 'Goten', 'Beerus', 'Whis', 'Freeza', 'Raditz', 'Nappa', 'Zarbon', 'Doboria', 'Guldo', 'Recoome', 'Burter', 'Jeice', 'Captain Ginyu', 'Cell', 'Broly', 'Babaidi', 'Dabura', 'Majin Buu', 'Goku Black', 'Zamasu', 'Oolong', 'Puar', 'Chi-Chi', 'Ox-King', 'Launch', 'Chiaotzu', 'Dr. Briefs', 'Korin', 'Yajirobe', 'Mr. Popo', 'Kami', 'Dende', 'Android 17', 'Mr. Satan', 'Videl', 'Marron', 'Pan', 'Uub', 'Jaco', 'Android 16', 'Arale', 'Bardock', 'Champa', 'Grandpa Gohan', 'The Kai', 'Kaio-Shin', 'King Vegeta', 'Emperor Pilaf', 'Mai', 'Shenron', 'Cabba', 'Frost', 'Hit', 'Fortuneteller Baba', 'Zeno', 'Garlic Jr.', 'Cooler', 'Pikkon', 'Giru', 'Doctor Myuu', 'Baby'
length = (1)
length = int(length)

sentence = ''
for c in range(length):
 sentence += random.choice(chars)
print("----------------------------")
print(sentence)
