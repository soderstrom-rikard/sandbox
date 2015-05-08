# -*- coding: utf-8 -*-
"""
 * Copyright (C) 2015-2020 Rikard Söderström, <soderstrom.rikard@gmail.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the version 2 of the GNU General Public License
 * as published by the Free Software Foundation
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, see <http://www.gnu.org/licenses/>
"""
import arch
from arch import *

def PrettyPrint(l,width=19):
  print "["
  for ind,b in enumerate(l):
    print '  ' + repr(b).ljust(width,' '),
    if ind+1 < len(l):
      print ', ',
    if (ind+1)%4 == 0 and ind+1 != len(l):
      print ''
  print "\n]"

#  print ''.join([repr(b).ljust(width,' ')+', '+('\n' if (ind+1)%4==0 else '') for ind,b in enumerate(l)])


print "Processors for the ADSP-218x DSPs"
PrettyPrint(arch.adsp218x.Processors, width = 12)
print "Processors for the ADSP-219x DSPs"
PrettyPrint(arch.adsp219x.Processors, width = 12)

adsp219x_keywords_added   = list(set(arch.adsp219x.Keywords).difference(set(arch.adsp218x.Keywords)))
adsp219x_keywords_removed = list(set(arch.adsp218x.Keywords).difference(set(arch.adsp219x.Keywords)))
adsp219x_keywords_added  .sort()
adsp219x_keywords_removed.sort()

print "Keywords added when creating adsp219x (based on adsp218x)"
PrettyPrint(adsp219x_keywords_added)
print "Keywords removed when creating adsp219x (based on adsp218x)"
PrettyPrint(adsp219x_keywords_removed)
