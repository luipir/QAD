# -*- coding: latin1 -*-
"""
/***************************************************************************
 QAD Quantum Aided Design plugin

 classe per gestire il map tool in ambito del comando copy
 
                              -------------------
        begin                : 2013-10-02
        copyright            : (C) 2013 IREN Acqua Gas SpA
        email                : geosim.dev@irenacquagas.it
        developers           : roberto poltini (roberto.poltini@irenacquagas.it)
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import math


import qad_debug
import qad_utils
from qad_snapper import *
from qad_snappointsdisplaymanager import *
from qad_variables import *
from qad_getpoint import *
from qad_rubberband import QadRubberBand


#===============================================================================
# Qad_copy_maptool_ModeEnum class.
#===============================================================================
class Qad_copy_maptool_ModeEnum():
   # noto niente si richiede il punto base
   NONE_KNOWN_ASK_FOR_BASE_PT = 1     
   # noto il punto base si richiede il secondo punto per la copia
   BASE_PT_KNOWN_ASK_FOR_COPY_PT = 2     

#===============================================================================
# Qad_copy_maptool class
#===============================================================================
class Qad_copy_maptool(QadGetPoint):
    
   def __init__(self, plugIn):
      QadGetPoint.__init__(self, plugIn)
                        
      self.basePt = None
      self.entitySet = QadEntitySet()
      self.seriesLen = 0
      self.adjust = False
      self.__rubberBand = QadRubberBand(self.canvas)

   def hidePointMapToolMarkers(self):
      QadGetPoint.hidePointMapToolMarkers(self)
      self.__rubberBand.hide()

   def showPointMapToolMarkers(self):
      QadGetPoint.showPointMapToolMarkers(self)
      self.__rubberBand.show()
                             
   def clear(self):
      QadGetPoint.clear(self)
      self.__rubberBand.reset()
      self.mode = None    
   
   def setCopiedGeometries(self, newPt):
      qad_debug.breakPoint()      
      self.__rubberBand.reset()            
      
      for layerEntitySet in self.entitySet.layerEntitySetList:
         layer = layerEntitySet.layer
         transformedBasePt = self.canvas.mapRenderer().mapToLayerCoordinates(layer, self.basePt)
         transformedNewPt = self.canvas.mapRenderer().mapToLayerCoordinates(layer, newPt)
         offSetX = transformedNewPt.x() - transformedBasePt.x()
         offSetY = transformedNewPt.y() - transformedBasePt.y()
         geoms = layerEntitySet.getGeometryCollection()
         
         if self.seriesLen > 0: # devo fare una serie
            #qad_debug.breakPoint()
            
            if self.adjust == True:
               offSetX = offSetX / (self.seriesLen - 1)
               offSetY = offSetY / (self.seriesLen - 1)

            deltaX = offSetX
            deltaY = offSetY
               
            for i in xrange(1, self.seriesLen, 1):
               for geom in geoms:
                  copiedGeom = qad_utils.moveQgsGeometry(geom, deltaX, deltaY)
                  self.__rubberBand.addGeometry(copiedGeom, layer)
                                    
               deltaX = deltaX + offSetX
               deltaY = deltaY + offSetY     
         else:
            for geom in geoms:
               copiedGeom = qad_utils.moveQgsGeometry(geom, offSetX, offSetY)
               self.__rubberBand.addGeometry(copiedGeom, layer)
            
      
   def canvasMoveEvent(self, event):
      QadGetPoint.canvasMoveEvent(self, event)
      
      # noto il punto base si richiede il secondo punto
      if self.mode == Qad_copy_maptool_ModeEnum.BASE_PT_KNOWN_ASK_FOR_COPY_PT:
         self.setCopiedGeometries(self.tmpPoint)                           
         
    
   def activate(self):
      QadGetPoint.activate(self)            
      self.__rubberBand.show()          

   def deactivate(self):
      QadGetPoint.deactivate(self)
      self.__rubberBand.hide()

   def setMode(self, mode):
      self.mode = mode
      # noto niente si richiede il punto base
      if self.mode == Qad_copy_maptool_ModeEnum.NONE_KNOWN_ASK_FOR_BASE_PT:
         self.setDrawMode(QadGetPointDrawModeEnum.NONE)
      # noto il punto base si richiede il secondo punto per l'angolo di rotazione
      elif self.mode == Qad_copy_maptool_ModeEnum.BASE_PT_KNOWN_ASK_FOR_COPY_PT:
         self.setDrawMode(QadGetPointDrawModeEnum.ELASTIC_LINE)
         self.setStartPoint(self.basePt)