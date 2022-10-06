Maysha Haliza Kirana - PBP C - NPM 2106751202 - Tugas 4
Link: https://mayshatugas2.herokuapp.com/todolist/login

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Jawab:
1. {% csrf_token %} diimplementasikan untuk CSRF protection, yaitu untuk melindungi data dari serangan yang ada. Syntax ini akan meng-generate sebuah token dan jika request yang datang tidak mempunyai token ini, request tersebut tidak akan di-execute.

2. Ya, dengan membuat forms secara manual dengan mengimport Form terlebih dahulu dan menginisiasi sebuah kelas form di forms.py (misal class MyForm(forms.Form)). Kemudian, import juga Form dan buat fungsi untuk membuat form di views.py.

3. Pertama, user akan mengirimkan sebuah request dengan mengisi data dan meng-klik tombol submit. Saat itu, user mengirimkan HTTP request berupa 'POST'. Data yang telah diinput user tersebut akan dimasukkan ke dalam database. Untuk menampilkan data-data tersebut dalam HTML, user akan mendapat respons data yang ingin ditampilkan dari database berupa HTTP request 'GET' melalui models dan views.

4. - Membuat aplikasi baru bernama todolist dengan perintah python manage.py startapp todolist
   - Menambahkan todolist dalam settings.py di folder project_django
   - Membuat model Task di models.py di folder todolist sesuai ketentuan (user, title, date, description)
   - Melakukan migrations dengan perintah python manage.py makemigrations dan python manage.py migrate
   - Mengimplementasikan fungsi-fungsi yang diperlukan pada views.py di folder todolist
   - Membuat html todolist, register, login, dan create-task dan mengimplementasikan sesuai ketentuan (untuk todolist.html, memuat tabel task, username pengguna terlogin, dan tombol logout)
   - Melakukan add, commit dan push dan men-deploy ke heroku
   - Membuat dua akun dan membuat minimal tiga task untuk masing-masing akun

REFERENSI
https://www.educative.io/answers/what-is-a-csrf-token-in-django
https://docs.djangoproject.com/en/4.1/topics/forms/

Tugas 5
1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
2. Jelaskan tag HTML5 yang kamu ketahui.
3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Jawab:
1. Inline: mengandung CSS di dalam section body. Hal ini dispesifikasi dengan tag HTML yang digunakan, yakni atribut style.
   Internal: CSS terkandung dalam section head HTML (ter-embedded dengan file HTML)
   External: mengandung file CSS terpisah yang mengandung properti beserta atributnya. CSS disimpan dalam file berbeda dengan HTML menggunakan extension .css dan dihubungkan dengan HTML dengan tag link.
2. Contoh-contoh dari tag HTML5 adalah:
   <head> merupakan bagian awal dari dokumen HTML5 yang biasanya berisikan judul.
   <body> merupakan bagian isi dari dokumen.
   <button> membuat sebuah button.
   <link> menghubungkan dokumen dengan dokumen eksternal.
   <nav> berisi tools untuk navigasi (misal navbar)
   <audio> menambahkan suara dalam dokumen.
   <video> menambahkan video dalam dokumen.
   <time> merepresentasikan waktu dan/atau tanggal.
   <section> mendefinisikan sebuah section dalam dokumen, misal header dan footer.
3. Element selector: menggunakan tag pada HTML sebagai selector, yaitu untuk mengubah properti yang ada dalam tag.
   ID selector: menggunakan ID sebagai selector. ID ditambahkan pada HTMLn kemudian dijadikan selector dalam file CSS.
   Class selector: class ditambahkan pada tag HTML, kemudian class tersebut ditambahkan dalam CSS sebagai selector.
4. Dalam tugas ini, digunakan internal CSS.
   - Dalam CSS, buat class yang akan digunakan untuk body page HTML. Dalam class, banyak hal yang bisa dikustomisasi, seperti warna dan font teks, ukuran teks, dan lain-lain. Semua class ini disimpan dalam section style yang terdapat dalam section head.
   - Membuat card: membuat sebuah class card dalam CSS internal yang berisikan setting untuk membuat daftar todolist menjadi card. Dalam class card, dapat dibuat kustomisasi card, misal ukuran dan warna.
   - menambahkan syntax <meta name="viewport" content="width=device-width, initial-scale=1.0"> untuk membuat page menjadi responsif.

REFERENSI
https://www.geeksforgeeks.org/types-of-css-cascading-style-sheet/
https://www.tutorialrepublic.com/html-reference/html5-tags.php