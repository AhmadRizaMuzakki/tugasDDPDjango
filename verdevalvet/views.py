from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def checkout(request):
    # Mengumpulkan data dari form yang dikirimkan
    nama = request.POST.get('nama')
    tanggal = request.POST.get('tanggal')
    hari = request.POST.get('hari')
    paket = request.POST.get('paket')
    
    # Membuat dictionary untuk menyimpan data tiket
    data_tiket = {
        'nama': nama,
        'tanggal': tanggal,
        'hari': hari,
        'paket': paket,
    }
    
    # Menyimpan data tiket ke dalam session
    request.session['data_tiket'] = data_tiket
    
    # Mengambil data tiket dari session untuk digunakan dalam template
    InfoTiket = request.session.get('data_tiket', {})
    
    # Mengembalikan render dengan data tiket yang telah diambil
    return render(request, 'Tiket.html', {'InfoTiket': InfoTiket})

def feedback(request):
    return
def my_ticket(request):
    return
def events(request):
    return
def contact(request):
    return

