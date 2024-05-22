from intranet_trems import _
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer


class IArea(Schema):
    """Definição de uma área no TRE-MS."""

    title = schema.TextLine(title=_("Nome Completo"), required=True)
    description = schema.Text(title=_("Biografia"), required=False)


@implementer(IArea)
class Area(Container):
    """Uma área no TRE-MS."""
