from crud import CRUDCategory


category = CRUDCategory.get(category_id=1)
print(category)
category.name = "Еда"
category.parent_id = None
CRUDCategory.update(category=category)
print(CRUDCategory.get(category_id=1))


