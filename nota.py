from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'NOTA FAKTUR', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Halaman {self.page_no()}', 0, 0, 'C')

def create_invoice():
    buyer_name = input("Masukkan Nama Pembeli: ")
    buyer_address = input("Masukkan Alamat Pembeli: ")
    buyer_city = input("Masukkan Kota Pembeli: ")

    items = []
    while True:
        item_name = input("Masukkan Nama Barang (atau ketik 'selesai' untuk selesai): ")
        if item_name.lower() == 'selesai':
            break
        item_qty = int(input("Masukkan Jumlah Barang: "))
        item_price = float(input("Masukkan Harga Barang per Item: "))
        items.append({'Nama Barang': item_name, 'Qty': item_qty, 'Harga': item_price})

    total = sum(item['Qty'] * item['Harga'] for item in items)

    invoice_data = {
        'buyer': {
            'Nama': buyer_name,
            'Alamat': buyer_address,
            'Kota': buyer_city
        },
        'items': items,
        'total': total
    }

    filename = input("Masukkan nama file PDF untuk menyimpan invoice (misalnya 'invoice.pdf'): ")
    if not filename.endswith('.pdf'):
        filename += '.pdf'

    pdf = PDF()
    pdf.add_page()

    # Informasi Pembeli
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 10, 'Informasi Pembeli:', 0, 1)
    pdf.set_font('Arial', '', 10)
    for key, value in invoice_data['buyer'].items():
        pdf.cell(0, 10, f'{key}: {value}', 0, 1)

    # Daftar Barang
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 10, 'Daftar Barang:', 0, 1)
    pdf.set_font('Arial', '', 10)
    col_width = pdf.w / 4
    for item in invoice_data['items']:
        for i, (key, value) in enumerate(item.items()):
            pdf.cell(col_width, 10, str(value), border=1)
        pdf.ln(10)

    # Total Pembayaran
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 10, f'Total Pembayaran: {invoice_data["total"]}', 0, 1)

    # Menyimpan file PDF
    pdf.output(name=filename, dest='F')

if __name__ == '__main__':
    create_invoice()