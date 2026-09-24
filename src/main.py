def tambah_cart(cart, produk):
    cart.append(produk)
    return "Produk berhasil ditambahkan ke cart"


cart = []

print(tambah_cart(cart, "Laptop"))
print(cart)