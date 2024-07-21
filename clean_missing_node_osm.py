import xml.etree.ElementTree as ET

def clean_osm_data(filename):
    """
    Clean the OSM file to remove references to missing nodes.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Extract nodes and ways
        nodes = {node.get('id') for node in root.findall('.//node')}
        ways = root.findall('.//way')

        # Remove references to missing nodes
        for way in ways:
            for nd in way.findall('nd'):
                if nd.get('ref') not in nodes:
                    way.remove(nd)
        
        # Write cleaned data to a new file
        cleaned_filename = f"cleaned_{filename}"
        tree.write(cleaned_filename, encoding='utf-8', xml_declaration=True)
        print(f"Cleaned OSM data saved to {cleaned_filename}")
        
    except Exception as e:
        print(f"Error cleaning OSM data: {e}")

if __name__ == '__main__':
    clean_osm_data("osm_bbox_data_39.867631_116.376426_2000.osm")
    