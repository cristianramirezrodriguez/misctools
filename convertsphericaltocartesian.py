
#Convert spherical to cartesian
#Author: Cristian Ramirez Rodriguez

import numpy as np

def findx(r, theta, phi):
  x = r*np.sin(theta)*np.cos(phi)
  return(x)

def findy(r, theta, phi):
  y = r*np.sin(theta)*np.sin(phi)
  return(y)

def findz(r, theta):
  z = r*np.cos(theta)
  return(z)

def rtptoxyz(r, theta, phi):
  x = findx(r, theta, phi)
  y = findy(r, theta, phi)
  z = findz(r, theta)
  recvec = [x, y, z]
  return(recvec)

def spherematrixtocartmatrix(listofvectors): #Of the form [[r0, theta0, phi0],[r1, theta1,phi1],[r2,theta2,phi2]...]
  cartmatrix = []
  for i in range(len(listofvectors)):
    r = listofvectors[i][0]
    theta = listofvectors[i][1]
    phi = listofvectors[i][2]
    newvec = rtptoxyz(r, theta, phi)
    cartmatrix.append(newvec)
  return(cartmatrix)

'''
#test

testsphericalmatrix = [[1,2,3],[3,4,5],[6,8,10],[11,-2,4],[3.2,5,6.5]]
print(spherematrixtocartmatrix(testsphericalmatrix))
'''
