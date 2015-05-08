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

# For the ADSP-219x DSPs
Processors = [
  'ADSP-2191', 'ADSP-2192-12', 'ADSP-2195',
  'ADSP-2196', 'ADSP-21990'
]

Keywords = [
'.ALIGN'           , '.ASM_ASSERT'      , '.BYTE'            , '.DATA'            ,
'.DMBSS'           , '.DMSEG'           , '.DW'              , '.ELIF'            ,
'.ELSE'            , '.END_REPEAT'      , '.ENDIF'           , '.ENDINCLUDE'      ,
'.ENDMACRO'        , '.ENDMOD'          , '.ENTRY'           , '.EXPORT'          ,
'.EXTERN'          , '.EXTERNAL'        , '.FILE'            , '.GENLABEL'        ,
'.GLOBAL'          , '.IF'              , '.'                , 'IMPORT'           ,
'.INCLUDE'         , '.INDENT'          , '.INIT'            , '.INIT24'          ,
'.LEFTMARGIN'      , '.LIST'            , '.LIST_DATA'       , '.LIST_DATFILE'    ,
'.LIST_DEFTAB'     , '.LIST_LOCTAB'     , '.LIST_WRAPDATA'   , '.LOCAL'           ,
'.MACRO'           , '.MODULE'          , '.NEWPAGE'         , '.NOLIST'          ,
'.NOLIST_DATA'     , '.NOLIST_DATFILE'  , '.NOLIST_WRAPDATA' , '.ORG'             ,
'.PAGE'            , '.PAGELENGTH'      , '.PAGEWIDTH'       , '.PMBSS'           ,
'.PMSEG'           , '.PORT'            , '.PRECISION'       , '.PREVIOUS'        ,
'.REPEAT'          , '.ROUND_MINUS'     , '.ROUND_NEAREST'   , '.ROUND_PLUS'      ,
'.ROUND_ZERO'      , '.SECTION'         , '.SETDATA'         , '.SIZE'            ,
'.STRUCT'          , '.TYPE'            , '.VAR'             , '.WEAK'            ,
'__DATE__'         , '__FILE__'         , '__LINE__'         , '__STDC__'         ,
'__TIME__'         , 'ABS'              , 'AC'               , 'ADDRESS'          ,
'AF'               , 'AND'              , 'AR'               , 'AR_SAT'           ,
'AS'               , 'ASHIFT'           , 'ASTAT'            , 'AV'               ,
'AV_LATCH'         , 'AX0'              , 'AX1'              , 'AYO'              ,
'AY1'              , 'B0'               , 'B1'               , 'B2'               ,
'B3'               , 'B4'               , 'B5'               , 'B6'               ,
'B7'               , 'BIT_REV'          , 'BOOT'             , 'BR'               ,
'BY'               , 'C'                , 'CACHE'            , 'CACTL'            ,
'CALL'             , 'CCODE'            , 'CE'               , 'CIRC'             ,
'CLRBIT'           , 'CLRINT'           , 'CNTR'             , 'CODE'             ,
'DATA'             , 'DB'               , 'DIS'              , 'DIVQ'             ,
'DIVS'             , 'DM'               , 'DMPG1'            , 'DMPG2'            ,
'D0'               , 'DW'               , 'DX'               , 'E_MODE'           ,
'EMUIDLE'          , 'ENA'              , 'ENDINCLUDE'       , 'ENDMACRO'         ,
'EQ'               , 'ETRAPEXP'         , 'EXPADJ'           , 'FL0'              ,
'FL1'              , 'FL2'              , 'FLAG_OUT'         , 'FLUSH'            ,
'FOREVER'          , 'GE'               , 'GT'               , 'HI'               ,
'HIX'              , 'I0'               , 'I1'               , 'I2'               ,
'I3'               , 'I4'               , 'I5'               , 'I6'               ,
'I7'               , 'INCTL'            , 'IDLE'             , 'IF'               ,
'IJPG'             , 'IMASK'            , 'INCLUDE'          , 'INIT24'           ,
'INT'              , 'IO'               , 'IOPG'             , 'IRPTL'            ,
'JUMPKTRAP'        , 'L0'               , 'L1'               , 'L2'               ,
'L3'               , 'L4'               , 'L5'               , 'L6'               ,
'L7'               , 'LCALL'            , 'LE'               , 'LENGTH'           ,
'LINE'             , 'LJUMPLO'          , 'LOOP'             , 'LPSTACKA'         ,
'LPSTACKP'         , 'LSHIFT'           , 'LT'               , 'M0'               ,
'M1'               , 'M2'               , 'M3'               , 'M4'               ,
'M5'               , 'M6'               , 'M7'               , 'M_MODE'           ,
'MACRO'            , 'MF'               , 'MM'               , 'MODIFY'           ,
'MR'               , 'MR0'              , 'MR1'              , 'MR2'              ,
'MSTAT'            , 'MV'               , 'MXO'              , 'MX1'              ,
'MYO'              , 'MY1'              , 'NE'               , 'NEG'              ,
'NONE'             , 'NOPNORM'          , 'NOT'              , 'OF'               ,
'OFFSETOF'         , 'OL'               , 'OR'               , 'PAGE'             ,
'PAGEID'           , 'PASS'             , 'PC'               , 'PM'               ,
'PMCODE'           , 'PMDATA'           , 'POP'              , 'POS'              ,
'PUSH'             , 'PX'               , 'RAM'              , 'REG'              ,
'RESET'            , 'RND'              , 'ROM'              , 'RTI'              ,
'RTS'              , 'SAT'              , 'SB'               , 'SD'               ,
'SE'               , 'SEC_DAG'          , 'SEC_REG'          , 'SEG'              ,
'SET'              , 'SETBIT'           , 'SETINT'           , 'SHIFT'            ,
'SHT_DEBUGINFO'    , 'SHT_DM'           , 'SHT_DYNAMIC'      , 'SHT_DYNSYM'       ,
'SH_HASH'          , 'SHT_LDF'          , 'SHT_NOBITS'       , 'SHT_NOTE'         ,
'SHT_NULL'         , 'SHT_PMCODE'       , 'SHT_PMDATA'       , 'SHT_PROCESSORTYPE',
'SHT_PROGBITS'     , 'SHT_REL'          , 'SHT_RELA'         , 'SHT_SEGMENTINFO'  ,
'SHT_SHLIB'        , 'SHT_STRTAB'       , 'SHT_SYMTAB'       , 'SI'               ,
'SIMIDLE'          , 'SIZEOF'           , 'SR'               , 'SR0'              ,
'SR1'              , 'SR2'              , 'SS'               , 'SSTAT'            ,
'STACKA'           , 'STACKPSTATIC'     , 'STEP'             , 'STRUCT'           ,
'STS'              , 'STT_FUNC'         , 'STT_OBJECT'       , 'SU'               ,
'SV'               , 'SWCOND'           , 'SYSCTL'           , 'TGLBIT'           ,
'TI'               , 'TIMER'            , 'TOGGLE'           , 'TRAP'             ,
'TRUE'             , 'TSTBIT'           , 'TX0'              , 'TX1'              ,
'UNTIL'            , 'US'               , 'UU'               , 'XOR'              ,
'WAIT'             , 'WARNING'          , 'WRITE'            , 'WEAK'             ,
'XOR'
]
