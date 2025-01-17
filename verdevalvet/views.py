from django.shortcuts import render
from verdevalvet.Controller.Database import *

# Create your views here.
def index(request):
    DataEvent = Database.DataEvent(request)[:4]
    DataArtis = Database.DataArtis(request)
    return render(request, 'index.html', {'Event': DataEvent, 'Artis': DataArtis})

def checkout(request):
    # Mengumpulkan data dari form yang dikirimkan
    nama = request.POST.get('nama')
    tanggal = request.POST.get('tanggal')
    hari = request.POST.get('waktu')
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
    return render(request, 'layout/pesanTiket.html', {'InfoTiket': InfoTiket})

def feedback(request):
    return
def my_ticket(request):
    return render(request, 'pages/cetakTiket.html')
def events(request):
    # Mengembalikan render dengan data event

    return render(request, 'pages/aboutEvent.html')

