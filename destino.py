from bge import logic as g, events 
import bge 
import random as r 
from bge import render as r 
cont = g.getCurrentController() 
o = cont.owner 
cena = g.getCurrentScene() 
add = cena.addObject 
objs = cena.objects 
cenas = g.getSceneList() 
tc = g.keyboard.events 
m = g.mouse.events 
sen = cont.sensors 
act = cont.actuators 
mo = sen['mo'] 
mlb = m[events.LEFTMOUSE] 
hitpos = mo.hitPosition 
if mo.positive: 
	if mlb: 
		o.position.x = hitpos.x o.position.y = hitpos.y
