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
import sys, struct, wave
from collections import OrderedDict

class Progression:
  def __init__(self,steps=25):
    self.steps = steps

  def Print(self, percent):
    hashes = self.steps*int(percent)/100
    spaces = self.steps-hashes
    print '\r[{0}] {1}%'.format('#'*hashes+' '*spaces, percent),

  def __del__(self):
    print ''

class ChunkError(Exception):
  def __init__(self,expected,actual):
    self.val = "Invalid header, expected \"" +expected+ "\" got \"" +actual+ "\""

  def __str__(self):
    return repr(self.val)

class Chunk(object):

  def ConfigureFormat(self, fmt_str, ByteOrder = "<"):
    self.chunk = struct.Struct(ByteOrder+fmt_str)

  def Validate(self, value_array):
    if self.header != value_array[0]:
      raise ChunkError(self.header,value_array[0])

  def __str__(self):
    l = filter(lambda x: not x.startswith('__'), dir(self))
    s = ''
    for attrib in l:
      o = getattr(self,attrib)
      if o == None:
        s = s + attrib+": None" + '\n'
      else:
        s = s + attrib+": "+str(o) + '\n'
    return s

class dsd_chunk(Chunk):
  def __init__(self):
    self.ConfigureFormat("4sQQQ")
    self.header         = "DSD " # 4s, DSD Header
    self.size           = None   #  Q, Chunk Size
    self.file_size      = None   #  Q, Total File Size
    self.metadata_start = None   #  Q, Metadata Offset

  def unpack(self, buf, offset=0):
    val_array = self.chunk.unpack_from(buf,offset)
    self.Validate(val_array)

    self.size           = val_array[1]
    self.file_size      = val_array[2]
    self.metadata_start = val_array[3]
    return self

class fmt_chunk(Chunk):
  def __init__(self):
    self.ConfigureFormat("4sQLLLLLLQLL")
    self.header          = "fmt " # 4s, FMT Header
    self.size            = None   #  Q, Chunk Size
    self.fmt_version     = None   #  L, Format Version
    self.fmt_id          = None   #  L, Format ID              0: DSD raw
    self.channel_type    = None   #  L, Channel Type           0: mono, 1: stereo, 3: 3 channels, 4: quad, 5: 4 channels, 6: 5 channels, 7: 5.1 channels
    self.channel_num     = None   #  L, Channel num            1: mono, 2: stereo .. 6: 6 channels
    self.sampling_freq   = None   #  L, Sampling Frequency     2822400, 5644800 [Hz]
    self.bits_per_sample = None   #  L, Bits Per Sample        1 bit (LSB), 8 bits (MSB)
    self.sample_count    = None   #  Q, Sample Count = Sample Frequency * n, where n is number of seconds
    self.block_size      = None   #  L, Block Size per channel, usually 4096 bytes
    self.reserved        = None   #  L, Reserved

  def unpack(self, buf, offset=28):
    val_array = self.chunk.unpack_from(buf,offset)
    self.Validate(val_array)

    self.size            = val_array[ 1]
    self.fmt_version     = val_array[ 2]
    self.fmt_id          = val_array[ 3]
    self.channel_type    = val_array[ 4]
    self.channel_num     = val_array[ 5]
    self.sampling_freq   = val_array[ 6]
    self.bits_per_sample = val_array[ 7]
    self.sample_count    = val_array[ 8]
    self.block_size      = val_array[ 9]
    self.reserved        = val_array[10]
    return self

class data_chunk(Chunk):
  def __init__(self):
    self.ConfigureFormat("4sQ")
    self.header = "data" # 4s, Data Header
    self.size   = None   #  Q, Chunk Size equal to n (see next line) + 12
    # nB, Data where n = Chunk Size - 12, during unpack we store the start and end pointers to data

  def unpack(self, buf, offset=80):
    val_array = self.chunk.unpack_from(buf,offset)
    self.Validate(val_array)

    self.size = val_array[ 1]
    self.start = offset + 12
    self.end   = offset + self.size
    return self

# For the metadata chunk one would need to implement the ID3v2 standard
# or use the http://eyed3.nicfit.net library, aka skipping metadata

