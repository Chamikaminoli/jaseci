def load_standard():
    import jaseci.actions.standard.net  # noqa
    import jaseci.actions.standard.rand  # noqa
    import jaseci.actions.standard.request  # noqa
    import jaseci.actions.standard.std  # noqa
    import jaseci.actions.standard.file  # noqa
    import jaseci.actions.standard.vector  # noqa
    import jaseci.actions.standard.date  # noqa
    import jaseci.actions.standard.jaseci  # noqa
    import jaseci.actions.standard.mail  # noqa


# from .utils.jsorc import jsorc_start
from .utils.utils import logger

# jsorc_start()

load_standard()
