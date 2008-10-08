#cs ----------------------------------------------------------------------------
Bot Version: v 2.34
Script Function:
Dieser Bot angelt automatisch für euch, schlachtet Fische, relogt und teleportiert sich wieder ins Wasser.
Mit zusätzlich Roll-Back Funktion.
Momentan existieren noch ca. 2 Bugs.

#ce ----------------------------------------------------------------------------
HotKeySet ( "{F5}" , "Start" ) ; Der Taste Numpad7 ist nun die Info Start hinzugefügt
HotKeySet ( "{F6}" , "Ende" ) ; Der Taste Numpad8 ist nun die Info Ende hinzugefügt
Opt('PixelCoordMode', 2) ; falls window als option gewählt wurde
Opt('MouseCoordMode', 2) ; falls window als option gewählt wurde
While (1) ; Endlosschleife anfang und 1 für an
Sleep (1000) ; Überprüft jetzt jede Sekunde ob die oben genannten Tasten/Infos gedrückt worden sind
Wend ; Endlosschleife ende
Func Start () ; Das Zeil für die Info Start
While (1) ; die vorher vergessene while funktion sry xD


Sleep (100)

If PixelGetColor (538, 579) = 0x005CA6 Then
MouseClick ( "", 477, 272)
Sleep (500)
MouseClick ( "", 522, 486)
Sleep (500)
Send("lucky709")
Sleep (800)
Mouseclick ("",603, 494)
Sleep (1000)
Send ( "53fcfa7")
Sleep (800)
Mouseclick ("", 590, 519)
Sleep (20000)
If PixelGetColor (402, 323) = 0xC7C7C7 Then
MouseClick ("", 402,323)
Sleep (800)
Mouseclick ("", 590, 519)
Sleep (20000)
EndIf
If PixelGetColor (402, 323) = 0xC7C7C7 Then
MouseClick ("", 402,323)
Sleep (800)
Mouseclick ("", 590, 519)
Sleep (20000)
EndIf
Sleep (1000)
If PixelGetColor (402, 323) = 0xC7C7C7 Then
MouseClick ("", 402,323)
Sleep (800)
Mouseclick ("", 590, 519)
Sleep (20000)
EndIf
Sleep (1000)
If PixelGetColor (402, 323) = 0xC7C7C7 Then
MouseClick ("", 402,323
Sleep (800)
Mouseclick ("", 590, 519)
Sleep (20000)
EndIf
Sleep (1000)
If PixelGetColor (402, 323) = 0xC7C7C7 Then
MouseClick ("", 402,323)
Sleep (800)
Mouseclick ("", 590, 519)
Sleep (20000)
EndIf
Sleep (25000)
MouseClick ( "",468, 519)
Sleep (300)
MouseClick ( "",468, 519)
Sleep (300)
MouseClick ("" ,170, 477)
Sleep (60000)
Mouseclick ("" ,415, 280)
Sleep (1000)
Send ( " {w down} " )
Sleep (2000)
Send ( " {F7} " )
Sleep (1000)
Send ( " {w up} " )
Sleep (1000)
Send ( " {w up} " )
Sleep (1000)
Send ( " {r down} " )
Sleep (200)
Send ( " {g down} " )
Sleep (2000)
Send ( " {r up} " )
Sleep (100)
Send ( " {g up} " )
Sleep (1000)
Send ( " m " )
Sleep (500)
EndIf



Sleep (2000) ; Wartet 5 sekunden bis er anfängt
Send ( "{F3 down}" , 0 ) ; hält die Taste F3 runter
Sleep (500) ; hält die taste 0,5 Sekunden
Send ( "{F3 up}" , 0 ) ; lässt die Taste F3 wieder los
If PixelGetColor (693, 12) <>  0xD9D9D9 Then
 Send ( "i" )
EndIf
Sleep (1000)
If PixelGetColor (786, 271) = 0xFFFFFF Then; Nach dem Köder anmachen, stellt er die Köder auf die anderen, so dass man genug köder hat
Sleep (700)
MouseClick ("left",776, 260)
Sleep (700)
MouseClick ("left",776, 290)
Sleep (700)
EndIf 

If PixelGetColor (786, 303) = 0xFFFFFF Then; Nach dem Köder anmachen, stellt er die Köder auf die anderen, so dass man genug köder hat
Sleep (700)
MouseClick ("left",776, 290)
Sleep (700)
MouseClick ("left",776, 322)
Sleep (700)
EndIf
If PixelGetColor (786, 335) = 0xFFFFFF Then
MouseClick ("left",776, 322)
Sleep (700)
MouseClick ("left",776, 364)
Sleep (700)
EndIf
If PixelGetColor ( 786, 367) = 0xFFFFFF Then
MouseClick ("left",776, 364)
Sleep (700)
MouseClick ("left",780, 399)
EndIf
 
 
Sleep (700)
 
If Pixelgetcolor (648 , 259) = 0xFFFFE6 Then MouseClick ("Right",648 , 259) ;zander öffnen
If Pixelgetcolor (648 , 259) = 0x7E6B38 Then MouseClick ("Right",648 , 259) ;mandarin öffnen
If Pixelgetcolor (648, 259) = 0xC89899 Then MouseClick ("Right",648 , 259) ;karpfen öffnen
If Pixelgetcolor (648, 259) = 0xA0966B Then MouseClick ("Right",648 , 259) ;graskarpfen öffnen
If Pixelgetcolor (648, 259) = 0x4B4B4C Then MouseClick ("Right",648 , 259) ;bachforelle öffnen
If Pixelgetcolor (648, 259) = 0x625A71 Then MouseClick ("Right",648 , 259) ;katzenfisch öffnen
If Pixelgetcolor (648 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 259) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 259) = 0xFFFFE6 Then MouseClick ("Right",680 , 259) ;zander öffnen
If Pixelgetcolor (680 , 259) = 0x7E6B38 Then MouseClick ("Right",680 , 259) ;mandarin öffnen
If Pixelgetcolor (680, 259) = 0xC89899 Then MouseClick ("Right",680 , 259) ;karpfen öffnen
If Pixelgetcolor (680, 259) = 0xA0966B Then MouseClick ("Right",680 , 259) ;graskarpfen öffnen
If Pixelgetcolor (680, 259) = 0x4B4B4C Then MouseClick ("Right",680 , 259) ;bachforelle öffnen
If Pixelgetcolor (680, 259) = 0x625A71 Then MouseClick ("Right",680 , 259) ;katzenfisch öffnen
If Pixelgetcolor (680 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 259) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 259) = 0xFFFFE6 Then MouseClick ("Right",712 , 259) ;zander öffnen
If Pixelgetcolor (712 , 259) = 0x7E6B38 Then MouseClick ("Right",712 , 259) ;mandarin öffnen
If Pixelgetcolor (712, 259) = 0xC89899 Then MouseClick ("Right",712 , 259) ;karpfen öffnen
If Pixelgetcolor (712, 259) = 0xA0966B Then MouseClick ("Right",712 , 259) ;graskarpfen öffnen
If Pixelgetcolor (712, 259) = 0x4B4B4C Then MouseClick ("Right",712 , 259) ;bachforelle öffnen
If Pixelgetcolor (712, 259) = 0x625A71 Then MouseClick ("Right",712 , 259) ;katzenfisch öffnen
If Pixelgetcolor (712 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 259) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 259) = 0xFFFFE6 Then MouseClick ("Right",744 , 259) ;zander öffnen
If Pixelgetcolor (744 , 259) = 0x7E6B38 Then MouseClick ("Right",744 , 259) ;mandarin öffnen
If Pixelgetcolor (744, 259) = 0xC89899 Then MouseClick ("Right",744 , 259) ;karpfen öffnen
If Pixelgetcolor (744, 259) = 0xA0966B Then MouseClick ("Right",744 , 259) ;graskarpfen öffnen
If Pixelgetcolor (744, 259) = 0x4B4B4C Then MouseClick ("Right",744 , 259) ;bachforelle öffnen
If Pixelgetcolor (744, 259) = 0x625A71 Then MouseClick ("Right",744 , 259) ;katzenfisch öffnen
If Pixelgetcolor (744 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744 , 259) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 , 259) = 0xFFFFE6 Then MouseClick ("Right",776 , 259) ;zander öffnen
If Pixelgetcolor (776 , 259) = 0x7E6B38 Then MouseClick ("Right",776 , 259) ;mandarin öffnen
If Pixelgetcolor (776, 259) = 0xC89899 Then MouseClick ("Right",766 , 259) ;karpfen öffnen
If Pixelgetcolor (766, 259) = 0xA0966B Then MouseClick ("Right",766 , 259) ;graskarpfen öffnen
If Pixelgetcolor (776, 259) = 0x4B4B4C Then MouseClick ("Right",766 , 259) ;bachforelle öffnen
If Pixelgetcolor (766, 259) = 0x625A71 Then MouseClick ("Right",766 , 259) ;katzenfisch öffnen
If Pixelgetcolor (776 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776 , 259) ;linksklick auf kl. fisch
EndIf
 
 
Sleep (100) ; 2. REIHE
 
 

