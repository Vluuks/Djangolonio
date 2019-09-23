from someapp.models import Category, Product

c = Category(name="test", description="test2")
c.save()
p = Product(category=c, name="test", price=1, inventory=1, description="blablabla")
p.save()
