#!/usr/bin/python
# -*- coding: utf-8 -*-

__title__   = "Nya"
__version__ = "1.0"
__date__    = "08.2022"

import FreeCAD, FreeCADGui, Part

OBJECT_VERTEX = "Vertex"
OBJECT_EDGE = "Edge"

INDEX_FIRST_POINT = 1
INDEX_SECOND_POINT = 2
INDEX_CENTER = 3

def message(text):
    FreeCAD.Console.PrintMessage(text)
    FreeCAD.Console.PrintMessage("\n")


def run_macro():
    vertices = collect_selected_vertices_names()
    if not vertices:
        message("No vertices selected.")
        return
    sketch = FreeCADGui.ActiveDocument.getInEdit().Object

    message(vertices)
    for vertex_name in vertices:
        index = int(vertex_name[len(OBJECT_VERTEX):]) - 1
        message(index)
        sketch.addConstraint(Sketcher.Constraint('Coincident', index, INDEX_CENTER, -1, 1))
    
def collect_selected_vertices_names():
    selection = FreeCADGui.Selection.getSelectionEx()
    if not selection:
        return []
    
    return list(filter(lambda x: x.startswith(OBJECT_VERTEX), selection[0].SubElementNames))

run_macro()
