import math
import numpy as np

#Dados do exercício

T = 0
g = 9.81

R34 = 0.813 
RP = 3.161
R14 = 2.012

w_2 = 2661  # Peso do elo 2 (N)
I2 = 1.333  # Momento de inércia do elo 2 (Kg.m²)
RCG2 = 0.335  # Centro de gravidade do elo 2 (m)

w_3 = 480.4  # Peso do elo 3 (N)
I3 = 16.95  # Momento de inércia do elo 3 (Kg.m²)
RCG3 = 1.016  # Centro de gravidade do elo 3 (m)

w_4 = 12040  # Peso do elo 4 (N)
I4 = 1209  # Momento de inércia do elo 4 (Kg.m²)
RCG4 = 2.012  # Centro de gravidade do elo 4 (m)

#Comprimento dos elos

a = 0.356 #m
b = 2.032 #m
c = 1.302 #m
d = 2.024 #m
w_2_rpm = 4 #rpm
w_2 = (w_2_rpm*2*math.pi)/60

#Ângulos

theta_2 = float(input('Informe o valor em graus de theta 2: \n'))

alpha_1 = math.atan(1.207 / 1.625) * (180 / math.pi)  # graus

beta = alpha_1 + 90  # graus

gama = 126.582  # graus
gama_rad = gama * (math.pi / 180)

alpha = 143.11
alpha_rad = alpha * (math.pi / 180)

delta = 156.62
delta_rad = delta * (math.pi / 180)

theta_2_linha = (360 - beta + theta_2)  # graus
theta_2_linha_rad = theta_2_linha * (math.pi / 180)  # rad

print("\nÂngulos: \nTheta 2 = ", theta_2, "\nAlpha 1 = ", alpha_1, "\n Beta = ", beta)

#Valores de K
K1 = d/a
K2 = d/c
K3 = ((a**2-b**2)+c**2+d**2)/(2*a*c)
K4 = d/b
K5 = (c**2-a**2-b**2-d**2)/(2*a*b)

print("\nValores de K \nK1 = ", K1, "\nK2 = ", K2, "\nK3 = ", K3, "\nK4 = ", K4, "\nK5 = ", K5)

# Constantes para calcular os angulos
A = math.cos(theta_2_linha_rad)-K1-(K2*math.cos(theta_2_linha_rad))+K3
B = -2*math.sin(theta_2_linha_rad)
C = K1 - (K2+1)*math.cos(theta_2_linha_rad)+K3
D = math.cos(theta_2_linha_rad)-K1+(K4*math.cos(theta_2_linha_rad))+K5
E = -2*math.sin(theta_2_linha_rad)
F = K1+(K4-1)*math.cos(theta_2_linha_rad)+K5

print("\nValores das constantes \nA = ", A, "\nB = ", B, "\nC = ", C, "\nD = ", D, "\nE = ", E, "\nF = ", F)

#Angulos

theta_3_linha_rad = 2 * math.atan((- E + math.sqrt(E ** 2 - 4 * D * F)) / (2 * D))  # graus
theta_4_linha_rad = 2 * math.atan((- B + math.sqrt(B ** 2 - 4 * A * C)) / (2 * A))  # graus

theta_3_linha = theta_3_linha_rad * (180 / math.pi)  # graus
theta_4_linha = theta_4_linha_rad * (180 / math.pi)  # graus

if theta_3_linha < 0:
    theta_3_linha = theta_3_linha + 360
    print("\nTheta 3 linha corrigido= ", theta_3_linha)
else:
    print("\nTheta 3 linha nao precisa ser corrigido")

if theta_4_linha < 0:
    theta_4_linha = theta_4_linha + 360
    print("\nTheta 4 linha corrigido= ", theta_4_linha)
else:
    print("\nTheta 4 linha nao precisa ser corrigido")

