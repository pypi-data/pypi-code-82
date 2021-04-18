import io
import logging

from PIL import Image

from pyscreenshot.plugins.backend import CBackend

log = logging.getLogger(__name__)


class PySide2BugError(Exception):
    pass


app = None


class PySide2GrabWindow(CBackend):
    name = "pyside2"

    def grab_to_buffer(self, buff, file_type="png"):
        from PySide2 import QtGui
        from PySide2 import QtCore
        from PySide2 import QtWidgets

        QApplication = QtWidgets.QApplication
        QBuffer = QtCore.QBuffer
        QIODevice = QtCore.QIODevice
        QScreen = QtGui.QScreen
        # QPixmap = self.PySide2.QtGui.QPixmap

        global app
        if not app:
            app = QApplication([])
        qbuffer = QBuffer()
        qbuffer.open(QIODevice.ReadWrite)
        QScreen.grabWindow(
            QApplication.primaryScreen(), QApplication.desktop().winId()
        ).save(qbuffer, file_type)
        # https://stackoverflow.com/questions/52291585/pyside2-typeerror-bytes-object-cannot-be-interpreted-as-an-integer
        buff.write(qbuffer.data().data())
        qbuffer.close()

    def grab(self, bbox=None):
        strio = io.BytesIO()
        self.grab_to_buffer(strio)
        strio.seek(0)
        im = Image.open(strio)
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        import PySide2

        return PySide2.__version__
