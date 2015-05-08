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

# For the ADSP-218x DSPs
Processors = [
  'ADSP-2181' , 'ADSP-2183' , 'ADSP-2184' , 'ADSP-2184L',
  'ADSP-2184N', 'ADSP-2185' , 'ADSP-2185L', 'ADSP-2185M',
  'ADSP-2185N', 'ADSP-2186' , 'ADSP-2186L', 'ADSP-2186M',
  'ADSP-2186N', 'ADSP-2187L', 'ADSP-2184L', 'ADSP-2187N',
  'ADSP-2188L', 'ADSP-2188N', 'ADSP-2189M', 'ADSP-2189N'
]

# ADSP-218x DSP Assembler Keywords
Keywords = [
  '.ALIGN'           , '.ASM_ASSERT'      , '.BYTE'            , '.DMSEG'           ,
  '.ELIF'            , '.ELSE'            , '.END_REPEAT'      , '.ENDIF'           ,
  '.ENDINCLUDE'      , '.ENDMACRO'        , '.ENDMOD'          , '.ENTRY'           ,
  '.EXPORT'          , '.EXTERN'          , '.EXTERNAL'        , '.FILE'            ,
  '.GLOBAL'          , '.IF'              , '.IMPORT'          , '.INCLUDE'         ,
  '.INDENT'          , '.INIT'            , '.INIT24'          , '.LEFTMARGIN'      ,
  '.LIST'            , '.LIST_DATA'       , '.LIST_DATFILE'    , '.LIST_DEFTAB'     ,
  '.LIST_LOCTAB'     , '.LIST_WRAPDATA'   , '.LOCAL'           , '.MACRO'           ,
  '.MODULE'          , '.NEWPAGE'         , '.NOLIST'          , '.NOLIST_DATA'     ,
  '.NOLIST_DATFILE'  , '.NOLIST_WRAPDATA' , '.ORG'             , '.PAGE'            ,
  '.PAGELENGTH'      , '.PAGEWIDTH'       , '.PMSEG'           , '.PORT'            ,
  '.PRECISION'       , '.PREVIOUS'        , '.REPEAT'          , '.ROUND_MINUS'     ,
  '.ROUND_NEAREST'   , '.ROUND_PLUS'      , '.ROUND_ZERO'      , '.SECTION'         ,
  '.SETDATA'         , '.SIZE'            , '.STRUCT'          , '.TYPE'            ,
  '.VAR'             , '.VCSE_METHODCALL' , '_END'             , '.VCSE_METHODCALL' ,
  '_START'           , '.VCSE_METHODCALL' , '_RETURNS'         , '.WEAK'            ,
  '__DATE__'         , '__FILE__'         , '__LINE__'         , '__STDC__'         ,
  '__TIME__'         , 'ABS'              , 'AC'               , 'ADDRESS'          ,
  'AF'               , 'AND'              , 'AR'               , 'AR_SAT'           ,
  'AS'               , 'ASHIFT'           , 'ASTAT'            , 'AV'               ,
  'AV_LATCH'         , 'AX0'              , 'AX1'              , 'AYO'              ,
  'AY1'              , 'BIT_REV'          , 'BOOT'             , 'BR'               ,
  'BY'               , 'C'                , 'CALL'             , 'CE'               ,
  'CIRC'             , 'CLRBIT'           , 'CLRBIT'           , 'CLRINT'           ,
  'CNTR'             , 'CODE'             , 'CONST'            , 'DATA'             ,
  'DIS'              , 'DIVQ'             , 'DIVS'             , 'DM'               ,
  'DMOVLAY'          , 'D0'               , 'E_MODE'           , 'EMUIDLE'          ,
  'ENDINCLUDE'       , 'ENDMACRO'         , 'E0'               , 'EXPEXPADJ'        ,
  'FI'               , 'FL0'              , 'FL1'              , 'FL2'              ,
  'FLAG_IN'          , 'FLAG_OUT'         , 'FLUSH'            , 'FO'               ,
  'FOREVER'          , 'G_MODE'           , 'GE'               , 'GM'               ,
  'GT'               , 'HI'               , 'HIX'              , 'I0'               ,
  'I1'               , 'I2'               , 'I3'               , 'I4'               ,
  'I5'               , 'I6'               , 'I7'               , 'ICNTL'            ,
  'IDLE'             , 'IF'               , 'IFC'              , 'IMASK'            ,
  'INCLUDE'          , 'INIT24'           , 'INT'              , 'INTS'             ,
  'IO'               , 'ISTAT'            , 'JUMP'             , 'L0'               ,
  'L1'               , 'L2'               , 'L3'               , 'L4'               ,
  'L5'               , 'L6'               , 'L7'               , 'LE'               ,
  'LENGTH'           , 'LINE'             , 'LO'               , 'LOOPLSHIFT'       ,
  'LT'               , 'M0'               , 'M1'               , 'M2'               ,
  'M3'               , 'M4'               , 'M5'               , 'M6'               ,
  'M7'               , 'M_MODE'           , 'MACRO'            , 'MF'               ,
  'MODIFY'           , 'MR'               , 'MR0'              , 'MR1'              ,
  'MR2'              , 'MSTAT'            , 'MV'               , 'MX0'              ,
  'MX1'              , 'MY0'              , 'MY1'              , 'NE'               ,
  'NEG'              , 'NONE'             , 'NOPNORM'          , 'NOT'              ,
  'OF'               , 'OFFSET'           , 'OL'               , 'OR'               ,
  'OWRCNTR'          , 'PAGE'             , 'PAGEID'           , 'PASS'             ,
  'PC'               , 'PM'               , 'PMCODE'           , 'PMDATA'           ,
  'PMOVLAY'          , 'POP'              , 'POS'              , 'PUSH'             ,
  'PX'               , 'RAM'              , 'RESET'            , 'RND'              ,
  'ROM'              , 'RTI'              , 'RTS'              , 'RX0'              ,
  'RX1'              , 'SAT'              , 'SB'               , 'SE'               ,
  'SEC_REG'          , 'SEG'              , 'SET'              , 'SETBIT'           ,
  'SETINT'           , 'SHIFT'            , 'SHT_DEBUGINFO'    , 'SHT_DM'           ,
  'SHT_DYNAMIC'      , 'SHT_DYNSYM'       , 'SHT_HASH'         , 'SHT_LDF'          ,
  'SHT_NOBITS'       , 'SHT_NOTE'         , 'SHT_NULL'         , 'SHT_PMCODE'       ,
  'SHT_PMDATA'       , 'SHT_PROCESSORTYPE', 'SHT_PROGBITS'     , 'SHT_REL'          ,
  'SHT_RELA'         , 'SHT_SEGMENINFO'   , 'SHT_SHLIB'        , 'SHT_STRTAB'       ,
  'SHT_SYMTAB'       , 'SI'               , 'SIMIDLE'          , 'SIZEOF'           ,
  'SR'               , 'SR0'              , 'SR1'              , 'SS'               ,
  'SSTAT'            , 'STATIC'           , 'STRUCT'           , 'STS'              ,
  'STT_FUNC'         , 'STT_OBJECT'       , 'SU'               , 'TGLBIT'           ,
  'TI'               , 'TIMER'            , 'TOGGLE'           , 'TOPLOOPSTACKH'    ,
  'TOPLOOPSTACKL'    , 'TOPPCSTACK'       , 'TRAP'             , 'TRUE'             ,
  'TSTBIT'           , 'TX0'              , 'TX1'              , 'UNTIL'            ,
  'US'               , 'UU'               , 'XOR'
]