#Velocidades
w_3 = (a*(w_2/b)*math.sin(theta_4_linha_rad - theta_2_linha_rad))/(math.sin(theta_3_linha_rad - theta_4_linha_rad))
w_4 = (a*(w_2/c)*math.sin(theta_2_linha_rad - theta_3_linha_rad))/(math.sin(theta_4_linha_rad - theta_3_linha_rad))

print("Velocidades Angulares: \nw_3 = ", w_3, "\nw_4 = ", w_4)

# Constantes para acelerações angulares

alpha_2 = 0

A = c * math.sin(theta_4_linha_rad)
B = b * math.sin(theta_3_linha_rad)
C = (a * alpha_2 * math.sin(theta_2_linha_rad)) + (a * w_2 ** 2 * math.cos(theta_2_linha_rad)) + \
    (b * w_3 ** 2 * math.sin(theta_3_linha_rad)) - (c * w_4 ** 2 * math.cos(theta_4_linha_rad))
D = c * math.cos(theta_4_linha_rad)
E = b * math.cos(theta_3_linha_rad)
F = (a * alpha_2 * math.cos(theta_2_linha_rad)) - (a * w_2 ** 2 * math.sin(theta_2_linha_rad)) - \
    (b * w_3 ** 2 * math.sin(theta_3_linha_rad)) + (c * w_4 ** 2 * math.sin(theta_4_linha_rad))

print("\nValores das constantes \nA = ", A, "\nB = ", B, "\nC = ", C, "\nD = ", D, "\nE = ", E, "\nF = ", F)

#Aceleração 
alpha_3 = ((C * D) - (A * F)) / ((A * E) - (B * D))
alpha_4 = ((C * E) - (B * F)) / ((A * E) - (B * D))

print("\nAcelerações Angulares: \nalpha 2 = ", alpha_2, "rad/s²", "\nalpha 3 = ", alpha_3, "rad/s²",
      "\nalpha 4 = ", alpha_4, "rad/s²")

#Acelerações no Centro de Gravidade
beta = -14.03
beta_rad = beta * (math.pi / 180)

print("\nAcelerações no centro de gravidade:")

a_CG2_real = RCG2 * alpha_2 * (-math.sin(theta_2_linha_rad)) - RCG2 * w_2 ** 2 * (math.cos(theta_2_linha_rad))
a_CG2_img = RCG2 * alpha_2 * (math.cos(theta_2_linha_rad)) - RCG2 * w_2 ** 2 * (math.sin(theta_2_linha_rad))
a_CG2 = math.sqrt(a_CG2_real ** 2 + a_CG2_img ** 2)  # Aceleração no CG2 (m/s²)

print("\nParte real da acel. no CG do elo 2 = ", a_CG2_real, "m/s²", "\nParte imag. da acel. no CG do elo 2 = ",
      a_CG2_img, "m/s²", "\nMódulo da acel. no CG2 = ", a_CG2, "m/s²")

a_A_real = a * alpha_2 * (-math.sin(theta_2_linha_rad)) - a * w_2 ** 2 * (math.cos(theta_2_linha_rad))
a_A_img = a * alpha_2 * (math.cos(theta_2_linha_rad)) - a * w_2 ** 2 * (math.sin(theta_2_linha_rad))
a_A = math.sqrt(a_A_real ** 2 + a_A_img ** 2)

print("\nParte real da acel. em A = ", a_A_real, "m/s²", "\nParte imag. da acel. em A = ",
      a_A_img, "m/s²", "\nMódulo da acel. em A = ", a_A, "m/s²")

a_CG3_A_real = RCG3 * alpha_3 * (-math.sin(theta_3_linha_rad)) - RCG3 * w_3 ** 2 * (math.cos(theta_3_linha_rad))
a_CG3_A_img = RCG3 * alpha_3 * (math.cos(theta_3_linha_rad)) - RCG3 * w_3 ** 2 * (math.sin(theta_3_linha_rad))
a_CG3_A = math.sqrt(a_CG3_A_real ** 2 + a_CG3_A_img ** 2)  # Aceleração no CG3 (m/s²)

