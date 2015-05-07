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
from BinaryNumber import *

a = BinaryNumber('01011100011')
b = BinaryNumber(21)

print "Bitstring '"+str(a)+"' have value" + str(a.Val())
print " a = " + str(a.Val())
print " b = " + str(b.Val())
print " a +  b = " + str((a+b).Val())
print " a -  b = " + str((a-b).Val())
print " a *  b = " + str((a*b).Val())
print " a ** b = " + str((a**b).Val())
print " a /  b = " + str((a/b).Val())
print " a // b = " + str((a//b).Val())
print " a %  b = " + str((a%b).Val())
print " a << b = " + str((a<<b).Val())
print " a >> b = " + str((a>>b).Val())
print " a &  b = " + str((a&b).Val())
print " a |  b = " + str((a|b).Val())
print " a ^  b = " + str((a^b).Val())
print "     ~b = " + str((~b).Val())
print "a[::-1] = " + str(a[::-1])
print "a[-4:]  = " + str(a[-4:])
