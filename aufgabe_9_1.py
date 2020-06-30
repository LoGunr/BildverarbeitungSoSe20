# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:25:21 2020

@author: logun
"""
import vtk
import matplotlib.pyplot as plt
import numpy as np 
from vtk.util.numpy_support import vtk_to_numpy
import cv2

#Read3DRAWimage
reader=vtk.vtkImageReader()
reader.SetDataScalarType(vtk.VTK_UNSIGNED_CHAR) #unsignedint8
reader.SetFileName("engine.raw")
reader.SetNumberOfScalarComponents(1)
reader.SetFileDimensionality(3)
reader.SetDataByteOrderToLittleEndian()
reader.SetDataExtent(0,255,0,255,0,127)
reader.SetDataSpacing(1.0,1.0,1.0)
reader.Update()

imgdata = reader.GetOutput()

img = vtk_to_numpy(imgdata.GetPointData().GetScalars())

hist, bins = np.histogram(img.flatten(), 256,[0,256])

equ = cv2.equalizeHist(img)

plt.hist(img.flatten(),256,[0,256], color="r")

#pls.imshow()

plt.subplot(111),plt.hist(img.flatten(),256,[0,256], color="r", log = True),plt.title('Histogramm')

#plt.xticks([]), plt.yticks([])
ren1 = vtk.vtkRenderer()
renWin=vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
iren=vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
#Mit dieser Funktion bestimmen sie die Opacity
#der jeweiligen Grauwerte im Bild
opacityTransferFunction=vtk.vtkPiecewiseFunction()
colorTransferFunction=vtk.vtkColorTransferFunction()

def show_20to60():
    opacityTransferFunction.AddPoint(0,0.0)
    opacityTransferFunction.AddPoint(20,0.0)
    opacityTransferFunction.AddPoint(50,0.8)
    opacityTransferFunction.AddPoint(60,0.0)
    #Create transfer mapping scalar value to color.
    
    colorTransferFunction.AddRGBPoint(0.0,1.0,0.0,0.0)
    colorTransferFunction.AddRGBPoint(64.0,1.0,0.0,0.0)
    colorTransferFunction.AddRGBPoint(128.0,0.0,0.0,1.0)
    colorTransferFunction.AddRGBPoint(192.0,0.0,1.0,0.0)
    colorTransferFunction.AddRGBPoint(255.0,0.0,0.2,0.0)

def show_green_clamps():
    opacityTransferFunction.AddPoint(0,0.0)
    opacityTransferFunction.AddPoint(254,0.0)
    opacityTransferFunction.AddPoint(255,0.8)
    #opacityTransferFunction.AddPoint(60,0.0)
    #Create transfer mapping scalar value to color.
    
    colorTransferFunction.AddRGBPoint(0.0,1.0,0.0,0.0)
    colorTransferFunction.AddRGBPoint(64.0,1.0,0.0,0.0)
    colorTransferFunction.AddRGBPoint(128.0,0.0,0.0,1.0)
    colorTransferFunction.AddRGBPoint(192.0,0.0,1.0,0.0)
    colorTransferFunction.AddRGBPoint(255.0,0.0,1.0,0.0)

show_green_clamps()
#The property describes how the data will look.
volumeProperty=vtk.vtkVolumeProperty()
volumeProperty.SetColor(colorTransferFunction)
volumeProperty.SetScalarOpacity(opacityTransferFunction)
volumeProperty.ShadeOn()
volumeProperty.SetInterpolationTypeToLinear()

#Themapper/raycastfunctionknowhowtorenderthedata.
volumeMapper=vtk.vtkFixedPointVolumeRayCastMapper()
volumeMapper.SetInputConnection(reader.GetOutputPort())
#Thevolumeholdsthemapperandthepropertyand
#canbeusedtoposition/orientthevolume.
volume=vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)
ren1.AddVolume(volume)
ren1.ResetCamera()

renWin.SetSize(600,600)
renWin.Render()
iren.Start()
