
import vtk
from vtk.util.colors import tomato

# Set parameters of cylinder
cylinder = vtk.vtkCylinderSource()
cylinder.SetCenter(0,0.73875,0)
cylinder.SetRadius(0.063)
cylinder.SetHeight(0.225) 
cylinder.SetResolution(1000)


cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.GetProperty().SetColor(tomato)
cylinderActor.RotateX(30.0)
cylinderActor.RotateY(-45.0)
cylinderActor.GetProperty().SetColor(1,1,1)

# renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.AddActor(cylinderActor)
ren.SetBackground(0, 0, 0)
renWin.SetSize(200, 200)

iren.Initialize()
ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()

# Start the event loop.
iren.Start()


