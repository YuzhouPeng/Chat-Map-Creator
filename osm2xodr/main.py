from math import floor, pi
import numpy as np
from OSMParser.testing import TestEntity, _test_nodes, testSimpleRoad, test_3WayTCrossing2
from OSMParser.osmParsing import parseAll,rNode, OSMWay,JunctionRoad, OSMWayEndcap, createOSMJunctionRoadLine, createOSMWayNodeList2XODRRoadLine
from OSMParser.xodrWriting import startBasicXODRFile,fillNormalRoads,fillJunctionRoads

osmPfad = './versioned_osm_bbox_data_30.548613_114.290288_500.osm'
topographieKartenPfad = ''
xodrPfad = osmPfad+'output.xodr'

parseAll(osmPfad)

startBasicXODRFile(xodrPfad)
fillNormalRoads(xodrPfad)
fillJunctionRoads(xodrPfad)

