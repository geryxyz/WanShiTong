from ..module_basehandler import ModulebaseHandler
from src.wst.utils.intermediate import *

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        fid = self.get_argument("folderid", None)
        if(fid is None):
            self.get_warn("danger", "Invalid folder id has been given!")
            self.render("edit_folder.html")
            return
        try:
            Processor.deleteFolder(fid)
        except NotImplementedError:
            self.get_warn("primary", "Delete function coming soon!")

        self.render("index.html", handler=self)
