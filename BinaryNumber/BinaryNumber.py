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
class BinaryNumberException(Exception):
  def __init__(self,bitstring):
    self.val = "Invalid bitstring \"" +bitstring+ "\""

  def __repr__(self):
    return "%s(%s)" % (self.__class__, repr(self.val))

  def __str__(self):
    return self.val

class BinaryNumber:
  def __init__(self,bitstring_or_value):

    try:
      if isinstance(bitstring_or_value,str):
        self.bitstring = bitstring_or_value
        self.bitstring = bin(self.Val())
      else:
        self.bitstring = bin(bitstring_or_value)
    except ValueError:
      raise BinaryNumberException(self.bitstring)

  """ Integer operator overload """
  def __add__(self,other):
    return self.Operator('__add__',other)

  def __sub__(self,other):
    return self.Operator('__sub__',other)

  def __mul__(self,other):
    return self.Operator('__mul__',other)

  def __pow__(self,other):
    return self.Operator('__pow__',other)

  def __div__(self,other):
    return self.Operator('__div__',other)

  def __truediv__(self,other):
    return self.Operator('__truediv__',other)

  def __floordiv__(self,other):
    return self.Operator('__floordiv__',other)

  def __mod__(self,other):
    return self.Operator('__mod__',other)

  def __lshift__(self,other):
    return self.Operator('__lshift__',other)

  def __rshift__(self,other):
    return self.Operator('__rshift__',other)

  def __and__(self,other):
    return self.Operator('__and__',other)

  def __or__(self,other):
    return self.Operator('__or__',other)

  def __xor__(self,other):
    return self.Operator('__xor__',other)

  def __invert__(self):
    return self.Operator('__invert__')

  """ String operator overloads """
  def __getitem__(self,key):
    sign, bits = self.bitstring.split('0b')
    return BinaryNumber('0b'.join([sign,bits[key]]))

  def __getslice__(self,i,j):
    return self.__getitem__(slice(i,j))

  def __len__(self):
    return len(self.bitstring.split('0b')[1])

  def __repr__(self):
    return "%s(%s)" % (self.__class__, repr(self.bitstring))

  def __str__(self):
    return self.bitstring

  """ Member Functions """
  def Operator(self,operator,other = None):
    func = getattr(self.Val(),operator)
    if other == None:
      return BinaryNumber(func())
    else:
      return BinaryNumber(func(other.Val()))

  def Val(self):
    return int(self.bitstring,2)
