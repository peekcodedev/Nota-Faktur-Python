from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Tulisan "FAKTUR PEEKCODE" di tengah
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'FAKTUR PEEKCODE', 0, 1, 'C')
        
        # Deskripsi Toko di tengah
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'Service Laptop & Jasa Perbaiki Error', 0, 1, 'C')
        
        # Garis bawah tebal double
        self.set_line_width(1)
        self.line(10, 30, 200, 30)
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
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Informasi Pembeli:', 0, 1)
    pdf.set_font('Arial', '', 12)
    for key, value in invoice_data['buyer'].items():
        pdf.cell(0, 10, f'{key}: {value}', 0, 1)

    # Garis Pembatas
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)

    # Daftar Barang
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Daftar Barang:', 0, 1)
    
    pdf.set_font('Arial', 'B', 10)
    col_widths = [60, 30, 50, 50]
    headers = ['Nama Barang', 'Jumlah Barang', 'Harga Satuan (Rp.)', 'Total Harga (Rp.)']
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, 'C')
    pdf.ln(10)
    
    pdf.set_font('Arial', '', 10)
    for item in invoice_data['items']:
        pdf.cell(col_widths[0], 10, item['Nama Barang'], 1)
        pdf.cell(col_widths[1], 10, str(item['Qty']), 1)
        pdf.cell(col_widths[2], 10, f"{item['Harga']:.2f}", 1)
        pdf.cell(col_widths[3], 10, f"{item['Qty'] * item['Harga']:.2f}", 1)
        pdf.ln(10)

    # Garis Pembatas
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)

    # Total Pembayaran
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'Total Pembayaran: {invoice_data["total"]:.2f}', 0, 1)

    # Menyimpan file PDF
    pdf.output(name=filename, dest='F')

if __name__ == '__main__':
    create_invoice()
