#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from time import strftime
from collections import Counter

archivo = file('README', 'r').read();
fichas  = re.findall('Fichas\s]=*(.*)==\[.*', archivo, re.S);
tipos   = re.findall('Tipo:\s*(.*)', fichas[0]);

empresas = organismos = universidades = otros = 0;
for tipo in tipos:
    if tipo == 'empresa':
       empresas += 1
    elif tipo == 'organismo':
       organismos += 1
    elif tipo == 'universidad':
       universidades += 1
    else:
       otros += 1

print "%-20s:%4d\n" % ('Total', empresas+organismos+universidades)
file("stats.txt", 'w').write("%-20s:%4d\n\n" % ('Total', empresas+organismos+universidades));

print "Por tipo:"
file("stats.txt", 'a').write("Por tipo:\n");
print "* %-18s:%4d" % ('Empresas', empresas)
file("stats.txt", 'a').write("* %-18s:%4d\n" % ('Empresas', empresas));
print "* %-18s:%4d" % ('Organismos', organismos)
file("stats.txt", 'a').write("* %-18s:%4d\n" % ('Organismos', organismos));
print "* %-18s:%4d" % ('Universidades', universidades)
file("stats.txt", 'a').write("* %-18s:%4d\n" % ('Universidades', universidades));
if otros > 0:
   print "* %-18s:%4d" % ('Otros', otros)
   file("stats.txt", 'a').write("* %-18s:%4d\n" % ('Otros', otros));

print "\nPor provincia:"
file("stats.txt", 'a').write("\nPor provincia:\n");
provincias = re.findall('Ubicación:\s*([\w\sáéíóú\/]*)\s', fichas[0]);
provincias = Counter(provincias)
for key in sorted(provincias):
    if any(i in key for i in 'áéíóú'):
       print "* %-19s:%4d" % (key, provincias[key])
       file("stats.txt", 'a').write("* %-19s:%4d\n" % (key, provincias[key]));
    else:
       print "* %-18s:%4d" % (key, provincias[key])
       file("stats.txt", 'a').write("* %-18s:%4d\n" % (key, provincias[key]));

file("stats.txt", 'a').write(strftime("\nActualizado         : %d-%m-%Y %H:%M:%S\n"));
