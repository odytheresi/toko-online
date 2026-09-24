def checkout(cart_items):
    if len(cart_items) > 0:
        return "Checkout berhasil"
    else:
        return "Keranjang kosong"