print("\nParte real da acel. em CG3_A = ", a_CG3_A_real, "m/s²", "\nParte imag. da acel. em CG3_A = ",
      a_CG3_A_img, "m/s²", "\nMódulo da acel. em CG3_A = ", a_CG3_A, "m/s²")

a_CG3_real = a_A_real + a_CG3_A_real
a_CG3_img = a_A_img + a_CG3_A_img
a_CG3 = math.sqrt(a_CG3_real ** 2 + a_CG3_img ** 2)

print("\nParte real da acel. no CG do elo 3 = ", a_CG3_real, "m/s²", "\nParte imag. da acel. no CG do elo 3 = ",
      a_CG3_img, "m/s²", "\nMódulo da acel. no CG3 = ", a_CG3, "m/s²")

a_CG4_real = RCG4 * alpha_4 * (-math.sin(theta_4_linha_rad + beta_rad)) - RCG4 * w_4 ** 2 * \
             (math.cos(theta_4_linha_rad + beta_rad))
a_CG4_img = RCG4 * alpha_4 * (math.cos(theta_4_linha_rad + beta_rad)) - RCG4 * w_4 ** 2 * \
            (math.sin(theta_4_linha_rad + beta_rad))
a_CG4 = math.sqrt(a_CG4_real ** 2 + a_CG4_img ** 2)  # Aceleração no CG4 (m/s²)

print("\nParte real da acel. no CG do elo 4 = ", a_CG4_real, "m/s²", "\nParte imag. da acel. no CG do elo 4 = ",
      a_CG4_img, "m/s²", "\nMódulo da acel. no CG4 = ", a_CG4, "m/s²")

# Ângulos dos Centros de gravidade no sistema de coordenadas global:
print("\nÂngulos dos Centros de gravidade no sistema de coordenadas global")

theta_CG2_rad = math.atan2(a_CG2_img, a_CG2_real) + gama_rad  # rad
theta_CG2 = theta_CG2_rad * (180 / math.pi)  # graus

theta_CG3_rad = math.atan2(a_CG3_img, a_CG3_real) + gama_rad  # rad
theta_CG3 = theta_CG3_rad * (180 / math.pi)  # graus

theta_CG4_rad = math.atan2(a_CG4_img, a_CG4_real) + gama_rad  # rad
theta_CG4 = theta_CG4_rad * (180 / math.pi)  # graus

print("Em graus:", "\nTheta no CG2: ", theta_CG2, "\nTheta no CG3 = ", theta_CG3, "\nTheta no CG4 = ", theta_CG4)
print("Em radianos :", "\nTheta no CG2: ", theta_CG2_rad, "\nTheta no CG3 = ", theta_CG3_rad,
      "\nTheta no CG4 = ", theta_CG4_rad)

#Componentes x e y das acelerações nos centros de gravidade:

a_CG2_x = a_CG2 * math.cos(theta_CG2_rad)
a_CG2_y = a_CG2 * math.sin(theta_CG2_rad)

a_CG3_x = a_CG3 * math.cos(theta_CG3_rad)
a_CG3_y = a_CG3 * math.sin(theta_CG3_rad)

a_CG4_x = a_CG4 * math.cos(theta_CG4_rad)
a_CG4_y = a_CG4 * math.sin(theta_CG4_rad)

print("\nComponente x no CG2 = ", a_CG2_x, "m/s²", "\nComponente y no CG2 = ", a_CG2_y,
      "\n\nComponente x no CG3 = ", a_CG3_x, "\nComponente y no CG3 = ", a_CG3_y,
      "\n\nComponente x no CG4 = ", a_CG4_x, "\nComponente y no CG4 = ", a_CG4_y)