If Pixelgetcolor (648 , 291) = 0xFFFFE6 Then MouseClick ("Right",648 , 291) ;zander öffnen
If Pixelgetcolor (648 , 291) = 0x7E6B38 Then MouseClick ("Right",648 , 291) ;mandarin öffnen
If Pixelgetcolor (648, 291) = 0xC89899 Then MouseClick ("Right",648 , 291) ;karpfen öffnen
If Pixelgetcolor (648, 291) = 0xA0966B Then MouseClick ("Right",648 , 291) ;graskarpfen öffnen
If Pixelgetcolor (648, 291) = 0x4B4B4C Then MouseClick ("Right",648 , 291) ;bachforelle öffnen
If Pixelgetcolor (648, 291) = 0x625A71 Then MouseClick ("Right",648 , 291) ;katzenfisch öffnen
If Pixelgetcolor (648 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 291) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 291) = 0xFFFFE6 Then MouseClick ("Right",680 , 291) ;zander öffnen
If Pixelgetcolor (680 , 291) = 0x7E6B38 Then MouseClick ("Right",680 , 291) ;mandarin
If Pixelgetcolor (680, 291) = 0xC89899 Then MouseClick ("Right",680 , 291) ;karpfen öffnen
If Pixelgetcolor (680, 291) = 0xA0966B Then MouseClick ("Right",680 , 291) ;graskarpfen öffnen
If Pixelgetcolor (680, 291) = 0x4B4B4C Then MouseClick ("Right",680 , 291) ;bachforelle öffnen
If Pixelgetcolor (680, 291) = 0x625A71 Then MouseClick ("Right",680 , 291) ;katzenfisch öffnen
If Pixelgetcolor (680 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 291) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 291) = 0xFFFFE6 Then MouseClick ("Right",712 , 291) ;zander öffnen
If Pixelgetcolor (712 , 291) = 0x7E6B38 Then MouseClick ("Right",712 , 291) ;mandarin
If Pixelgetcolor (712, 291) = 0xC89899 Then MouseClick ("Right",712 , 291) ;karpfen öffnen
If Pixelgetcolor (712, 291) = 0xA0966B Then MouseClick ("Right",712 , 291) ;graskarpfen öffnen
If Pixelgetcolor (712, 291) = 0x4B4B4C Then MouseClick ("Right",712 , 291) ;bachforelle öffnen
If Pixelgetcolor (712, 291) = 0x625A71 Then MouseClick ("Right",712 , 291) ;katzenfisch öffnen
If Pixelgetcolor (712 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 291) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 291) = 0xFFFFE6 Then MouseClick ("Right",744 , 291) ;zander öffnen
If Pixelgetcolor (744 , 291) = 0x7E6B38 Then MouseClick ("Right",744 , 291) ;mandarin
If Pixelgetcolor (744, 291) = 0xC89899 Then MouseClick ("Right",744 , 291) ;karpfen öffnen
If Pixelgetcolor (744, 291) = 0xA0966B Then MouseClick ("Right",744 , 291) ;graskarpfen öffnen
If Pixelgetcolor (744, 291) = 0x4B4B4C Then MouseClick ("Right",744 , 291) ;bachforelle öffnen
If Pixelgetcolor (744, 291) = 0x625A71 Then MouseClick ("Right",744 , 291) ;katzenfisch öffnen
If Pixelgetcolor (744 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744 , 291) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 , 291) = 0xFFFFE6 Then MouseClick ("Right",776 , 291) ;zander öffnen
If Pixelgetcolor (776 , 291) = 0x7E6B38 Then MouseClick ("Right",776 , 291) ;mandarin
If Pixelgetcolor (776, 291) = 0xC89899 Then MouseClick ("Right",766 , 291) ;karpfen öffnen
If Pixelgetcolor (766, 291) = 0xA0966B Then MouseClick ("Right",766 , 291) ;graskarpfen öffnen
If Pixelgetcolor (776, 291) = 0x4B4B4C Then MouseClick ("Right",766 , 291) ;bachforelle öffnen
If Pixelgetcolor (766, 291) = 0x625A71 Then MouseClick ("Right",766 , 291) ;katzenfisch öffnen
If Pixelgetcolor (776 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776 , 291) ;linksklick auf kl. fisch
EndIf
 
 
Sleep (100) ; 3. REIHE
 
 
If Pixelgetcolor (648 , 323) = 0xFFFFE6 Then MouseClick ("Right",648 , 323) ;zander öffnen
If Pixelgetcolor (648 , 323) = 0x7E6B38 Then MouseClick ("Right",648 , 323) ;mandarin öffnen
If Pixelgetcolor (648, 323) = 0xC89899 Then MouseClick ("Right",648 , 323) ;karpfen öffnen
If Pixelgetcolor (648, 323) = 0xA0966B Then MouseClick ("Right",648 , 323) ;graskarpfen öffnen
If Pixelgetcolor (648, 323) = 0x4B4B4C Then MouseClick ("Right",648 , 323) ;bachforelle öffnen
If Pixelgetcolor (648, 323) = 0x625A71 Then MouseClick ("Right",648 , 323) ;katzenfisch öffnen
If Pixelgetcolor (648 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 323) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 323) = 0xFFFFE6 Then MouseClick ("Right",680 , 323) ;zander öffnen
If Pixelgetcolor (680 , 323) = 0x7E6B38 Then MouseClick ("Right",680 , 323) ;mandarin
If Pixelgetcolor (680, 323) = 0xC89899 Then MouseClick ("Right",680 , 323) ;karpfen öffnen
If Pixelgetcolor (680, 323) = 0xA0966B Then MouseClick ("Right",680 , 323) ;graskarpfen öffnen
If Pixelgetcolor (680, 323) = 0x4B4B4C Then MouseClick ("Right",680 , 323) ;bachforelle öffnen
If Pixelgetcolor (680, 323) = 0x625A71 Then MouseClick ("Right",680 , 323) ;katzenfisch öffnen
If Pixelgetcolor (680 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 323) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 323) = 0xFFFFE6 Then MouseClick ("Right",712 , 323) ;zander öffnen
If Pixelgetcolor (712 , 323) = 0x7E6B38 Then MouseClick ("Right",712 , 323) ;mandarin
If Pixelgetcolor (712, 323) = 0xC89899 Then MouseClick ("Right",712 , 323) ;karpfen öffnen
If Pixelgetcolor (712, 323) = 0xA0966B Then MouseClick ("Right",712 , 323) ;graskarpfen öffnen
If Pixelgetcolor (712, 323) = 0x4B4B4C Then MouseClick ("Right",712 , 323) ;bachforelle öffnen
If Pixelgetcolor (712, 323) = 0x625A71 Then MouseClick ("Right",712 , 323) ;katzenfisch öffnen
If Pixelgetcolor (712 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 323) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 323 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 323) ;zander öffnen
If Pixelgetcolor (744 , 323) = 0x7E6B38 Then MouseClick ("Right",744 , 323) ;mandarin
If Pixelgetcolor (744, 323) = 0xC89899 Then MouseClick ("Right",744 , 323) ;karpfen öffnen
If Pixelgetcolor (744, 323) = 0xA0966B Then MouseClick ("Right",744 , 323) ;graskarpfen öffnen
If Pixelgetcolor (744, 323) = 0x4B4B4C Then MouseClick ("Right",744 , 323) ;bachforelle öffnen
If Pixelgetcolor (744, 323) = 0x625A71 Then MouseClick ("Right",744 , 323) ;katzenfisch öffnen
If Pixelgetcolor (744 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744 , 323) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 ,323) = 0xFFFFE6 Then MouseClick ("Right",776 , 323) ;zander öffnen
If Pixelgetcolor (776 , 323) = 0x7E6B38 Then MouseClick ("Right",776 , 323) ;mandarin
If Pixelgetcolor (776, 323) = 0xC89899 Then MouseClick ("Right",776 , 323) ;karpfen öffnen
If Pixelgetcolor (776, 323) = 0xA0966B Then MouseClick ("Right",776 , 323) ;graskarpfen öffnen
If Pixelgetcolor (776, 323) = 0x4B4B4C Then MouseClick ("Right",776 , 323) ;bachforelle öffnen
If Pixelgetcolor (776, 323) = 0x625A71 Then MouseClick ("Right",776 , 323) ;katzenfisch öffnen
If Pixelgetcolor (776 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776 , 323) ;linksklick auf kl. fisch
EndIf
 

