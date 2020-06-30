# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:25:21 2020

@author: logun
"""
import vtk

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



#Visualization
contour=vtk.vtkMarchingCubes()
#vtk.vtkContourFilter()
contour.SetInputConnection(reader.GetOutputPort())
contour.ComputeNormalsOn()
contour.SetValue(4,8)


mapper=vtk.vtkPolyDataMapper()
mapper.SetInputConnection(contour.GetOutputPort())
mapper.ScalarVisibilityOff()

actor=vtk.vtkActor()
actor.SetMapper(mapper)
renderer=vtk.vtkRenderer()
renderer.AddActor(actor)
window=vtk.vtkRenderWindow()
window.SetSize(600,600)
window.AddRenderer(renderer)

#Createinteractor,addwindow&addobservers
interactor=vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

#Startrenderer&interactor3
window.Render()
interactor.Initialize()
