import xml.etree.ElementTree
from config import XML_PATh


# read the information from the XML file
class Read_xml :
    ips = []
    ports = []
    usernames = []
    passwords = []
    mails = []
    alerts={}
    Xml_file = xml.etree.ElementTree.parse(XML_PATh)
    Xml_root = Xml_file.getroot()
    clients_index=0
    for Xml_client in Xml_root.iter('client'):
        ips.append(Xml_client.attrib['ip'])
        ports.append(Xml_client.attrib["port"])
        usernames.append(Xml_client.attrib["username"])
        passwords.append( Xml_client.attrib["password"])
        mails.append(Xml_client.attrib["mail"])
        alerts_index = 0
        for Xml_alert in Xml_client.iter('alert'):
            alerts[clients_index, alerts_index] = (Xml_alert.attrib["type"], Xml_alert.attrib["limit"])
            alerts_index += 1
        clients_index += 1






