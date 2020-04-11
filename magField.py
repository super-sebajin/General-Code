#Programa par calcular el campo magnetico de un proton en moviemiento en varias condiciones
from vpython import *

scene.width = scene.height = 1000

#class Constants hecha para encapsular las constantes del programa en un objeto
class Constants:
    def __init__(self):
        self.mzofp = 1e-7
        self.dr = 4e-12
        self.dt = 1e-16
        self.obs_pd = 8e-11
        self.scale = 1e-11

#Instancia de Constants, sin el no corre el programa
C = Constants()

#proton y anti proton
e_p = sphere(pos = vector(-4e-10,0,0), radius = 1e-11 ,color = color.orange, q = 1.6e-17, vel = vector(4e4,0,0))
e_p_opp = sphere(pos = vector(4e-10,0,0), radius = 1e-11 ,color = color.orange, q = 1.6e-17, vel = vector(-4e4,0,0))

#punto y inicial y final
sphere(pos = vector(-4e-10,0,0), radius = 1e-11 ,color = color.blue)
sphere(pos = vector(4e-10,0,0), radius = 1e-11 ,color = color.red)

def obs_pts():#crear lista de flechas a una distancia radial del origen
    theta = 0
    pts = []
    while theta < 2*pi:
        pts.append(arrow(pos = vector(0,C.obs_pd*cos(theta), C.obs_pd*sin(theta)),
                         axis = vector(0,0,0), color = color.red))
        theta += pi/3
    return pts

def more_pts(a):#crear lista de flechas a una distancia radial del parametro a
    theta = 0
    arrows = []
    while theta < 2*pi:
        arrows.append(arrow(pos = vector(a, C.obs_pd*cos(theta), C.obs_pd*sin(theta)),
            axis = vector(0,0,0), color = color.red))
        theta += pi/3
    return arrows

def B_at_pt(a):#patron de campo magnetico en el origen, un aro
    obs = obs_pts()
    while a.pos.x < 4e-10:
        rate(30)
        a.pos = a.pos + a.vel*C.dt
        for i in obs:
            r = i.pos - a.pos
            B = (C.mzofp * a.q * cross(a.vel,norm(r))) / mag2(r)
            i.axis = C.scale*B

def B_multi(a):#patron de campo magnetico de izquierda a derecha, multiples aros
    obs = [more_pts(-4e-10),
           more_pts(-2e-10),
           more_pts(0),
           more_pts(2e-10),
           more_pts(4e-10)]
    while a.pos.x < 4e-10:
        rate(50)
        a.pos = a.pos + a.vel*C.dt
        for i in range(len(obs)):
            for j in obs[i]:
                r = j.pos - a.pos
                B = (C.mzofp * a.q * cross(a.vel,norm(r))) / mag2(r)
                j.axis = C.scale * B

def B_multi_opp(a):#patron de campo magnetico de derecha a izquierda, multiples aros
    obs = [more_pts(4e-10),
           more_pts(2e-10),
           more_pts(0),
           more_pts(-2e-10),
           more_pts(-4e-10)]
    while a.pos.x > -4e-10:
        rate(50)
        a.pos = a.pos + a.vel*C.dt
        for i in range(len(obs)):
            for j in obs[i]:
                r = j.pos - a.pos
                B = (C.mzofp * a.q * cross(a.vel,norm(r))) / mag2(r)
                j.axis = C.scale * B
#quitar comentario a la funcion de deseas llamar
#B_at_pt(e_p)
#B_multi(e_p)
B_multi_opp(e_p_opp)