Sleep (100) ; 4. REIHE
 

If Pixelgetcolor (648 , 355) = 0xFFFFE6 Then MouseClick ("Right",648 , 355) ;zander öffnen
If Pixelgetcolor (648 , 355) = 0x7E6B38 Then MouseClick ("Right",648 , 355) ;mandarin öffnen
If Pixelgetcolor (648, 355) = 0xC89899 Then MouseClick ("Right",648 , 355) ;karpfen öffnen
If Pixelgetcolor (648, 355) = 0xA0966B Then MouseClick ("Right",648 , 355) ;graskarpfen öffnen
If Pixelgetcolor (648, 355) = 0x4B4B4C Then MouseClick ("Right",648 , 355) ;bachforelle öffnen
If Pixelgetcolor (648, 355) = 0x625A71 Then MouseClick ("Right",648 , 355) ;katzenfisch öffnen
If Pixelgetcolor (648 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 355) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 355) = 0xFFFFE6 Then MouseClick ("Right",680 , 355) ;zander öffnen
If Pixelgetcolor (680 , 355) = 0x7E6B38 Then MouseClick ("Right",680 , 355) ;mandarin
If Pixelgetcolor (680, 355) = 0xC89899 Then MouseClick ("Right",680 , 355) ;karpfen öffnen
If Pixelgetcolor (680, 355) = 0xA0966B Then MouseClick ("Right",680 , 355) ;graskarpfen öffnen
If Pixelgetcolor (680, 355) = 0x4B4B4C Then MouseClick ("Right",680 , 355) ;bachforelle öffnen
If Pixelgetcolor (680, 355) = 0x625A71 Then MouseClick ("Right",680 , 355) ;katzenfisch öffnen
If Pixelgetcolor (680 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 355) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 355) = 0xFFFFE6 Then MouseClick ("Right",712 , 355) ;zander öffnen
If Pixelgetcolor (712 , 355) = 0x7E6B38 Then MouseClick ("Right",712 , 355) ;mandarin
If Pixelgetcolor (712, 355) = 0xC89899 Then MouseClick ("Right",712 , 355) ;karpfen öffnen
If Pixelgetcolor (712, 355) = 0xA0966B Then MouseClick ("Right",712 , 355) ;graskarpfen öffnen
If Pixelgetcolor (712, 355) = 0x4B4B4C Then MouseClick ("Right",712 , 355) ;bachforelle öffnen
If Pixelgetcolor (712, 355) = 0x625A71 Then MouseClick ("Right",712 , 355) ;katzenfisch öffnen
If Pixelgetcolor (712 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 355) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 355 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 355) ;zander öffnen
If Pixelgetcolor (744 , 355) = 0x7E6B38 Then MouseClick ("Right",744 , 355) ;mandarin
If Pixelgetcolor (744, 355) = 0xC89899 Then MouseClick ("Right",744 , 355) ;karpfen öffnen
If Pixelgetcolor (744, 355) = 0xA0966B Then MouseClick ("Right",744 , 355) ;graskarpfen öffnen
If Pixelgetcolor (744, 355) = 0x4B4B4C Then MouseClick ("Right",744 , 355) ;bachforelle öffnen
If Pixelgetcolor (744, 355) = 0x625A71 Then MouseClick ("Right",744 , 355 );katzenfisch öffnen
If Pixelgetcolor (744 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744 , 355) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 ,355) = 0xFFFFE6 Then MouseClick ("Right",776 , 355) ;zander öffnen
If Pixelgetcolor (776 , 355) = 0x7E6B38 Then MouseClick ("Right",776 , 355) ;mandarin
If Pixelgetcolor (776, 355) = 0xC89899 Then MouseClick ("Right",776 , 355) ;karpfen öffnen
If Pixelgetcolor (776, 355) = 0xA0966B Then MouseClick ("Right",776 , 355) ;graskarpfen öffnen
If Pixelgetcolor (776, 355) = 0x4B4B4C Then MouseClick ("Right",776 , 355) ;bachforelle öffnen
If Pixelgetcolor (776, 355) = 0x625A71 Then MouseClick ("Right",776 , 355) ;katzenfisch öffnen
If Pixelgetcolor (776 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776 , 355) ;linksklick auf kl. fisch
EndIf
 
 
Sleep (100) ; 5. REIHE
 
 
If Pixelgetcolor (648 , 387) = 0xFFFFE6 Then MouseClick ("Right",648 , 387) ;zander öffnen
If Pixelgetcolor (648 , 387) = 0x7E6B38 Then MouseClick ("Right",648 , 387) ;mandarin öffnen
If Pixelgetcolor (648, 387) = 0xC89899 Then MouseClick ("Right",648 , 387) ;karpfen öffnen
If Pixelgetcolor (648, 387) = 0xA0966B Then MouseClick ("Right",648 , 387) ;graskarpfen öffnen
If Pixelgetcolor (648, 387) = 0x4B4B4C Then MouseClick ("Right",648 , 387) ;bachforelle öffnen
If Pixelgetcolor (648, 387) = 0x625A71 Then MouseClick ("Right",648 , 387) ;katzenfisch öffnen
If Pixelgetcolor (648 , 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 387) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 387) = 0xFFFFE6 Then MouseClick ("Right",680 , 387) ;zander öffnen
If Pixelgetcolor (680 , 387) = 0x7E6B38 Then MouseClick ("Right",680 , 387) ;mandarin
If Pixelgetcolor (680, 387) = 0xC89899 Then MouseClick ("Right",680 , 387) ;karpfen öffnen
If Pixelgetcolor (680, 387) = 0xA0966B Then MouseClick ("Right",680 , 387) ;graskarpfen öffnen
If Pixelgetcolor (680, 387) = 0x4B4B4C Then MouseClick ("Right",680 , 387) ;bachforelle öffnen
If Pixelgetcolor (680, 387) = 0x625A71 Then MouseClick ("Right",680 , 387) ;katzenfisch öffnen
If Pixelgetcolor (680, 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 387) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 387) = 0xFFFFE6 Then MouseClick ("Right",712 , 387) ;zander öffnen
If Pixelgetcolor (712 , 387) = 0x7E6B38 Then MouseClick ("Right",712 , 387) ;mandarin
If Pixelgetcolor (712, 387) = 0xC89899 Then MouseClick ("Right",712 , 387) ;karpfen öffnen
If Pixelgetcolor (712, 387) = 0xA0966B Then MouseClick ("Right",712 , 387) ;graskarpfen öffnen
If Pixelgetcolor (712, 387) = 0x4B4B4C Then MouseClick ("Right",712 , 387) ;bachforelle öffnen
If Pixelgetcolor (712, 387) = 0x625A71 Then MouseClick ("Right",712 , 387) ;katzenfisch öffnen
If Pixelgetcolor (712, 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 387) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 387 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 387) ;zander öffnen
If Pixelgetcolor (744 , 387) = 0x7E6B38 Then MouseClick ("Right",744 , 387) ;mandarin
If Pixelgetcolor (744, 387) = 0xC89899 Then MouseClick ("Right",744 , 387) ;karpfen öffnen
If Pixelgetcolor (744, 387) = 0xA0966B Then MouseClick ("Right",744 , 387) ;graskarpfen öffnen
If Pixelgetcolor (744, 387) = 0x4B4B4C Then MouseClick ("Right",744 , 387) ;bachforelle öffnen
If Pixelgetcolor (744, 387) = 0x625A71 Then MouseClick ("Right",744 , 387) ;katzenfisch öffnen
If Pixelgetcolor (744, 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744, 387) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 ,387) = 0xFFFFE6 Then MouseClick ("Right",776 , 387) ;zander öffnen
If Pixelgetcolor (776 , 387) = 0x7E6B38 Then MouseClick ("Right",776 , 387) ;mandarin
If Pixelgetcolor (776, 387) = 0xC89899 Then MouseClick ("Right",776 , 387) ;karpfen öffnen
If Pixelgetcolor (776, 387) = 0xA0966B Then MouseClick ("Right",776 , 387) ;graskarpfen öffnen
If Pixelgetcolor (776, 387) = 0x4B4B4C Then MouseClick ("Right",776 , 387) ;bachforelle öffnen
If Pixelgetcolor (776, 387) = 0x625A71 Then MouseClick ("Right",776 , 387) ;katzenfisch öffnen
If Pixelgetcolor (776, 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776, 387) ;linksklick auf kl. fisch
EndIf
 

