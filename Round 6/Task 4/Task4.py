import re

contacts = """Project Expert Stina.Boedeker@uta.fi
PINNI B1049 040 865 9520 Study Secretary
Minna.I.Heinonen@uta.fi PINNI B1053 050 318 6398
Executive Secretary Heli.Jokiaho@uta.fi PINNI B1052
040 190 9840 Travel Secretary Minna.Koskela@uta.fi
PINNI B1055 050 318 7056 Head of Study Affairs
Taru.Koskinen@uta.fi PINNI B1051 040 190 1219 Study
Secretary Elisa.Laatikainen@uta.fi PÄÄT C106 Study
Coordinator Ulla.Lassila@uta.fi SJOKI 050 549 0420
HR Specialist Nina.Majamaki@uta.fi PINNI A2031 050
318 6911 Study Coordinator Tiina.Maenpaa@uta.fi
PINNI B1060 050 437 7321 Financial Expert
Minna.K.Parviainen@uta.fi PINNI B1046 050 421 1064
Study Coordinator Heli.Rikala@uta.fi PINNI B1058 050
318 6669 Head of Administrative Affairs
Sari.Saastamoinen@uta.fi PINNI A2036 040 190 1479
Coordinator of International Education
Kirsi-Marja.Tuominen@uta.fi PINNI B1057 050 318 6688
Administrative Secretary Anneli.Ostman@uta.fi PINNI
B1048 050 437 2649 Study Coordinator
Anna.Vahamaki@uta.fi PÄÄT E227 050 318 6639 Trainee
Iida.Roksa@uta.fi PINNI B1061 050 437 7470"""

telpatt = r'redefine me'
telg = 0
emailpatt = r'redefine me'
emailg = 0
roompatt = r'redefine me'
roomg = 0

# Add below new definitions for telpatt, emailpatt and roompatt.
# Also redefine telg, emailg and/or roomg, if necessary.

telpatt = r'\d{3}\s\d{3}\s\d{4}'
emailpatt = r'[A-Za-zÄäÖö\-\.]+@[A-Za-zÄäÖö\-]+\.[A-Za-zÄäÖö\-\.]+'
roompatt = r'[A-Za-zÄäÖö\-\.]+@[A-Za-zÄäÖö\-]+\.[A-Za-zÄäÖö\-\.]+\s([A-ZÄÖ]+(\s[A-ZÄÖ]+[0-9]+)?)'
roomg = 1


# Add above new definitions for telpatt, emailpatt and roompatt.
# Also redefine telg, emailg and/or roomg, if necessary.
for pattern, group in ((telpatt, telg), (emailpatt, emailg), (roompatt, roomg)):
  res = [r for r in re.finditer(pattern, contacts)]
  res = [r.group(group).replace("\n", " ") for r in res]
  for i in range(0, len(res), 2):
    print(", ".join(res[i:i+2]))
  print()