#Calculando as compon. x e y dos vetores de posição
theta_2_linha_rad = theta_2_linha_rad + gama_rad
theta_3_linha_rad = theta_3_linha_rad + gama_rad - (2 * math.pi)
theta_4_linha_rad = theta_4_linha_rad + gama_rad - (2 * math.pi)

R12X = RCG2 * math.cos(theta_2_linha_rad + math.pi)
R12Y = RCG2 * math.sin(theta_2_linha_rad + math.pi)

R32X = (a - RCG2) * (math.cos(theta_2_linha_rad))
R32Y = (a - RCG2) * (math.sin(theta_2_linha_rad))

R23X = RCG3 * math.cos(theta_3_linha_rad + math.pi)
R23Y = RCG3 * math.sin(theta_3_linha_rad + math.pi)

R43X = (RCG3 - b) * math.cos(theta_3_linha_rad + math.pi)
R43Y = (RCG3 - b) * math.sin(theta_3_linha_rad + math.pi)

R34X = R34 * math.cos(theta_4_linha_rad + alpha_rad)
R34Y = R34 * math.sin(theta_4_linha_rad + alpha_rad)

R14X = R14 * math.cos(theta_4_linha_rad + beta_rad + math.pi)
R14Y = R14 * math.sin(theta_4_linha_rad + beta_rad + math.pi)

RPX = RP * math.cos(theta_4_linha_rad + delta_rad)
RPY = RP * math.sin(theta_4_linha_rad + delta_rad)

print("\nR12x = ", R12X)
print("\nR12y = ", R12Y)
print("\nR32x = ", R32X)
print("\nR32y = ", R32Y)
print("\nR23x = ", R23X)
print("\nR23y = ", R23Y)
print("\nR43x = ", R43X)
print("\nR43y = ", R43Y)
print("\nR34x = ", R34X)
print("\nR34y = ", R34Y)
print("\nF14x = ", R14X)
print("\nF14y = ", R14Y)
print("\nRPx = ", RPX)
print("\nRPy = ", RPY)

#Componentes x e y da força externa em P e as forças peso nos CG
FPX = 0
FPY = -F
FG2Y = -w_2
FG3Y = -w_3
FG4Y = -w_4

#Calculando as massas dos elos
m2 = w_2 / g
m3 = w_3 / g
m4 = w_4 / g

print("\nMassas dos elos:\n", "\nMassa do elo 2 = ", m2, "Kg", "\nMassa do elo 3 = ", m3, "Kg",
      "\nMassa do elo 4 = ", m4, "Kg")

#Matrizes

C = [[1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 0, 0, 0, 0],
     [-R12Y, R12X, -R32Y, R32X, 0, 0, 0, 0, 1],
     [0, 0, -1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, -1, 0, 1, 0, 0, 0],
     [0, 0, R23Y, -R23X, -R43Y, R43X, 0, 0, 0],
     [0, 0, 0, 0, -1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, -1, 0, 1, 0],
     [0, 0, 0, 0, R34Y, -R34X, -R14Y, R14X, 0]]

print("\nMatriz C= ", C)

C_inv = np.linalg.inv(C)

F = [[m2 * a_CG2_x],
     [m2 * a_CG2_y - FG2Y],
     [I2 * alpha_2],
     [m3 * a_CG3_x],
     [m3 * a_CG3_y - FG3Y],
     [I3 * alpha_3],
     [m4 * a_CG4_x - FPX],
     [m4 * a_CG4_y - FPY - FG4Y],
     [I4 * alpha_4 - (RPX * FPY - RPY * FPX)]]

print("\nMatriz F= ", F)

R = np.dot(C_inv, F)

print("\nF12x= ", R[0])
print("\nF12y= ", R[1])
print("\nF32x= ", R[2])
print("\nF32y= ", R[3])
print("\nF43x= ", R[4])
print("\nF43y= ", R[5])
print("\nF14x= ", R[6])
print("\nF14y= ", R[7])
print("\nT12x= ", R[8])