Sleep (100) ; 6. REIHE 

If Pixelgetcolor (648 , 419) = 0xFFFFE6 Then MouseClick ("Right",648 , 419) ;zander öffnen
If Pixelgetcolor (648 , 419) = 0x7E6B38 Then MouseClick ("Right",648 , 419) ;mandarin öffnen
If Pixelgetcolor (648, 419) = 0xC89899 Then MouseClick ("Right",648 , 419) ;karpfen öffnen
If Pixelgetcolor (648, 419) = 0xA0966B Then MouseClick ("Right",648 , 419) ;graskarpfen öffnen
If Pixelgetcolor (648, 419) = 0x4B4B4C Then MouseClick ("Right",648 , 419) ;bachforelle öffnen
If Pixelgetcolor (648, 419) = 0x625A71 Then MouseClick ("Right",648 , 419) ;katzenfisch öffnen
If Pixelgetcolor (648, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648, 419) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 419) = 0xFFFFE6 Then MouseClick ("Right",680 , 419) ;zander öffnen
If Pixelgetcolor (680 , 419) = 0x7E6B38 Then MouseClick ("Right",680 , 419) ;mandarin
If Pixelgetcolor (648, 419) = 0xC89899 Then MouseClick ("Right",648 , 419) ;karpfen öffnen
If Pixelgetcolor (648, 419) = 0xA0966B Then MouseClick ("Right",648 , 419) ;graskarpfen öffnen
If Pixelgetcolor (648, 419) = 0x4B4B4C Then MouseClick ("Right",648 , 419) ;bachforelle öffnen
If Pixelgetcolor (648, 419) = 0x625A71 Then MouseClick ("Right",648 , 419) ;katzenfisch öffnen
If Pixelgetcolor (648, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648, 419) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 419) = 0xFFFFE6 Then MouseClick ("Right",712 , 419) ;zander öffnen
If Pixelgetcolor (712 , 419) = 0x7E6B38 Then MouseClick ("Right",712 , 419) ;mandarin
If Pixelgetcolor (712, 419) = 0xC89899 Then MouseClick ("Right",712 , 419) ;karpfen öffnen
If Pixelgetcolor (712, 419) = 0xA0966B Then MouseClick ("Right",712 , 419) ;graskarpfen öffnen
If Pixelgetcolor (712, 419) = 0x4B4B4C Then MouseClick ("Right",712 , 419) ;bachforelle öffnen
If Pixelgetcolor (712, 419) = 0x625A71 Then MouseClick ("Right",712 , 419) ;katzenfisch öffnen
If Pixelgetcolor (712, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712, 419) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 419 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 419) ;zander öffnen
If Pixelgetcolor (744 , 419) = 0x7E6B38 Then MouseClick ("Right",744 , 419) ;mandarin
If Pixelgetcolor (744, 419) = 0xC89899 Then MouseClick ("Right",744 , 419) ;karpfen öffnen
If Pixelgetcolor (744, 419) = 0xA0966B Then MouseClick ("Right",744 , 419) ;graskarpfen öffnen
If Pixelgetcolor (744, 419) = 0x4B4B4C Then MouseClick ("Right",744 , 419) ;bachforelle öffnen
If Pixelgetcolor (744, 419) = 0x625A71 Then MouseClick ("Right",744 , 419) ;katzenfisch öffnen
If Pixelgetcolor (744, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744, 419) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 ,419) = 0xFFFFE6 Then MouseClick ("Right",776 , 419) ;zander öffnen
If Pixelgetcolor (776 , 419) = 0x7E6B38 Then MouseClick ("Right",776 , 419) ;mandarin
If Pixelgetcolor (776, 419) = 0xC89899 Then MouseClick ("Right",776 , 419) ;karpfen öffnen
If Pixelgetcolor (776, 419) = 0xA0966B Then MouseClick ("Right",776 , 419) ;graskarpfen öffnen
If Pixelgetcolor (776, 419) = 0x4B4B4C Then MouseClick ("Right",776 , 419) ;bachforelle öffnen
If Pixelgetcolor (776, 419) = 0x625A71 Then MouseClick ("Right",776 , 419) ;katzenfisch öffnen
If Pixelgetcolor (776, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776, 419) ;linksklick auf kl. fisch
EndIf
 
