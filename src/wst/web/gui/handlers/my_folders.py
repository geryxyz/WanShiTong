from ..module_basehandler import ModulebaseHandler
from src.wst.utils import *


# Its the same as folder browsing
class Index(ModulebaseHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world")
        # self.content_template = 'content/folders.html'
        # self.render("index.html", handler=self)
        self.folder_processor = Processor(Folder)
        self.content_processor = Processor(Folder_Content)
        if "my_folders/folders" in self.request.uri:
            try:
                self.get_folder_content(self.get_argument("fid", None))
            except ValueError:
                raise NotImplementedError()
        else:
            self.fid = -1
            folder_filters = []
            content_filters = []
            folder_filters.append(Processor.str2filter(Folder, "Equals", "userid", self.userid))
            folder_filters.append(Processor.str2filter(Folder, "Equals", "parent", -1))

            # content_filters.append(Processor.str2filter(Folder_Content, "Equals", "userid", self.userid))
            self.folder_processor.filter(folder_filters)
            self.folder_processor.logic([And()])
            # self.content_processor.filter(content_filters)
            self.folders = self.folder_processor.get_result()
            self.content = []
            # content = self.content_processor.get_result()
            # self.folder_processor
            #first request from the page
            # self.render("elements/folders/folder_to_list.html")
            uri = self.request.uri
            split = uri.split('/')
            if("iframe" in uri):
                self.render("folders_to_iframe.html")
                return
            self.render("my_folders.html")
        if (self.userid is None):
            self.redirect("/index")

    def get_folder_content(self, folder_id):
        if (folder_id is None):
            raise ValueError("Bad request has been received!")
        filters = []
        self.fid = folder_id
        filters.append(Processor.str2filter(Folder, "Equals", "parent", int(folder_id)))
        filters.append(Processor.str2filter(Folder, "Equals", "userid", int(self.userid)))
        self.folder_processor.filter(filters)
        self.folder_processor.logic([And()])
        self.folders = self.folder_processor.get_result()

        content_filters = []
        content_filters.append(Processor.str2filter(Folder_Content, "Equals", "folder", int(folder_id)))
        try:
            self.content_processor.filter(content_filters)
            self.content = self.content_processor.get_result()
            filters = []
            logic = []
            for i in self.content:
                filters.append(Processor.str2filter(Processor.str2entry(i.entry_type), "matchwith", "citekey", i.citekey))
                logic.append(Or())
            logic.pop(0)
            nameProcessor = Processor(Article)
            nameProcessor.filter(filters)
            nameProcessor.logic(logic)
            self.names = nameProcessor.get_result()
            self.namess = {}
            for i in self.names:
                self.namess[i.citekey] = i.title
        except ZeroResultException:
            self.content = []
        self.render("elements/folders/folder_to_list.html")
        return
