#!/usr/bin/env python3

import os
import binascii
import hashlib
import time

try:
  os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
  from pygame import mixer

  mixer.init()
  mixer.music.load("music.mp3")
  mixer.music.play()
except: pass

week_hexs = {
  1: 'b2052cb0',
  2: 'f3079e83',
  3: 'dd729ced',
  4: 'ec5169fe',
  5: 'c7a4eff5',
  6: 'b008fa89',
  7: '077e8c3d',
  8: 'beebe3b0',
  9: '20d24c88',
  10: 'e3c147d3',
  11: 'c47bd741',
  12: '54141185',
}

def md5(text):
  return hashlib.md5(text.encode()).hexdigest()

print('''            
                                                                      
  ,----..    ,----..        ,----,     ,----..                        
 /   /   \  /   /   \     .'   .' \   /   /   \                       
|   :     :|   :     :  ,----,'    | /   .     :                      
.   |  ;. /.   |  ;. /  |    :  .  ;.   /   ;.  \                     
.   ; /--` .   ; /--`   ;    |.'  /.   ;   /  ` ;                     
;   | ;    ;   | ;      `----'/  ; ;   |  ; \ ; |                     
|   : |    |   : |        /  ;  /  |   :  | ; | '                     
.   | '___ .   | '___    ;  /  /-, .   |  ' ' ' :                     
'   ; : .'|'   ; : .'|  /  /  /.`| '   ;  \; /  |                     
'   | '/  :'   | '/  :./__;      :  \   \  ',  /                      
|   :    / |   :    / |   :    .'    ;   :    /                       
 \   \ .'   \   \ .'  ;   | .'        \   \ .'                        
  `---`,--.  `---`    `---'            `---`                     ,--. 
   ,--/  /|    ,---,.               ,----..       ,---,.       ,--.'| 
,---,': / '  ,'  .' |        ,---, /   /   \    ,'  .' |   ,--,:  : | 
:   : '/ / ,---.'   |       /_ ./||   :     : ,---.'   |,`--.'`|  ' : 
|   '   ,  |   |   .' ,---, |  ' :.   |  ;. / |   |   .'|   :  :  | | 
'   |  /   :   :  |-,/___/ \.  : |.   ; /--`  :   :  |-,:   |   \ | : 
|   ;  ;   :   |  ;/| .  \  \ ,' ';   | ;  __ :   |  ;/||   : '  '; | 
:   '   \  |   :   .'  \  ;  `  ,'|   : |.' .'|   :   .''   ' ;.    ; 
|   |    ' |   |  |-,   \  \    ' .   | '_.' :|   |  |-,|   | | \   | 
'   : |.  \'   :  ;/|    '  \   | '   ; : \  |'   :  ;/|'   : |  ; .' 
|   | '_\.'|   |    \     \  ;  ; '   | '/  .'|   |    \|   | '`--'   
'   : |    |   :   .'      :  \  \|   :    /  |   :   .''   : |       
;   |,'    |   | ,'         \  ' ; \   \ .'   |   | ,'  ;   |.'       
'---'      `----'            `--`   `---`     `----'    '---'         
                                                                      
''')

while True:
  print("Week: ", end="")
  week = input()

  try:
    first_hex = week_hexs[int(week)]
  except:
    print('Week not found')
    continue

  timestamp = int(time.time())

  time_hash = hex(timestamp)[2:]

  last_hex = binascii.b2a_hex(os.urandom(4)).decode()

  result = 'CCIT{' + first_hex + time_hash + last_hex + '}'
  print('Flag:', result)
