from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

PORT_NUMBER = 8080


class UPNPHTTPServerHandler(BaseHTTPRequestHandler):
    """
    A HTTP handler that serves the UPnP XML files.
    """

    # Handler for the GET requests
    def do_GET(self):
        if self.path == "/" + self.server.scpd_xml_path:
            self.send_response(200)
            self.send_header('Content-type', 'application/xml')
            self.end_headers()
            self.wfile.write(self.scpd_xml.encode())
            return
        if self.path == "/" + self.server.device_xml_path:
            self.send_response(200)
            self.send_header('Content-type', 'application/xml')
            self.end_headers()
            self.wfile.write(self.device_xml.encode())
            return
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Not found.")
            return

    @property
    def services_xml(self):
        xml = """<serviceList>
            <service>
                <URLBase>{hive_url}</URLBase>
                <serviceType>urn:jarbasAi:HiveMind:service:Master</serviceType>
                <serviceId>urn:jarbasAi:HiveMind:serviceId:HiveMindNode</serviceId>
                <controlURL>/HiveMind</controlURL>
                <eventSubURL/>
                <SCPDURL>{scpd_path}</SCPDURL>
            </service>
        </serviceList>"""
        return xml.format(scpd_path=self.server.scpd_xml_path,
                          hive_url=self.server.presentation_url)

    @property
    def device_xml(self):
        """
        Get the main device descriptor xml file.
        """
        xml = """<root>
    <specVersion>
        <major>{major}</major>
        <minor>{minor}</minor>
    </specVersion>
    <device>
        <deviceType>urn:schemas-upnp-org:device:Basic:1</deviceType>
        <friendlyName>{friendly_name}</friendlyName>
        <manufacturer>{manufacturer}</manufacturer>
        <manufacturerURL>{manufacturer_url}</manufacturerURL>
        <modelDescription>{model_description}</modelDescription>
        <modelName>{model_name}</modelName>
        <modelNumber>{model_number}</modelNumber>
        <modelURL>{model_url}</modelURL>
        <serialNumber>{serial_number}</serialNumber>
        <UDN>uuid:{uuid}</UDN>
        {services_xml}
        <presentationURL>{presentation_url}</presentationURL>
    </device>
</root>"""
        return xml.format(friendly_name=self.server.friendly_name,
                          manufacturer=self.server.manufacturer,
                          manufacturer_url=self.server.manufacturer_url,
                          model_description=self.server.model_description,
                          model_name=self.server.model_name,
                          model_number=self.server.model_number,
                          model_url=self.server.model_url,
                          serial_number=self.server.serial_number,
                          uuid=self.server.uuid,
                          presentation_url=self.server.presentation_url,
                          scpd_path=self.server.scpd_xml_path,
                          services_xml=self.services_xml,
                          major=self.server.major_version,
                          minor=self.server.minor_version
                          # device_xml_path=self.device_xml_path
                          )

    @property
    def scpd_xml(self):
        """
        Get the device WSD file.
        """
        return """<scpd xmlns="urn:schemas-upnp-org:service-1-0">
<specVersion>
<major>1</major>
<minor>0</minor>
</specVersion>
</scpd>"""


class UPNPHTTPServerBase(HTTPServer):
    """
    A simple HTTP server that knows the information about a UPnP device.
    """

    def __init__(self, server_address, request_handler_class):
        HTTPServer.__init__(self, server_address, request_handler_class)
        self.port = None
        self.friendly_name = None
        self.manufacturer = None
        self.manufacturer_url = None
        self.model_description = None
        self.model_name = None
        self.model_url = None
        self.serial_number = None
        self.uuid = None
        self.presentation_url = None
        self.scpd_xml_path = None
        self.device_xml_path = None
        self.major_version = None
        self.minor_version = None


class UPNPHTTPServer(threading.Thread):
    """
    A thread that runs UPNPHTTPServerBase.
    """

    def __init__(self, port, friendly_name, manufacturer, manufacturer_url,
                 model_description, model_name,
                 model_number, model_url, serial_number, uuid,
                 presentation_url, host=""):
        threading.Thread.__init__(self, daemon=True)
        self.server = UPNPHTTPServerBase(('', port), UPNPHTTPServerHandler)
        self.server.port = port
        self.server.friendly_name = friendly_name
        self.server.manufacturer = manufacturer
        self.server.manufacturer_url = manufacturer_url
        self.server.model_description = model_description
        self.server.model_name = model_name
        self.server.model_number = model_number
        self.server.model_url = model_url
        self.server.serial_number = serial_number
        self.server.uuid = uuid
        self.server.presentation_url = presentation_url
        self.server.scpd_xml_path = 'scpd.xml'
        self.server.device_xml_path = "device.xml"
        self.server.major_version = 0
        self.server.minor_version = 1
        self.host = host

    @property
    def path(self):
        path = 'http://{ip}:{port}/{path}'.format(ip=self.host,
                                                  port=8088,
                                                  path=self.server.device_xml_path)
        return path

    def run(self):
        self.server.serve_forever()
