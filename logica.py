from bge import logic as g, events
import bge
import random as r from bge
import render as r

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

mov = act['mov']
track = act['track']
dest = objs['destino']

if o.getDistanceTo(dest) > 2:
	cont.activate(mov)
	cont.activate(track)
else:
	cont.deactivate(mov)
	cont.deactivate(track)