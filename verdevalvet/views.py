from django.shortcuts import render
from django.shortcuts import redirect
from verdevalvet.Controller.Database import *
from django.http import HttpResponseRedirect


# Create your view{%  %}here.
def index(request):
    DataEvent = Database.DataEvent(request)[:4]
    DataArtis = Database.DataArtis(request)
    return render(request, 'index.html', {'Event': DataEvent, 'Artis': DataArtis})

def my_ticket(request):
    # Ambil data dari form POST
    nama = request.POST.get('nama')
    sesi = request.POST.get('sesi')
    acara = request.POST.get('acara')
    nomor_kursi = request.POST.get('nomor_kursi')
    harga = request.POST.get('harga')
    
    # Ambil data dari Database
    DataEvent = Database.DataEvent(request)
    DataKursi = Database.DataKursi(request)
    SesiKonser = Database.SesiKonser(request)
    
    # Cari data event dan kursi berdasarkan input
    event_info =  [event for event in DataEvent if event['id'] == int(acara)]
    sesi_info =  [event for event in SesiKonser if event['id'] == int(sesi)]
    kursi_info = next((kursi for kursi in DataKursi if kursi['nomor'] == nomor_kursi), None)
    
    # Menyimpan data ke dalam session
    request.session['nama'] = nama
    request.session['sesi'] = sesi
    request.session['acara'] = acara
    request.session['nomor_kursi'] = nomor_kursi
    request.session['harga'] = harga
    request.session['event_info'] = event_info
    request.session['kursi_info'] = kursi_info

    # Kirim data ke template untuk ditampilkan
    return render(request, 'pages/cetakTiket.html', {
        'informasi': DataEvent,
        'nama': nama,
        'sesi': sesi_info,
        'acara': acara,
        'nomor_kursi': nomor_kursi,
        'harga': harga,
        'event_info': event_info,
        'kursi_info': kursi_info
    })

def checkout(request):
    # Mengambil data paket berdasarkan ID
    DataPaket = Database.DataPaket(request) 
    DataEvent =  Database.DataEvent(request) 
    DataKursi =  Database.DataKursi(request) 
    SesiKonser = Database.SesiKonser(request)
    
    
    return render(request, 'pages/pesanTiket.html', {'kategori': DataPaket, 'infoEvent': DataEvent, 'kursi': DataKursi, 'Sesi':SesiKonser})
def about(request, id):
    # Ambil data event berdasarkan ID
    event_detail = [event for event in Database.DataEvent(request) if event['id'] == id]
    paket = Database.DataPaket(request)
    # Mengambil list komentar dari session untuk ditampilkan di template
    comment = request.session.get('comment', [])
    
    return render(request, 'pages/aboutEvent.html', {'event': event_detail, 'comment': comment, 'paket': paket})

def addComment(request, id):
    email = request.POST.get('email')
    pesan = request.POST.get('pesan')
    # Mengambil list komentar dari session atau membuat list baru jika belum ada
    # Membuat batasan maksimal 5 komentar
    comment = request.session.get('comment', [])[:4]
    
    # Menambahkan komentar baru ke dalam list
    comment.insert(0, {
        'email': email,
        'pesan': pesan,
    })
    
    # Menyimpan list kome{%  %}ar yang telah diperbarui ke dalam session
    request.session['comment'] = comment
    return redirect('about_event', id)
