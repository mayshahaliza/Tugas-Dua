Link tugas heroku: https://mayshatugas2.herokuapp.com/

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
Jawab: user --> urls --> views --> models --> database --> models dan views --> template HTML --> user

Pertama, client mengirim permintaan menuju server Django, kemudian permintaan ini akan diproses melalui urls kemudian akan diteruskan ke views. Views didefinisikan oleh pengembang untuk memproses permintaan yang didapat. Views akan memanggil query ke models untuk proses yang memerlukan database. Setalah itu, models akan melakukan transaksi data dengan database dan database akan mengembalikan hasil query menuju models dan views. Kemudian, views akan memetakan hasil tersebut ke dalam HTML. HTML tersebut kemudian akan diberikan kepada user.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab: Virtual environment perlu diaktifkan untuk mengisolasi package dan dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain dalam komputer. Aplikasi web berbasis django dapat dibuat tanpa virtual environment, tetapi tidak sesuai best practice yang dianjurkan, seperti kasus di mana requirements.txt digunakan bersamaan dengan virtual environment.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Jawab:

Langkah 1: Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML
Dalam views.py, ditambahkan fungsi dan import sebagai berikut:
    from django.urls import path
    from katalog.models import CatalogItem
    def show_katalog(request):
        data_katalog_item = CatalogItem.objects.all()
        context = {
        'list_item': data_katalog_item,
        'name': 'Maysha Haliza Kirana'
        }
        return render(request, "katalog.html", context)

Langkah 2: Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py
Dalam urls.py di folder katalog, ditambahkan fungsi dan import sebagai berikut:
    from katalog.views import show_katalog

    app_name = 'katalog'

    urlpatterns = [
        path('', show_katalog, name='show_katalog'),
    ]

Dalam urls.py di folder project_django, ditambahkan juga potongan kode berikut pada variabel urlpatterns
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('example_app.urls')),
        path('katalog/', include('katalog.urls'))
    ]

Kemudian, dijalankan python manage.py runserver dan membuka http://localhost:8000/katalog/

Langkah 3: Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template
Mengubah isi dari katalog.html untuk tampilan web

Langkah 4: Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
Mengubah file Procfile dengan:
    web: gunicorn katalog.wsgi --log-file -

Kemudian melakukan add, commit, dan push ke gitHub. Setelah itu, menyalin API key dan nama app di heroku yang telah dibuat dalam file teks dengan isi:
    HEROKU_API_KEY: *key API*
    HEROKU_APP_NAME: *nama app*

    # ditulis dengan key API dan nama app yang dibuat

Kemudian, menambahkan repository secret baru dengan name: nama app heroku dan value: key API. Untuk melakukan hal ini, dalam github, akses settings --> secrets --> actions, kemudian simpan variabel yang dibuat. Jalankan kembali workflownya, dan buka halaman https://<nama-aplikasi-heroku>.herokuapp.com (diisi dengan nama app di heroku). Jika status deployment berhasil, aplikasi dapat diakses.