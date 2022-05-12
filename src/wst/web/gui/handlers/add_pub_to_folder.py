from ..module_basehandler import ModulebaseHandler
from src.wst.utils.intermediate import *

class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        p = Processor(Folder)
        filters = [Processor.str2filter(Folder, "Equals", "userid", self.userid)]
        p.filter(filters)
        self.user_folders = p.get_result()
        self.citekey = self.get_argument("citekey", None)
        folderid = self.get_argument("folderid", None)
        if (folderid is not None and parentid is not None):
            try:
                Processor.makeFolder(folderid, parentid)
            except NotImplementedError:
                self.get_warn("Primary", "Saving publications coming soon!")
        self.buildFolderTree()
        self.render("add_pub_to_folder.html", handler=self)

    def post(self):
        p = Processor(Folder)
        filters = [Processor.str2filter(Folder, "Equals", "userid", self.userid)]
        p.filter(filters)
        self.user_folders = p.get_result()
        self.citekey = self.get_argument("citekey", None)
        folderid = self.get_argument("folderid", None)
        if (folderid is not None and self.citekey is not None):
            try:
                Processor.addPubtoFolder(folderid, self.citekey)
            except NotImplementedError:
                self.get_warn("Primary", "Saving publications coming soon!")
        self.buildFolderTree()
        self.render("add_pub_to_folder.html", handler=self)


    def buildFolderTree(self):
        # dict: id - szülő/gyerek/unoka/folder
        folderlist = {}
        parents = []
        # → kulcs: folderid, érték: self.user_folders tömb indexhelye
        for i in range(0, len(self.user_folders)):
            obj = self.user_folders[i]
            if obj.parent == -1:
                continue
            folderlist[obj.id] = obj
            if (obj.parent not in parents):
                parents.append(obj.parent)
        for i in parents:
            if (i not in folderlist):
                continue
            del (folderlist[i])
        self.trees = []
        self.trees_as_string = {}  # id: the child's id
        for i in self.user_folders:
            self.getParentTree(i)
            # self.getParentTree(folderlist[i])
        var_dump(self.trees_as_string)

        # innentől a folderlistben csak gyermekek vannak

    def getParentTree(self, folder: Folder, list=None):
        if list is None:
            list = []
        list.append(folder)
        if (folder.parent == -1):
            self.trees_as_string[list[0].id] = list
            print(list)
            return
        else:
            for i in self.user_folders:
                # if(i.parent == -1 and len(list) == 1):
                #     print(i)
                if (folder.parent == i.id):
                    return self.getParentTree(i, list)

