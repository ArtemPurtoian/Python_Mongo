from base_mongo import BaseMongo


class CollectionProducts(BaseMongo):
    def __init__(self):
        super().__init__('companies', 'products')