Sleep (100) ; 7. REIHE
 
 
If Pixelgetcolor (648 , 451) = 0xFFFFE6 Then MouseClick ("Right",648 , 451) ;zander öffnen
If Pixelgetcolor (648 , 451) = 0x7E6B38 Then MouseClick ("Right",648 , 451) ;mandarin öffnen
If Pixelgetcolor (648 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",648 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (680 , 451) = 0xFFFFE6 Then MouseClick ("Right",680 , 451) ;zander öffnen
If Pixelgetcolor (680 , 451) = 0x7E6B38 Then MouseClick ("Right",680 , 451) ;mandarin
If Pixelgetcolor (680 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",680 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (712 , 451) = 0xFFFFE6 Then MouseClick ("Right",712 , 451) ;zander öffnen
If Pixelgetcolor (712 , 451) = 0x7E6B38 Then MouseClick ("Right",712 , 451) ;mandarin
If Pixelgetcolor (712 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",712 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (744 , 451 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 451) ;zander öffnen
If Pixelgetcolor (744 , 451) = 0x7E6B38 Then MouseClick ("Right",744 , 451) ;mandarin
If Pixelgetcolor (744 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",744 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (776 ,451) = 0xFFFFE6 Then MouseClick ("Right",776 , 451) ;zander öffnen
If Pixelgetcolor (776 , 451) = 0x7E6B38 Then MouseClick ("Right",776 , 451) ;mandarin
If Pixelgetcolor (776 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",776 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
 
Sleep (100) ; 8. REIHE
 
 
If Pixelgetcolor (648 , 483) = 0xFFFFE6 Then MouseClick ("Right",648 , 483) ;zander öffnen
If Pixelgetcolor (648 , 483) = 0x7E6B38 Then MouseClick ("Right",648 , 483) ;mandarin öffnen
If Pixelgetcolor (648 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",648 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (680 , 483) = 0xFFFFE6 Then MouseClick ("Right",680 , 483) ;zander öffnen
If Pixelgetcolor (680 , 483) = 0x7E6B38 Then MouseClick ("Right",680 , 483) ;mandarin
If Pixelgetcolor (680 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",680 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (712 , 483) = 0xFFFFE6 Then MouseClick ("Right",712 , 483) ;zander öffnen
If Pixelgetcolor (712 , 483) = 0x7E6B38 Then MouseClick ("Right",712 , 483) ;mandarin
If Pixelgetcolor (712 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",712 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (744 , 483 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 483) ;zander öffnen
If Pixelgetcolor (744 , 483) = 0x7E6B38 Then MouseClick ("Right",744 , 483) ;mandarin
If Pixelgetcolor (744 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",744 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (776 ,483) = 0xFFFFE6 Then MouseClick ("Right",776 , 483) ;zander öffnen
If Pixelgetcolor (776 , 483) = 0x7E6B38 Then MouseClick ("Right",776 , 483) ;mandarin
If Pixelgetcolor (776 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",776 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
; ---------------------------------------------------------
 
 
 
MouseClick ("",752, 234)
 
 
 
If Pixelgetcolor (648 , 259) = 0xFFFFE6 Then MouseClick ("Right",648 , 259) ;zander öffnen
If Pixelgetcolor (648 , 259) = 0x7E6B38 Then MouseClick ("Right",648 , 259) ;mandarin öffnen
If Pixelgetcolor (648, 259) = 0xC89899 Then MouseClick ("Right",648 , 259) ;karpfen öffnen
If Pixelgetcolor (648, 259) = 0xA0966B Then MouseClick ("Right",648 , 259) ;graskarpfen öffnen
If Pixelgetcolor (648, 259) = 0x4B4B4C Then MouseClick ("Right",648 , 259) ;bachforelle öffnen
If Pixelgetcolor (648, 259) = 0x625A71 Then MouseClick ("Right",648 , 259) ;katzenfisch öffnen
If Pixelgetcolor (648 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 259) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 259) = 0xFFFFE6 Then MouseClick ("Right",680 , 259) ;zander öffnen
If Pixelgetcolor (680 , 259) = 0x7E6B38 Then MouseClick ("Right",680 , 259) ;mandarin öffnen
If Pixelgetcolor (680, 259) = 0xC89899 Then MouseClick ("Right",680 , 259) ;karpfen öffnen
If Pixelgetcolor (680, 259) = 0xA0966B Then MouseClick ("Right",680 , 259) ;graskarpfen öffnen
If Pixelgetcolor (680, 259) = 0x4B4B4C Then MouseClick ("Right",680 , 259) ;bachforelle öffnen
If Pixelgetcolor (680, 259) = 0x625A71 Then MouseClick ("Right",680 , 259) ;katzenfisch öffnen
If Pixelgetcolor (680 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 259) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 259) = 0xFFFFE6 Then MouseClick ("Right",712 , 259) ;zander öffnen
If Pixelgetcolor (712 , 259) = 0x7E6B38 Then MouseClick ("Right",712 , 259) ;mandarin öffnen
If Pixelgetcolor (712, 259) = 0xC89899 Then MouseClick ("Right",712 , 259) ;karpfen öffnen
If Pixelgetcolor (712, 259) = 0xA0966B Then MouseClick ("Right",712 , 259) ;graskarpfen öffnen
If Pixelgetcolor (712, 259) = 0x4B4B4C Then MouseClick ("Right",712 , 259) ;bachforelle öffnen
If Pixelgetcolor (712, 259) = 0x625A71 Then MouseClick ("Right",712 , 259) ;katzenfisch öffnen
If Pixelgetcolor (712 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 259) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 259) = 0xFFFFE6 Then MouseClick ("Right",744 , 259) ;zander öffnen
If Pixelgetcolor (744 , 259) = 0x7E6B38 Then MouseClick ("Right",744 , 259) ;mandarin öffnen
If Pixelgetcolor (744, 259) = 0xC89899 Then MouseClick ("Right",744 , 259) ;karpfen öffnen
If Pixelgetcolor (744, 259) = 0xA0966B Then MouseClick ("Right",744 , 259) ;graskarpfen öffnen
If Pixelgetcolor (744, 259) = 0x4B4B4C Then MouseClick ("Right",744 , 259) ;bachforelle öffnen
If Pixelgetcolor (744, 259) = 0x625A71 Then MouseClick ("Right",744 , 259) ;katzenfisch öffnen
If Pixelgetcolor (744 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744 , 259) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 , 259) = 0xFFFFE6 Then MouseClick ("Right",776 , 259) ;zander öffnen
If Pixelgetcolor (776 , 259) = 0x7E6B38 Then MouseClick ("Right",776 , 259) ;mandarin öffnen
If Pixelgetcolor (776, 259) = 0xC89899 Then MouseClick ("Right",766 , 259) ;karpfen öffnen
If Pixelgetcolor (766, 259) = 0xA0966B Then MouseClick ("Right",766 , 259) ;graskarpfen öffnen
If Pixelgetcolor (776, 259) = 0x4B4B4C Then MouseClick ("Right",766 , 259) ;bachforelle öffnen
If Pixelgetcolor (766, 259) = 0x625A71 Then MouseClick ("Right",766 , 259) ;katzenfisch öffnen
If Pixelgetcolor (776 , 259) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776 , 259) ;linksklick auf kl. fisch
EndIf
 
 
Sleep (100) ; 2. REIHE
 
 

If Pixelgetcolor (648 , 291) = 0xFFFFE6 Then MouseClick ("Right",648 , 291) ;zander öffnen
If Pixelgetcolor (648 , 291) = 0x7E6B38 Then MouseClick ("Right",648 , 291) ;mandarin öffnen
If Pixelgetcolor (648, 291) = 0xC89899 Then MouseClick ("Right",648 , 291) ;karpfen öffnen
If Pixelgetcolor (648, 291) = 0xA0966B Then MouseClick ("Right",648 , 291) ;graskarpfen öffnen
If Pixelgetcolor (648, 291) = 0x4B4B4C Then MouseClick ("Right",648 , 291) ;bachforelle öffnen
If Pixelgetcolor (648, 291) = 0x625A71 Then MouseClick ("Right",648 , 291) ;katzenfisch öffnen
If Pixelgetcolor (648 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 291) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 291) = 0xFFFFE6 Then MouseClick ("Right",680 , 291) ;zander öffnen
If Pixelgetcolor (680 , 291) = 0x7E6B38 Then MouseClick ("Right",680 , 291) ;mandarin
If Pixelgetcolor (680, 291) = 0xC89899 Then MouseClick ("Right",680 , 291) ;karpfen öffnen
If Pixelgetcolor (680, 291) = 0xA0966B Then MouseClick ("Right",680 , 291) ;graskarpfen öffnen
If Pixelgetcolor (680, 291) = 0x4B4B4C Then MouseClick ("Right",680 , 291) ;bachforelle öffnen
If Pixelgetcolor (680, 291) = 0x625A71 Then MouseClick ("Right",680 , 291) ;katzenfisch öffnen
If Pixelgetcolor (680 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 291) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 291) = 0xFFFFE6 Then MouseClick ("Right",712 , 291) ;zander öffnen
If Pixelgetcolor (712 , 291) = 0x7E6B38 Then MouseClick ("Right",712 , 291) ;mandarin
If Pixelgetcolor (712, 291) = 0xC89899 Then MouseClick ("Right",712 , 291) ;karpfen öffnen
If Pixelgetcolor (712, 291) = 0xA0966B Then MouseClick ("Right",712 , 291) ;graskarpfen öffnen
If Pixelgetcolor (712, 291) = 0x4B4B4C Then MouseClick ("Right",712 , 291) ;bachforelle öffnen
If Pixelgetcolor (712, 291) = 0x625A71 Then MouseClick ("Right",712 , 291) ;katzenfisch öffnen
If Pixelgetcolor (712 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 291) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 291) = 0xFFFFE6 Then MouseClick ("Right",744 , 291) ;zander öffnen
If Pixelgetcolor (744 , 291) = 0x7E6B38 Then MouseClick ("Right",744 , 291) ;mandarin
If Pixelgetcolor (744, 291) = 0xC89899 Then MouseClick ("Right",744 , 291) ;karpfen öffnen
If Pixelgetcolor (744, 291) = 0xA0966B Then MouseClick ("Right",744 , 291) ;graskarpfen öffnen
If Pixelgetcolor (744, 291) = 0x4B4B4C Then MouseClick ("Right",744 , 291) ;bachforelle öffnen
If Pixelgetcolor (744, 291) = 0x625A71 Then MouseClick ("Right",744 , 291) ;katzenfisch öffnen
If Pixelgetcolor (744 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744 , 291) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 , 291) = 0xFFFFE6 Then MouseClick ("Right",776 , 291) ;zander öffnen
If Pixelgetcolor (776 , 291) = 0x7E6B38 Then MouseClick ("Right",776 , 291) ;mandarin
If Pixelgetcolor (776, 291) = 0xC89899 Then MouseClick ("Right",766 , 291) ;karpfen öffnen
If Pixelgetcolor (766, 291) = 0xA0966B Then MouseClick ("Right",766 , 291) ;graskarpfen öffnen
If Pixelgetcolor (776, 291) = 0x4B4B4C Then MouseClick ("Right",766 , 291) ;bachforelle öffnen
If Pixelgetcolor (766, 291) = 0x625A71 Then MouseClick ("Right",766 , 291) ;katzenfisch öffnen
If Pixelgetcolor (776 , 291) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776 , 291) ;linksklick auf kl. fisch
EndIf
 
 
Sleep (100) ; 3. REIHE
 
 
If Pixelgetcolor (648 , 323) = 0xFFFFE6 Then MouseClick ("Right",648 , 323) ;zander öffnen
If Pixelgetcolor (648 , 323) = 0x7E6B38 Then MouseClick ("Right",648 , 323) ;mandarin öffnen
If Pixelgetcolor (648, 323) = 0xC89899 Then MouseClick ("Right",648 , 323) ;karpfen öffnen
If Pixelgetcolor (648, 323) = 0xA0966B Then MouseClick ("Right",648 , 323) ;graskarpfen öffnen
If Pixelgetcolor (648, 323) = 0x4B4B4C Then MouseClick ("Right",648 , 323) ;bachforelle öffnen
If Pixelgetcolor (648, 323) = 0x625A71 Then MouseClick ("Right",648 , 323) ;katzenfisch öffnen
If Pixelgetcolor (648 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 323) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 323) = 0xFFFFE6 Then MouseClick ("Right",680 , 323) ;zander öffnen
If Pixelgetcolor (680 , 323) = 0x7E6B38 Then MouseClick ("Right",680 , 323) ;mandarin
If Pixelgetcolor (680, 323) = 0xC89899 Then MouseClick ("Right",680 , 323) ;karpfen öffnen
If Pixelgetcolor (680, 323) = 0xA0966B Then MouseClick ("Right",680 , 323) ;graskarpfen öffnen
If Pixelgetcolor (680, 323) = 0x4B4B4C Then MouseClick ("Right",680 , 323) ;bachforelle öffnen
If Pixelgetcolor (680, 323) = 0x625A71 Then MouseClick ("Right",680 , 323) ;katzenfisch öffnen
If Pixelgetcolor (680 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 323) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 323) = 0xFFFFE6 Then MouseClick ("Right",712 , 323) ;zander öffnen
If Pixelgetcolor (712 , 323) = 0x7E6B38 Then MouseClick ("Right",712 , 323) ;mandarin
If Pixelgetcolor (712, 323) = 0xC89899 Then MouseClick ("Right",712 , 323) ;karpfen öffnen
If Pixelgetcolor (712, 323) = 0xA0966B Then MouseClick ("Right",712 , 323) ;graskarpfen öffnen
If Pixelgetcolor (712, 323) = 0x4B4B4C Then MouseClick ("Right",712 , 323) ;bachforelle öffnen
If Pixelgetcolor (712, 323) = 0x625A71 Then MouseClick ("Right",712 , 323) ;katzenfisch öffnen
If Pixelgetcolor (712 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 323) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 323 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 323) ;zander öffnen
If Pixelgetcolor (744 , 323) = 0x7E6B38 Then MouseClick ("Right",744 , 323) ;mandarin
If Pixelgetcolor (744, 323) = 0xC89899 Then MouseClick ("Right",744 , 323) ;karpfen öffnen
If Pixelgetcolor (744, 323) = 0xA0966B Then MouseClick ("Right",744 , 323) ;graskarpfen öffnen
If Pixelgetcolor (744, 323) = 0x4B4B4C Then MouseClick ("Right",744 , 323) ;bachforelle öffnen
If Pixelgetcolor (744, 323) = 0x625A71 Then MouseClick ("Right",744 , 323) ;katzenfisch öffnen
If Pixelgetcolor (744 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744 , 323) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 ,323) = 0xFFFFE6 Then MouseClick ("Right",776 , 323) ;zander öffnen
If Pixelgetcolor (776 , 323) = 0x7E6B38 Then MouseClick ("Right",776 , 323) ;mandarin
If Pixelgetcolor (776, 323) = 0xC89899 Then MouseClick ("Right",776 , 323) ;karpfen öffnen
If Pixelgetcolor (776, 323) = 0xA0966B Then MouseClick ("Right",776 , 323) ;graskarpfen öffnen
If Pixelgetcolor (776, 323) = 0x4B4B4C Then MouseClick ("Right",776 , 323) ;bachforelle öffnen
If Pixelgetcolor (776, 323) = 0x625A71 Then MouseClick ("Right",776 , 323) ;katzenfisch öffnen
If Pixelgetcolor (776 , 323) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776 , 323) ;linksklick auf kl. fisch
EndIf
 

