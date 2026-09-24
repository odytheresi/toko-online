
produk = [
    {
        "id": 1,
        "nama": "Laptop",
        "harga": 7500000
    },
    {
        "id": 2,
        "nama": "Mouse",
        "harga": 150000
    },
    {
        "id": 3,
        "nama": "Keyboard",
        "harga": 300000
    }
]


def daftar_produk():
    print("=== DAFTAR PRODUK ===")

    for item in produk:
        print(
            f"{item['id']}. "
            f"{item['nama']} - "
            f"Rp{item['harga']:,}"
        )


if __name__ == "__main__":
    daftar_produk()

def tambah_cart(cart, produk):
    cart.append(produk)
    return "Produk berhasil ditambahkan ke cart"


cart = []

print(tambah_cart(cart, "Laptop"))
print(cart)

