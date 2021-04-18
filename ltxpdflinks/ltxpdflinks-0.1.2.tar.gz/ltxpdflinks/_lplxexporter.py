import os
import os.path
import re
import string
import datetime

import logging
logger = logging.getLogger(__name__)

from . import __version__ as version_str


_ltx_arg_safe = r'-:;&?/.+=^_\[\]' + string.ascii_letters + string.digits

_rx_escape = re.compile(
    r'(?:(?P<pc>%(?P<pchex>[a-fA-F0-9]{2}))|(?P<char>[^'+_ltx_arg_safe+']))'
)

def _makeltxsafe(s):
    def _do_replace(m):
        if m.group('pc'):
            # use \lplxHexChar{FF} instead
            return r'\lplxHexChar{'+m.group('pchex')+'}'
        return r'\lplxHexChar{%02x}'%(ord(m.group()))
    return _rx_escape.sub(_do_replace, s)


class LplxPictureEnvExporter:
    def __init__(self, *, include_comments_catcode=False):
        super().__init__()
        self.include_comments_catcode = include_comments_catcode

    def export(self, extractedgraphiclinks):
        e = extractedgraphiclinks # shorthand
        graphic_basefname, graphic_ext = os.path.splitext(e.graphic_fname)

        s = ""

        if self.include_comments_catcode:
            s += r"""\catcode`\%=14\relax""" + "\n"

        s += (
r"""% Automatically generated by ltxpdflinks """ + version_str + r""" on """ +
            datetime.datetime.now().isoformat() + r"""
%
% LPLX - """ + _makeltxsafe(e.graphic_fname) + r"""
%
\LPLX{version=0,ltxpdflinksversion={""" + version_str +
            r"""},features={bbox}}{%
\lplxGraphic{""" + _makeltxsafe(graphic_basefname) + r"""}{"""
            + _makeltxsafe(graphic_ext) + r"""}%
\lplxUserSpaceUnitLength{""" + e.unitlength + r"""}%
\lplxSetBbox{0}{0}""" + "{{{:.6g}}}{{{:.6g}}}".format(e.size[0], e.size[1]) + r"""%
%%BoundingBox: 0 0 """ + "{:d} {:d}".format(int(e.size[0]+0.5), int(e.size[1]+0.5)) + r"""
%%HiResBoundingBox: 0 0 """ + "{:.6g} {:.6g}".format(e.size[0], e.size[1]) + r"""
\lplxPicture{%
"""
        )

        for el in e.links:
            x, y, w, h = el.link_bbox
            if el.link_type == 'URI':
                s2 = r"""\href{{{tgt}}}""".format(tgt=_makeltxsafe(el.link_target))
            elif el.link_type == 'latex-ref':
                s2 = r"""\hyperref[{{{tgt}}}]""".format(tgt=_makeltxsafe(el.link_target))
            elif el.link_type == 'latex-cite':
                s2 = r"""\hyperlink{{cite.{tgt}}}""".format(tgt=_makeltxsafe(el.link_target))
            else:
                logger.warning("Ignoring link with unsupported link_type: %r", el)
                continue

            # s += (
            #     r"\put({x},{y})".format(x=el.link_bbox[0], y=el.link_bbox[1]) +
            #     "{" + s2 + "}\n"
            # )
            s += (
                r"\lplxPutLink{{{x:.8g}}}{{{y:.8g}}}{{{w:.8g}}}{{{h:.8g}}}{{{hrstart}}}{{{hrend}}}"
                .format(x=x, y=y, w=w, h=h, hrstart=s2, hrend='')
                + r"%" + "\n"
            )

        s += r"""}}%""" + "\n"
        
        return s
