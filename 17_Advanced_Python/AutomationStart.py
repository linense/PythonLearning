# Whenever we are importing any module, that module executable code will run automatically
import PyModule

PyModule.testingPythonModuleFunction()
PyModule.sum(100,200)

# To use class functions, we need to create an object of the class

obj=PyModule.A()
obj.testingPythonClassFunction()