

class Database:
    def SesiKonser(request):
        sesi_konser = [
            {'id': 1, 'nama': 'Sesi Siang', 'waktu': '13:00 - 16:00' },
            {'id': 2, 'nama': 'Sesi Malam', 'waktu': '19:00 - 22:00' },
            {'id': 3, 'nama': 'Sesi Siang', 'waktu': '13:00 - 16:00' },
            {'id': 4, 'nama': 'Sesi Malam', 'waktu': '19:00 - 22:00'},
            {'id': 5, 'nama': 'Sesi Siang', 'waktu': '13:00 - 16:00'},
            {'id': 6, 'nama': 'Sesi Malam', 'waktu': '19:00 - 22:00'},
        ]
        return sesi_konser
    def DataKursi(request):
        nomor_kursi = [
            {'id': 1, 'nomor': ['A1', 'A2', 'A3', 'A4', 'A5'], 'kategori': 'VIP', 'status': 'tersedia'},
            {'id': 2, 'nomor': ['B1', 'B2', 'B3', 'B4', 'B5'], 'kategori': 'Premium', 'status': 'tersedia'},
            {'id': 3, 'nomor': ['C1', 'C2', 'C3', 'C4', 'C5'], 'kategori': 'Basic', 'status': 'tersedia'},
        ]
        return nomor_kursi
    
    def DataPaket(request):
        tbl_paket = [
            {'id': 1, 'grade': 'vip', 'harga': 3000000},
            {'id': 2, 'grade': 'premium', 'harga': 1000000},
            {'id': 3, 'grade': 'basic', 'harga': 700000},
        ]
        return tbl_paket
    def DataEvent(request):
        
        tbl_event =  [
            {'id': 1, 'nama': 'Ramadhan Berbahagia', 'deskripsi': 'Acara ini akan menghadirkan berbagai penampilan musik dan tarian yang akan membuat Anda berbahagia.', 'time': '15 juni 2025', 'bangunan': 'Gelora Bung Karno', 'alamat': 'Jalan Pintu 1 Senayan, Gelora, Tanah Abang, Jakarta Pusat, DKI Jakarta 10270', 'poster': 'https://png.pngtree.com/thumb_back/fw800/background/20230321/pngtree-stage-concert-background-gold-image_2050942.jpg', 'artis': ['Tulus', 'Agnez Mo', 'Isyana Sarasvati']},
            {'id': 2, 'nama': 'Akbar Gebyar', 'deskripsi': 'Akbar Gebyar adalah acara yang paling ditunggu-tunggu di tahun ini. Dengan penampilan musik yang sangat beragam, Anda tidak akan kecewa.', 'time': '20 juli 2025', 'bangunan': 'Stadion Utama Gelora Bung Karno', 'alamat': 'Jalan Pintu 1 Senayan, Gelora, Tanah Abang, Jakarta Pusat, DKI Jakarta 10270', 'poster': 'https://png.pngtree.com/background/20210715/original/pngtree-creative-carnival-music-festival-hd-background-picture-image_1318639.jpg', 'artis': ['Raisa', 'Judika', 'Maliq & D’Essentials']},
            {'id': 3, 'nama': 'Senayan Berpesta', 'deskripsi': 'Senayan Berpesta adalah acara yang akan menghadirkan berbagai penampilan musik dan tarian yang sangat beragam dan menarik.', 'time': '25 agustus 2025', 'bangunan': 'Lapangan D Senayan', 'alamat': 'Jalan Jenderal Sudirman, Senayan, Kebayoran Baru, Jakarta Selatan, DKI Jakarta 12190', 'poster': 'https://1.bp.blogspot.com/-4JBNfe_H6PQ/YD5giaQTVGI/AAAAAAAABoA/PpWIew4qnQgHvvv0NlaDM5ZU017UPrNKACLcBGAsYHQ/s1200/konser.jpg', 'artis': ['Ariel NOAH', 'Bunga Citra Lestari', 'Gigi']},
            {'id': 4, 'nama': 'Jakarta Berpesta', 'deskripsi': 'Jakarta Berpesta adalah acara yang paling ditunggu-tunggu di Jakarta. Dengan penampilan musik yang sangat beragam, Anda tidak akan kecewa.', 'time': '10 september 2025', 'bangunan': 'Taman Mini Indonesia Indah', 'alamat': 'Jalan Raya Taman Mini Indonesia Indah, Pinang Ranti, Makasar, Jakarta Timur, DKI Jakarta 13560', 'poster': 'https://img.freepik.com/premium-vector/music-event-banner-design-template-festival-concert-party_85212-64.jpg?w=1380', 'artis': ['Yura Yunita', 'Danilla Riyadi', 'Padi Reborn']},
            {'id': 5, 'nama': 'Festival Musik Jakarta', 'deskripsi': 'Festival Musik Jakarta adalah acara yang akan menghadirkan berbagai penampilan musik dari berbagai genre.', 'time': '15 oktober 2025', 'bangunan': 'Gelora Bung Karno', 'alamat': 'Jalan Pintu 1 Senayan, Gelora, Tanah Abang, Jakarta Pusat, DKI Jakarta 10270', 'poster': 'https://png.pngtree.com/thumb_back/fw800/background/20230321/pngtree-stage-concert-background-gold-image_2050942.jpg', 'artis': ['Noah', 'Tulus', 'Ari Lasso']},
            {'id': 6, 'nama': 'Konser Amal', 'deskripsi': 'Konser Amal adalah acara yang diadakan untuk mengumpulkan dana bagi korban bencana alam.', 'time': '20 november 2025', 'bangunan': 'Stadion Utama Gelora Bung Karno', 'alamat': 'Jalan Pintu 1 Senayan, Gelora, Tanah Abang, Jakarta Pusat, DKI Jakarta 10270', 'poster': 'https://png.pngtree.com/background/20210715/original/pngtree-creative-carnival-music-festival-hd-background-picture-image_1318639.jpg', 'artis': ['Agnez Mo', 'Raisa', 'Andien']},
            {'id': 7, 'nama': 'Festival Budaya', 'deskripsi': 'Festival Budaya adalah acara yang akan menghadirkan berbagai penampilan budaya dari berbagai daerah di Indonesia.', 'time': '25 desember 2025', 'bangunan': 'Lapangan D Senayan', 'alamat': 'Jalan Jenderal Sudirman, Senayan, Kebayoran Baru, Jakarta Selatan, DKI Jakarta 12190', 'poster': 'https://1.bp.blogspot.com/-4JBNfe_H6PQ/YD5giaQTVGI/AAAAAAAABoA/PpWIew4qnQgHvvv0NlaDM5ZU017UPrNKACLcBGAsYHQ/s1200/konser.jpg', 'artis': ['Batik Keris', 'Kerispatih', 'Slank']},
            {'id': 8, 'nama': 'Pesta Rakyat', 'deskripsi': 'Pesta Rakyat adalah acara yang diadakan untuk memperingati hari kemerdekaan Indonesia.', 'time': '17 agustus 2025', 'bangunan': 'Taman Mini Indonesia Indah', 'alamat': 'Jalan Raya Taman Mini Indonesia Indah, Pinang Ranti, Makasar, Jakarta Timur, DKI Jakarta 13560', 'poster': 'https://img.freepik.com/premium-vector/music-event-banner-design-template-festival-concert-party_85212-64.jpg?w=1380', 'artis': ['Gigi', 'Iwan Fals', 'The Titans']},
            {'id': 9, 'nama': 'Festival Film', 'deskripsi': 'Festival Film adalah acara yang akan menghadirkan berbagai film dari berbagai genre.', 'time': '10 januari 2026', 'bangunan': 'Gelora Bung Karno', 'alamat': 'Jalan Pintu 1 Senayan, Gelora, Tanah Abang, Jakarta Pusat, DKI Jakarta 10270', 'poster': 'https://png.pngtree.com/thumb_back/fw800/background/20230321/pngtree-stage-concert-background-gold-image_2050942.jpg', 'artis': ['Vino G. Bastian', 'Reza Rahadian', 'Titi Kamal']},
            {'id': 10, 'nama': 'Pesta Musik', 'deskripsi': 'Pesta Musik adalah acara yang akan menghadirkan berbagai penampilan musik dari berbagai genre.', 'time': '15 februari 2026', 'bangunan': 'Stadion Utama Gelora Bung Karno', 'alamat': 'Jalan Pintu 1 Senayan, Gelora, Tanah Abang, Jakarta Pusat, DKI Jakarta 10270', 'poster': 'https://png.pngtree.com/background/20210715/original/pngtree-creative-carnival-music-festival-hd-background-picture-image_1318639.jpg', 'artis': ['Rizky Febian', 'Isyana Sarasvati', 'Vidi Aldiano']},
        ]

        return tbl_event
    def DataArtis(request):
        tbl_artis = [
            {'id' : 1, 'nama': 'Baskara', 'Motivasi': 'Selalu berusaha untuk memberikan yang terbaik dalam setiap penampilan.', 'Photo': 'https://i.pinimg.com/736x/4e/01/3d/4e013d4407878f38fa925409ae5effea.jpg'},
            {'id' : 2, 'nama': 'Raisa', 'Motivasi': 'Musik adalah cara saya mengekspresikan diri dan menyentuh hati orang lain.', 'Photo': 'https://highlight.id/wp-content/uploads/2018/11/Highlight_daftar-nama-penyanyi-wanita-perempuan-solo-indonesia-ngehits-terkenal-populer_01-681x681.jpg'},
            {'id' : 3, 'nama': 'Afgan', 'Motivasi': 'Saya percaya bahwa setiap lagu memiliki cerita yang bisa menginspirasi banyak orang.', 'Photo': 'https://lastfm.freetls.fastly.net/i/u/ar0/3892f5228d633edf7186860d2ebe4901.jpg'},
            {'id' : 4, 'nama': 'Bernadya', 'Motivasi': 'Saya ingin menjadi suara bagi generasi muda dan menyebarkan pesan positif.', 'Photo': 'https://statik.tempo.co/data/2024/09/25/id_1339871/1339871_720.jpg'},
            {'id' : 5, 'nama': 'Dewi Sandra', 'Motivasi': 'Saya berharap musik saya dapat menginspirasi orang lain untuk menjadi lebih baik.', 'Photo': 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Dewi_Sandra_2011.jpg'},
        ]
        return tbl_artis