class dsf2wave:
  def __init__(self,filename):
    print "Loading DSF File .."

    self.f = open(filename,'rb')
    f = self.f
    f.seek(0,2)
    min_size = 92
    file_size = f.tell()

    if file_size < min_size: # Minimum header size for a dsf file
      print "This file is corrupt or not a dsf formatted audio file"
      return

    f.seek(0,0)
    header = f.read(min_size)
    dsd  =  dsd_chunk().unpack(header)                     # ('DSD ', 28, 28221532, 0)
    fmt  =  fmt_chunk().unpack(header,dsd.size)            # ('fmt ', 52, 1, 0, 2, 2, 5644800, 1, 112885760, 4096, 0)
    data = data_chunk().unpack(header,dsd.size + fmt.size) # ('data', 28221452, 105)

    if file_size < data.end:
      print "(data_chunk) Bad header info"
      return
    self.dsd  = dsd
    self.fmt  = fmt
    self.data = data

    """ [ ANNOTATION 1 ] DSF Interleaved format """
    DSF_Interleaved_fmt = {
        1: ['front'                                                                         ], # mono
        2: ['front_left','front_right'                                                      ], # stereo
        3: ['front_left','front_right','center'                                             ], # 3 channels
        4: ['front_left','front_right','back_left','back_right'                             ], # quad
        5: ['front_left','front_right','center'   ,'low_frequency'                          ], # 4 channels
        6: ['front_left','front_right','center'   ,'back_left'    ,'back_right'             ], # 5   channels
        7: ['front_left','front_right','center'   ,'low_frequency','back_left' ,'back_right'], # 5.1 channels
        }[fmt.channel_type]

    """ [ ANNOTATION 4 ] Bits per sample is endian-dependent , 1 bit (LSB) Little Endian <, 8 bits (MSB) Big Endian > """
    data_packer = struct.Struct(('<' if fmt.bits_per_sample == 1 else '>') + str(fmt.block_size)+'s')
    self.bytes_per_channel = (data.end-data.start) / fmt.channel_num
    data_blocks = (data.end-data.start) / fmt.block_size

    # Extracting channels
    channels = {}
    for channel_name in DSF_Interleaved_fmt:
      channels[channel_name] = bytearray(self.bytes_per_channel)

    f.seek(data.start,0)
    progress = Progression()
    progress.Print(0)
    for b in range(data_blocks):
      channel_id   = b % fmt.channel_num
      channel_name = channels.keys()[channel_id]
      b_id         = b/fmt.channel_num
      block_start  = b_id*fmt.block_size
      block_end    = block_start + fmt.block_size
      channels[channel_name][block_start:block_end] = f.read(fmt.block_size)
      #channels[channel_name][block_start:block_end] = data_packer.pack(f.read(fmt.block_size))
      progress.Print((10000*(b+1)/data_blocks)/100.0)

    progress = None
    self.channels = channels

  def ToRaw(self,raw_file, max_bytes = -1):
    print "Writing raw file .."
    cend = len(self.channels[self.channels.keys()[0]])

    progress = Progression()
    progress.Print(0)
    with open(raw_file,'wb') as f:
      for channel_id in range(self.fmt.channel_num):
        channel_name = self.channels.keys()[channel_id]
        if 0 < max_bytes and max_bytes <= cend: # Avoid slicing big arrays
          f.write(self.channels[channel_name][0:max_bytes])
        else:
          f.write(self.channels[channel_name])
        progress.Print((10000*(channel_id+1)/self.fmt.channel_num)/100.0)

    progress = None
    for channel_id in range(self.fmt.channel_num):
      print self.channels.keys()[channel_id]

  def ToWave(self,wave_file):
    print "Writing wave file .."
    progress = Progression()
    wav = wave.open(wave_file,'wb')
    wav.setnchannels(self.fmt.channel_num)
    wav.setnframes(self.fmt.sample_count)
    wav.setsampwidth(1)
    wav.setframerate(self.fmt.sampling_freq)
    progress.Print(0)
    for channel_id in range(self.fmt.channel_num):
      channel_name = self.channels.keys()[channel_id]
      wav.writeframes(self.channels[channel_name])
      progress.Print((10000*(channel_id+1)/self.fmt.channel_num)/100.0)


    progress = None
    wav.close()

  def __str__(self):
    return "\nDSD\n"+str(self.dsd) + \
           "\nFMT\n"+str(self.fmt) + \
           "\nDATA\n"+str(self.data)


  def __del__(self):
    self.f.close()

dsf = dsf2wave("02-Mend My Mind.dsf")
dsf.ToRaw("tmp.mine.raw", 1056768)
#dsf.ToRaw("tmp.mine.raw", 4096*100)
#dsf.ToWave("tmp.mine.wav")
print " File converted"

"""
# When testing
import winsound

winsound.PlaySound(channels[channel_name], winsound.SND_MEMORY)
winsound.PlaySound("sound.wav",winsound.SND_FILENAME)
"""

