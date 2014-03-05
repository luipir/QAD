# -*- coding: latin1 -*-
"""
/***************************************************************************
 QAD Quantum Aided Design plugin

 comando SETCURRLAYERBYGRAPH per settare il layer corrente tramite selezione grafica
 comando SETCURRUPDATEABLELAYERBYGRAPH per settare il layer corrente e porlo in modifica 
                                       tramite selezione grafica
 
                              -------------------
        begin                : 2013-05-22
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


import qad_debug
from qad_generic_cmd import QadCommandClass
from qad_snapper import *
from qad_getpoint import *
from qad_entsel_cmd import QadEntSelClass
from qad_ssget_cmd import QadSSGetClass
from qad_msg import QadMsg


# Classe che gestisce il comando SETCURRLAYERBYGRAPH
class QadSETCURRLAYERBYGRAPHCommandClass(QadCommandClass):

   def getName(self):
      return QadMsg.translate("Command_list", "SETCURRLAYERDAGRAFICA")

   def connectQAction(self, action):
      QObject.connect(action, SIGNAL("triggered()"), self.plugIn.runSETCURRLAYERBYGRAPHCommand)

   def getIcon(self):
      return QIcon(":/plugins/qad/icons/setcurrlayerbygraph.png")
   
   def getNote(self):
      # impostare le note esplicative del comando      
      return QadMsg.translate("Command_SETCURRLAYERBYGRAPH", "Seleziona un layer di un oggetto grafico.")
   
   def __init__(self, plugIn):
      QadCommandClass.__init__(self, plugIn)
      self.EntSelClass = None

   def __del__(self):
      QadCommandClass.__del__(self)
      
   def getPointMapTool(self, drawMode = QadGetPointDrawModeEnum.NONE):
      if self.step == 0 or self.step == 1: # quando si � in fase di selezione entit�
         return self.EntSelClass.getPointMapTool(drawMode)
      else:
         return QadCommandClass.getPointMapTool(self, drawMode)
   
   def waitForEntsel(self, msgMapTool, msg):
      if self.EntSelClass is not None:
         del self.EntSelClass            
      self.EntSelClass = QadEntSelClass(self.plugIn)
      self.EntSelClass.msg = QadMsg.translate("Command_SETCURRLAYERBYGRAPH", "Selezionare l'oggetto il cui layer diventer� quello corrente: ")
      self.getPointMapTool().setSnapType(QadSnapTypeEnum.DISABLE)
      self.EntSelClass.run(msgMapTool, msg)
        
   def run(self, msgMapTool = False, msg = None):
      if self.step == 0:     
         self.waitForEntsel(msgMapTool, msg)
         self.step = 1
         return False # continua
      
      elif self.step == 1:
         if self.EntSelClass.run(msgMapTool, msg) == True:
            if self.EntSelClass.entity.isInitialized():
               layer = self.EntSelClass.entity.layer
               if self.plugIn.canvas.currentLayer() is None or \
                  self.plugIn.canvas.currentLayer() != layer:                              
                  self.plugIn.canvas.setCurrentLayer(layer)
                  self.plugIn.iface.setActiveLayer(layer) # lancia evento di deactivate e activate dei plugin
                  self.plugIn.iface.legendInterface().refreshLayerSymbology(layer)
                  msg = QadMsg.translate("Command_SETCURRLAYERBYGRAPH", "\nIl layer corrente � {0}.")
                  self.showMsg(msg.format(layer.name()))
               del self.EntSelClass
               return True
            else:               
               self.showMsg(QadMsg.translate("Command_SETCURRLAYERBYGRAPH", "Non ci sono geometrie in questa posizione."))
               self.waitForEntsel(msgMapTool, msg)
         return False # continua
         

# Classe che gestisce il comando SETCURRUPDATEABLELAYERBYGRAPH
class QadSETCURRUPDATEABLELAYERBYGRAPHCommandClass(QadCommandClass):

   def getName(self):
      return QadMsg.translate("Command_list", "SETCURRMODIFLAYERDAGRAFICA")

   def connectQAction(self, action):
      QObject.connect(action, SIGNAL("triggered()"), self.plugIn.runSETCURRUPDATEABLELAYERBYGRAPHCommand)

   def getIcon(self):
      return QIcon(":/plugins/qad/icons/setcurrupdateablelayerbygraph.png")
   
   def getNote(self):
      # impostare le note esplicative del comando      
      return QadMsg.translate("Command_SETCURRUPDATEABLELAYERBYGRAPH", "Seleziona un layer di un oggetto grafico e lo rende modificabile.")
   
   def __init__(self, plugIn):
      QadCommandClass.__init__(self, plugIn)
      self.SSGetClass = QadSSGetClass(plugIn)
      self.firstTime = True

   def __del__(self):
      QadCommandClass.__del__(self)
      del self.SSGetClass
        
   def getPointMapTool(self, drawMode = QadGetPointDrawModeEnum.NONE):
      if self.step == 0: # quando si � in fase di selezione entit�
         return self.SSGetClass.getPointMapTool(drawMode)
      else:
         return QadCommandClass.getPointMapTool(self, drawMode)
        
   def run(self, msgMapTool = False, msg = None):     
      if self.step == 0: # inizio del comando   
         if self.firstTime == True:
            self.showMsg(QadMsg.translate("Command_SETCURRUPDATEABLELAYERBYGRAPH", "\nSelezionare gli oggetti i cui layer diventeranno editabili: "))
            self.firstTime = False
            
         if self.SSGetClass.run(msgMapTool, msg) == True:
            # selezione terminata
            self.step = 1
            return self.run(msgMapTool, msg)
         else:
            return False # continua

      elif self.step == 1: # dopo aver atteso la selezione di oggetti         
         for layerEntitySet in self.SSGetClass.entitySet.layerEntitySetList:
            layer = layerEntitySet.layer       
            if layer.isEditable() == False:
               if layer.startEditing() == True:
                  self.plugIn.iface.legendInterface().refreshLayerSymbology(layer)
                  msg = QadMsg.translate("Command_SETCURRUPDATEABLELAYERBYGRAPH", "\nIl layer {0} � editabile.")
                  self.showMsg(msg.format(layer.name()))

         if len(self.SSGetClass.entitySet.layerEntitySetList) == 1:
            layer = self.SSGetClass.entitySet.layerEntitySetList[0].layer
            if self.plugIn.canvas.currentLayer() is None or \
               self.plugIn.canvas.currentLayer() != layer:               
               self.plugIn.canvas.setCurrentLayer(layer)
               self.plugIn.iface.setActiveLayer(layer) # lancia evento di deactivate e activate dei plugin
               self.plugIn.iface.legendInterface().refreshLayerSymbology(layer)
               msg = QadMsg.translate("Command_SETCURRUPDATEABLELAYERBYGRAPH", "\nIl layer corrente � {0}.")
               self.showMsg(msg.format(layer.name()))
         
         return True