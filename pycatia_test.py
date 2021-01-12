from pycatia import CATIAApplication

class CatiaList():
    def __init__(self):
        super(CatiaList, self).__init__()
        self.init()

    def init(self):
        try:
            catia = CATIAApplication()
            documents = catia.documents()
            # documents.open(r'D:\\draw\\test2\\COL-UPR HSG ASSY (MSCL)-0000001.CATProduct')
            documents.open(r'D:\\util\\new_ny_CADIG\\_CheckOut\\CAV513242_00_1223_095553\\00.U_JOINT ASSY.CATProduct')
            document = catia.document()
            product = document.product()

            self.products = product.get_products()
            if len(self.products) == 0:
                print("no children || no product file")
            else:
                while len(self.products) != 0:
                    # print(self.products)
                    self.Recur(self.products[0])
                    del self.products[0]
        except Exception as e:
            print(e)
        finally:
            document.close()

    def Recur(self, item):
        file_type = item.file_name[item.file_name.rfind('.'):]
        if file_type == '.CATPart':
            print(item.file_name)
        elif file_type == '.CATProduct':
            print(item.file_name)
            if item.has_children():
                self.products.extend(item.get_children())


CatiaList()