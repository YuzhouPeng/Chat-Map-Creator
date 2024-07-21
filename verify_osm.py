import xml.etree.ElementTree as ET

def verify_osm_data(filename):
    """
    Verify that the OSM file includes all nodes referenced by ways.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Extract nodes and ways
        nodes = {node.get('id') for node in root.findall('.//node')}
        ways = root.findall('.//way')

        # Check for missing nodes
        for way in ways:
            for nd in way.findall('nd'):
                if nd.get('ref') not in nodes:
                    raise ValueError(f"Missing node {nd.get('ref')} referenced in way {way.get('id')}")

        print("OSM data verification complete: No missing nodes.")
        
    except Exception as e:
        print(f"Error verifying OSM data: {e}")


if __name__ == '__main__':
    verify_osm_data("osm_bbox_data_39.909187_116.397455_2000.osm")
    