Sleep (100) ; 4. REIHE
 

If Pixelgetcolor (648 , 355) = 0xFFFFE6 Then MouseClick ("Right",648 , 355) ;zander öffnen
If Pixelgetcolor (648 , 355) = 0x7E6B38 Then MouseClick ("Right",648 , 355) ;mandarin öffnen
If Pixelgetcolor (648, 355) = 0xC89899 Then MouseClick ("Right",648 , 355) ;karpfen öffnen
If Pixelgetcolor (648, 355) = 0xA0966B Then MouseClick ("Right",648 , 355) ;graskarpfen öffnen
If Pixelgetcolor (648, 355) = 0x4B4B4C Then MouseClick ("Right",648 , 355) ;bachforelle öffnen
If Pixelgetcolor (648, 355) = 0x625A71 Then MouseClick ("Right",648 , 355) ;katzenfisch öffnen
If Pixelgetcolor (648 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 355) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 355) = 0xFFFFE6 Then MouseClick ("Right",680 , 355) ;zander öffnen
If Pixelgetcolor (680 , 355) = 0x7E6B38 Then MouseClick ("Right",680 , 355) ;mandarin
If Pixelgetcolor (680, 355) = 0xC89899 Then MouseClick ("Right",680 , 355) ;karpfen öffnen
If Pixelgetcolor (680, 355) = 0xA0966B Then MouseClick ("Right",680 , 355) ;graskarpfen öffnen
If Pixelgetcolor (680, 355) = 0x4B4B4C Then MouseClick ("Right",680 , 355) ;bachforelle öffnen
If Pixelgetcolor (680, 355) = 0x625A71 Then MouseClick ("Right",680 , 355) ;katzenfisch öffnen
If Pixelgetcolor (680 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 355) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 355) = 0xFFFFE6 Then MouseClick ("Right",712 , 355) ;zander öffnen
If Pixelgetcolor (712 , 355) = 0x7E6B38 Then MouseClick ("Right",712 , 355) ;mandarin
If Pixelgetcolor (712, 355) = 0xC89899 Then MouseClick ("Right",712 , 355) ;karpfen öffnen
If Pixelgetcolor (712, 355) = 0xA0966B Then MouseClick ("Right",712 , 355) ;graskarpfen öffnen
If Pixelgetcolor (712, 355) = 0x4B4B4C Then MouseClick ("Right",712 , 355) ;bachforelle öffnen
If Pixelgetcolor (712, 355) = 0x625A71 Then MouseClick ("Right",712 , 355) ;katzenfisch öffnen
If Pixelgetcolor (712 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 355) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 355 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 355) ;zander öffnen
If Pixelgetcolor (744 , 355) = 0x7E6B38 Then MouseClick ("Right",744 , 355) ;mandarin
If Pixelgetcolor (744, 355) = 0xC89899 Then MouseClick ("Right",744 , 355) ;karpfen öffnen
If Pixelgetcolor (744, 355) = 0xA0966B Then MouseClick ("Right",744 , 355) ;graskarpfen öffnen
If Pixelgetcolor (744, 355) = 0x4B4B4C Then MouseClick ("Right",744 , 355) ;bachforelle öffnen
If Pixelgetcolor (744, 355) = 0x625A71 Then MouseClick ("Right",744 , 355 );katzenfisch öffnen
If Pixelgetcolor (744 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744 , 355) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 ,355) = 0xFFFFE6 Then MouseClick ("Right",776 , 355) ;zander öffnen
If Pixelgetcolor (776 , 355) = 0x7E6B38 Then MouseClick ("Right",776 , 355) ;mandarin
If Pixelgetcolor (776, 355) = 0xC89899 Then MouseClick ("Right",776 , 355) ;karpfen öffnen
If Pixelgetcolor (776, 355) = 0xA0966B Then MouseClick ("Right",776 , 355) ;graskarpfen öffnen
If Pixelgetcolor (776, 355) = 0x4B4B4C Then MouseClick ("Right",776 , 355) ;bachforelle öffnen
If Pixelgetcolor (776, 355) = 0x625A71 Then MouseClick ("Right",776 , 355) ;katzenfisch öffnen
If Pixelgetcolor (776 , 355) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776 , 355) ;linksklick auf kl. fisch
EndIf
 
 
Sleep (100) ; 5. REIHE
 
 
If Pixelgetcolor (648 , 387) = 0xFFFFE6 Then MouseClick ("Right",648 , 387) ;zander öffnen
If Pixelgetcolor (648 , 387) = 0x7E6B38 Then MouseClick ("Right",648 , 387) ;mandarin öffnen
If Pixelgetcolor (648, 387) = 0xC89899 Then MouseClick ("Right",648 , 387) ;karpfen öffnen
If Pixelgetcolor (648, 387) = 0xA0966B Then MouseClick ("Right",648 , 387) ;graskarpfen öffnen
If Pixelgetcolor (648, 387) = 0x4B4B4C Then MouseClick ("Right",648 , 387) ;bachforelle öffnen
If Pixelgetcolor (648, 387) = 0x625A71 Then MouseClick ("Right",648 , 387) ;katzenfisch öffnen
If Pixelgetcolor (648 , 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648 , 387) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 387) = 0xFFFFE6 Then MouseClick ("Right",680 , 387) ;zander öffnen
If Pixelgetcolor (680 , 387) = 0x7E6B38 Then MouseClick ("Right",680 , 387) ;mandarin
If Pixelgetcolor (680, 387) = 0xC89899 Then MouseClick ("Right",680 , 387) ;karpfen öffnen
If Pixelgetcolor (680, 387) = 0xA0966B Then MouseClick ("Right",680 , 387) ;graskarpfen öffnen
If Pixelgetcolor (680, 387) = 0x4B4B4C Then MouseClick ("Right",680 , 387) ;bachforelle öffnen
If Pixelgetcolor (680, 387) = 0x625A71 Then MouseClick ("Right",680 , 387) ;katzenfisch öffnen
If Pixelgetcolor (680, 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",680 , 387) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 387) = 0xFFFFE6 Then MouseClick ("Right",712 , 387) ;zander öffnen
If Pixelgetcolor (712 , 387) = 0x7E6B38 Then MouseClick ("Right",712 , 387) ;mandarin
If Pixelgetcolor (712, 387) = 0xC89899 Then MouseClick ("Right",712 , 387) ;karpfen öffnen
If Pixelgetcolor (712, 387) = 0xA0966B Then MouseClick ("Right",712 , 387) ;graskarpfen öffnen
If Pixelgetcolor (712, 387) = 0x4B4B4C Then MouseClick ("Right",712 , 387) ;bachforelle öffnen
If Pixelgetcolor (712, 387) = 0x625A71 Then MouseClick ("Right",712 , 387) ;katzenfisch öffnen
If Pixelgetcolor (712, 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712 , 387) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 387 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 387) ;zander öffnen
If Pixelgetcolor (744 , 387) = 0x7E6B38 Then MouseClick ("Right",744 , 387) ;mandarin
If Pixelgetcolor (744, 387) = 0xC89899 Then MouseClick ("Right",744 , 387) ;karpfen öffnen
If Pixelgetcolor (744, 387) = 0xA0966B Then MouseClick ("Right",744 , 387) ;graskarpfen öffnen
If Pixelgetcolor (744, 387) = 0x4B4B4C Then MouseClick ("Right",744 , 387) ;bachforelle öffnen
If Pixelgetcolor (744, 387) = 0x625A71 Then MouseClick ("Right",744 , 387) ;katzenfisch öffnen
If Pixelgetcolor (744, 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744, 387) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 ,387) = 0xFFFFE6 Then MouseClick ("Right",776 , 387) ;zander öffnen
If Pixelgetcolor (776 , 387) = 0x7E6B38 Then MouseClick ("Right",776 , 387) ;mandarin
If Pixelgetcolor (776, 387) = 0xC89899 Then MouseClick ("Right",776 , 387) ;karpfen öffnen
If Pixelgetcolor (776, 387) = 0xA0966B Then MouseClick ("Right",776 , 387) ;graskarpfen öffnen
If Pixelgetcolor (776, 387) = 0x4B4B4C Then MouseClick ("Right",776 , 387) ;bachforelle öffnen
If Pixelgetcolor (776, 387) = 0x625A71 Then MouseClick ("Right",776 , 387) ;katzenfisch öffnen
If Pixelgetcolor (776, 387) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776, 387) ;linksklick auf kl. fisch
EndIf
 

