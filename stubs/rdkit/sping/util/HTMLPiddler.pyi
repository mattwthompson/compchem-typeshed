from types import *
import htmllib
from typing import Any

TRACE: int

class HTMLPiddler:
    html: Any
    start: Any
    xLimits: Any
    font: Any
    color: Any
    def __init__(self, html: str = ..., start=..., xLimits=..., font: Any | None = ..., color: Any | None = ...) -> None: ...
    def renderOn(self, aPiddleCanvas) -> None: ...

class _HtmlParser(htmllib.HTMLParser):
    def anchor_bgn(self, href, name, type) -> None: ...
    def anchor_end(self) -> None: ...

class _HtmlPiddleWriter:
    FontSizeDict: Any
    DefaultFontSize: int
    piddler: Any
    pc: Any
    anchor: Any
    lineHeight: int
    atbreak: int
    color: Any
    defaultFont: Any
    fsizex: Any
    fsizey: Any
    indentSize: Any
    indent: Any
    def __init__(self, aHTMLPiddler, aPiddleCanvas) -> None: ...
    oldcolor: Any
    def anchor_bgn(self, href, name, type) -> None: ...
    def anchor_end(self) -> None: ...
    font: Any
    def new_font(self, fontParams) -> None: ...
    def new_margin(self, margin, level) -> None: ...
    def new_spacing(self, spacing) -> None: ...
    def new_styles(self, styles) -> None: ...
    def send_label_data(self, data) -> None: ...
    y: Any
    def send_paragraph(self, blankline) -> None: ...
    oldLineHeight: Any
    x: Any
    def send_line_break(self) -> None: ...
    def send_hor_rule(self) -> None: ...
    def send_literal_data(self, data) -> None: ...
    def send_flowing_data(self, data) -> None: ...
    def OutputLine(self, text, linebreak: int = ...) -> None: ...

__copyrite_jim__: str
DEMO_HTML: str

def demoPDF(html) -> None: ...
def demoPIL(html) -> None: ...
def demoTK(html) -> None: ...
def demoWX(html) -> None: ...
def demo(html=...) -> None: ...
