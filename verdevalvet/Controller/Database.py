

class Database:
    
    def DataEvent(request):
        tbl_event = [
            {'id': 1, 'nama': 'Ramadhan Berbahagia', 'deskripsi': 'Acara ini akan menghadirkan berbagai penampilan musik dan tarian yang akan membuat Anda berbahagia.', 'time': '15 juni 2025', 'tempat': 'Gelora Bung Karno', 'poster': 'https://png.pngtree.com/thumb_back/fw800/background/20230321/pngtree-stage-concert-background-gold-image_2050942.jpg'},
            {'id': 2, 'nama': 'Akbar Gebyar', 'deskripsi': 'Akbar Gebyar adalah acara yang paling ditunggu-tunggu di tahun ini. Dengan penampilan musik yang sangat beragam, Anda tidak akan kecewa.', 'time': '20 juli 2025', 'tempat': 'Stadion Utama Gelora Bung Karno', 'poster': 'https://png.pngtree.com/background/20210715/original/pngtree-creative-carnival-music-festival-hd-background-picture-image_1318639.jpg'},
            {'id': 3, 'nama': 'Senayan Berpesta', 'deskripsi': 'Senayan Berpesta adalah acara yang akan menghadirkan berbagai penampilan musik dan tarian yang sangat beragam dan menarik.', 'time': '25 agustus 2025', 'tempat': 'Lapangan D Senayan', 'poster': 'https://1.bp.blogspot.com/-4JBNfe_H6PQ/YD5giaQTVGI/AAAAAAAABoA/PpWIew4qnQgHvvv0NlaDM5ZU017UPrNKACLcBGAsYHQ/s1200/konser.jpg'},
            {'id': 4, 'nama': 'Jakarta Berpesta', 'deskripsi': 'Jakarta Berpesta adalah acara yang paling ditunggu-tunggu di Jakarta. Dengan penampilan musik yang sangat beragam, Anda tidak akan kecewa.', 'time': '10 september 2025', 'tempat': 'Taman Mini Indonesia Indah', 'poster': 'https://img.freepik.com/premium-vector/music-event-banner-design-template-festival-concert-party_85212-64.jpg?w=1380'},
            {'id': 5, 'nama': 'Festival Musik Jakarta', 'deskripsi': 'Festival Musik Jakarta adalah acara yang akan menghadirkan berbagai penampilan musik dari berbagai genre.', 'time': '15 oktober 2025', 'tempat': 'Gelora Bung Karno', 'poster': 'https://png.pngtree.com/thumb_back/fw800/background/20230321/pngtree-stage-concert-background-gold-image_2050942.jpg'},
            {'id': 6, 'nama': 'Konser Amal', 'deskripsi': 'Konser Amal adalah acara yang diadakan untuk mengumpulkan dana bagi korban bencana alam.', 'time': '20 november 2025', 'tempat': 'Stadion Utama Gelora Bung Karno', 'poster': 'https://png.pngtree.com/background/20210715/original/pngtree-creative-carnival-music-festival-hd-background-picture-image_1318639.jpg'},
            {'id': 7, 'nama': 'Festival Budaya', 'deskripsi': 'Festival Budaya adalah acara yang akan menghadirkan berbagai penampilan budaya dari berbagai daerah di Indonesia.', 'time': '25 desember 2025', 'tempat': 'Lapangan D Senayan', 'poster': 'https://1.bp.blogspot.com/-4JBNfe_H6PQ/YD5giaQTVGI/AAAAAAAABoA/PpWIew4qnQgHvvv0NlaDM5ZU017UPrNKACLcBGAsYHQ/s1200/konser.jpg'},
            {'id': 8, 'nama': 'Pesta Rakyat', 'deskripsi': 'Pesta Rakyat adalah acara yang diadakan untuk memperingati hari kemerdekaan Indonesia.', 'time': '17 agustus 2025', 'tempat': 'Taman Mini Indonesia Indah', 'poster': 'https://img.freepik.com/premium-vector/music-event-banner-design-template-festival-concert-party_85212-64.jpg?w=1380'},
            {'id': 9, 'nama': 'Festival Film', 'deskripsi': 'Festival Film adalah acara yang akan menghadirkan berbagai film dari berbagai genre.', 'time': '10 januari 2026', 'tempat': 'Gelora Bung Karno', 'poster': 'https://png.pngtree.com/thumb_back/fw800/background/20230321/pngtree-stage-concert-background-gold-image_2050942.jpg'},
            {'id': 10, 'nama': 'Pesta Musik', 'deskripsi': 'Pesta Musik adalah acara yang akan menghadirkan berbagai penampilan musik dari berbagai genre.', 'time': '15 februari 2026', 'tempat': 'Stadion Utama Gelora Bung Karno', 'poster': 'https://png.pngtree.com/background/20210715/original/pngtree-creative-carnival-music-festival-hd-background-picture-image_1318639.jpg'},
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