Sleep (100) ; 6. REIHE 

If Pixelgetcolor (648 , 419) = 0xFFFFE6 Then MouseClick ("Right",648 , 419) ;zander öffnen
If Pixelgetcolor (648 , 419) = 0x7E6B38 Then MouseClick ("Right",648 , 419) ;mandarin öffnen
If Pixelgetcolor (648, 419) = 0xC89899 Then MouseClick ("Right",648 , 419) ;karpfen öffnen
If Pixelgetcolor (648, 419) = 0xA0966B Then MouseClick ("Right",648 , 419) ;graskarpfen öffnen
If Pixelgetcolor (648, 419) = 0x4B4B4C Then MouseClick ("Right",648 , 419) ;bachforelle öffnen
If Pixelgetcolor (648, 419) = 0x625A71 Then MouseClick ("Right",648 , 419) ;katzenfisch öffnen
If Pixelgetcolor (648, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648, 419) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (680 , 419) = 0xFFFFE6 Then MouseClick ("Right",680 , 419) ;zander öffnen
If Pixelgetcolor (680 , 419) = 0x7E6B38 Then MouseClick ("Right",680 , 419) ;mandarin
If Pixelgetcolor (648, 419) = 0xC89899 Then MouseClick ("Right",648 , 419) ;karpfen öffnen
If Pixelgetcolor (648, 419) = 0xA0966B Then MouseClick ("Right",648 , 419) ;graskarpfen öffnen
If Pixelgetcolor (648, 419) = 0x4B4B4C Then MouseClick ("Right",648 , 419) ;bachforelle öffnen
If Pixelgetcolor (648, 419) = 0x625A71 Then MouseClick ("Right",648 , 419) ;katzenfisch öffnen
If Pixelgetcolor (648, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",648, 419) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (712 , 419) = 0xFFFFE6 Then MouseClick ("Right",712 , 419) ;zander öffnen
If Pixelgetcolor (712 , 419) = 0x7E6B38 Then MouseClick ("Right",712 , 419) ;mandarin
If Pixelgetcolor (712, 419) = 0xC89899 Then MouseClick ("Right",712 , 419) ;karpfen öffnen
If Pixelgetcolor (712, 419) = 0xA0966B Then MouseClick ("Right",712 , 419) ;graskarpfen öffnen
If Pixelgetcolor (712, 419) = 0x4B4B4C Then MouseClick ("Right",712 , 419) ;bachforelle öffnen
If Pixelgetcolor (712, 419) = 0x625A71 Then MouseClick ("Right",712 , 419) ;katzenfisch öffnen
If Pixelgetcolor (712, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",712, 419) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (744 , 419 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 419) ;zander öffnen
If Pixelgetcolor (744 , 419) = 0x7E6B38 Then MouseClick ("Right",744 , 419) ;mandarin
If Pixelgetcolor (744, 419) = 0xC89899 Then MouseClick ("Right",744 , 419) ;karpfen öffnen
If Pixelgetcolor (744, 419) = 0xA0966B Then MouseClick ("Right",744 , 419) ;graskarpfen öffnen
If Pixelgetcolor (744, 419) = 0x4B4B4C Then MouseClick ("Right",744 , 419) ;bachforelle öffnen
If Pixelgetcolor (744, 419) = 0x625A71 Then MouseClick ("Right",744 , 419) ;katzenfisch öffnen
If Pixelgetcolor (744, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",744, 419) ;linksklick auf kl. fisch
EndIf
Sleep (100)
If Pixelgetcolor (776 ,419) = 0xFFFFE6 Then MouseClick ("Right",776 , 419) ;zander öffnen
If Pixelgetcolor (776 , 419) = 0x7E6B38 Then MouseClick ("Right",776 , 419) ;mandarin
If Pixelgetcolor (776, 419) = 0xC89899 Then MouseClick ("Right",776 , 419) ;karpfen öffnen
If Pixelgetcolor (776, 419) = 0xA0966B Then MouseClick ("Right",776 , 419) ;graskarpfen öffnen
If Pixelgetcolor (776, 419) = 0x4B4B4C Then MouseClick ("Right",776 , 419) ;bachforelle öffnen
If Pixelgetcolor (776, 419) = 0x625A71 Then MouseClick ("Right",776 , 419) ;katzenfisch öffnen
If Pixelgetcolor (776, 419) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Right",776, 419) ;linksklick auf kl. fisch
EndIf
 
Sleep (100) ; 7. REIHE
 
 
If Pixelgetcolor (648 , 451) = 0xFFFFE6 Then MouseClick ("Right",648 , 451) ;zander öffnen
If Pixelgetcolor (648 , 451) = 0x7E6B38 Then MouseClick ("Right",648 , 451) ;mandarin öffnen
If Pixelgetcolor (648 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",648 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (680 , 451) = 0xFFFFE6 Then MouseClick ("Right",680 , 451) ;zander öffnen
If Pixelgetcolor (680 , 451) = 0x7E6B38 Then MouseClick ("Right",680 , 451) ;mandarin
If Pixelgetcolor (680 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",680 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (712 , 451) = 0xFFFFE6 Then MouseClick ("Right",712 , 451) ;zander öffnen
If Pixelgetcolor (712 , 451) = 0x7E6B38 Then MouseClick ("Right",712 , 451) ;mandarin
If Pixelgetcolor (712 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",712 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (744 , 451 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 451) ;zander öffnen
If Pixelgetcolor (744 , 451) = 0x7E6B38 Then MouseClick ("Right",744 , 451) ;mandarin
If Pixelgetcolor (744 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",744 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (776 ,451) = 0xFFFFE6 Then MouseClick ("Right",776 , 451) ;zander öffnen
If Pixelgetcolor (776 , 451) = 0x7E6B38 Then MouseClick ("Right",776 , 451) ;mandarin
If Pixelgetcolor (776 , 451) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",776 , 451) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
 
Sleep (100) ; 8. REIHE
 
 
If Pixelgetcolor (648 , 483) = 0xFFFFE6 Then MouseClick ("Right",648 , 483) ;zander öffnen
If Pixelgetcolor (648 , 483) = 0x7E6B38 Then MouseClick ("Right",648 , 483) ;mandarin öffnen
If Pixelgetcolor (648 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",648 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (680 , 483) = 0xFFFFE6 Then MouseClick ("Right",680 , 483) ;zander öffnen
If Pixelgetcolor (680 , 483) = 0x7E6B38 Then MouseClick ("Right",680 , 483) ;mandarin
If Pixelgetcolor (680 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",680 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (712 , 483) = 0xFFFFE6 Then MouseClick ("Right",712 , 483) ;zander öffnen
If Pixelgetcolor (712 , 483) = 0x7E6B38 Then MouseClick ("Right",712 , 483) ;mandarin
If Pixelgetcolor (712 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",712 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (744 , 483 ) = 0xFFFFE6 Then MouseClick ("Right",744 , 483) ;zander öffnen
If Pixelgetcolor (744 , 483) = 0x7E6B38 Then MouseClick ("Right",744 , 483) ;mandarin
If Pixelgetcolor (744 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",744 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
Sleep (100)
If Pixelgetcolor (776 ,483) = 0xFFFFE6 Then MouseClick ("Right",776 , 483) ;zander öffnen
If Pixelgetcolor (776 , 483) = 0x7E6B38 Then MouseClick ("Right",776 , 483) ;mandarin
If Pixelgetcolor (776 , 483) = 0x757651 Then ;kleinen fisch Wegwerfen 
MouseClick ("Left",776 , 483) ;linksklick auf kl. fisch
MouseClick ("Left",513, 401) ;linksklick ausserhalb des inventars
MouseClick ("Left",366, 321) ;rauswerfen bestätigen
EndIf
;---------------------------------------------------
 
 

MouseClick ("", 673, 230)
 
 
 

Sleep (500)
Send ( "{F4 down}" , 0 ) ; hält die Taste F4 runter
Sleep (500) ; Hält die Taste 0,5 Sekunden
Send ( "{F4 up}" , 0 ) ; lässt die Taste F4 wieder los
$begin = TimerInit()
Sleep (1000) ; Wartet wieder 1ne Sekund
 
While (1)
$Fish1 = PixelGetColor ( 414, 130 ) ; Farbe: 0xFCF8FC
$Fish2 = PixelGetColor ( 514, 60 ) ; Farbe: 00xE4E0E4
$Fish3 = PixelGetColor ( 450, 188 ) ; Farbe: 0xF3EFF3
$Fish4 = PixelGetColor ( 298, 112 ) ; Farbe: 0xF3EFF2
$Fish5 = PixelGetColor ( 394, 124 ) ; Farbe: 0xFCF8FC
$Fish6 = PixelGetColor ( 343, 345 ) ; Farbe: 0xEFEAEE
$Fish7 = PixelGetColor ( 375 , 199 ) ; Farbe: 0xF4F0F4
$Fish8 = PixelGetColor ( 440 , 181 ) ; Farbe: 0xECE8EC
$Fish9 = PixelGetColor ( 489 , 205 ) ; Farbe: 0xD8D4D8
$Fish10 = PixelGetColor ( 381 , 95 ) ; Farbe: 0xFDF9FC
$Fish11 = PixelGetColor ( 380 , 77 ) ; Farbe: 0xFCF8FC
$Fish12 = PixelGetColor ( 330 , 51 ) ; Farbe: 0xFCF8FC
$Fish13 = PixelGetColor ( 386 , 51 ) ; Farbe: 0xFCF8FC
$Fish14 = PixelGetColor ( 489 , 63 ) ; Farbe: 0xF7F3F7
$Fish15 = PixelGetColor ( 325 , 221 ) ; Farbe: 0xEBE7EB
$Zeit = 2300

If $Fish1 = 0xFCF8FC Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish1 = 0xFCFCFB Then
Sleep ( $Zeit)
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish2 = 0xE4E0E4 Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish2 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish3 = 0xFCF8FC Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish3 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish4 = 0xF3EFF2 Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish4 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish5 = 0xFCF8FC Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish5 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)$Zeit
Send("{F4 up}")
ExitLoop
EndIf
If $Fish6 = 0xF9F5F8 Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish6 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish7 = 0xF4F0F4 Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish7 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish8 = 0xECE8EC Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish8 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish9 = 0xD8D4D8 Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish9 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish10 = 0xFBFBFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish10 = 0xFDF9FC Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish11 = 0xFCF8FC Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish11 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish12 = 0xFBFBFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish12 = 0xFCF8FC Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish13 = 0xFCF8FC Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish13 = 0xFCFCFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish14 = 0xFBFBFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish14 = 0xF7F3F7 Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish15 = 0xFBFBFB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
If $Fish15 = 0xEBE7EB Then
Sleep ( $Zeit )
Send("{F4 down}")
Sleep(500)
Send("{F4 up}")
ExitLoop
EndIf
$dif = TimerDiff($begin)
If $dif > 120000 Then; wenn die differenz bis zum rotemakiertem timerstart größer als 1min ist, dann
ExitLoop
Endif
Sleep(500) ; Da der While Befehl ist muss auch ein Sleep befehl drin sein sonst überlastet das den PC unnötig
Wend
Sleep(3000) ; wartezeit , bevor er wieder von vorne anfängt
Wend ; die vorher vergessene Wend funktion sry xD
Endfunc
Func Ende ()
Exit ; Programm beendet sich 
EndFunc 
