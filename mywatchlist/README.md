Maysha Haliza K. - PBP C - NPM 2106751202 - Tugas 2
Link tugas heroku: https://mayshatugas2.herokuapp.com/

1. Jelaskan perbedaan antara JSON, XML, dan HTML!
   JSON: formatnya identik dengan kode yang dipakai untuk objek javascript. Data yang disimpan lebih efisien tetapi kurang rapi untuk dilihat. JSON cenderung lebih mudah dipakai daripada XML, dan data yang ditampilkan berupa array dengan value.
   XML: menggunakan XML DOM untuk melakukan loop pada dokumen. Tidak seperti JSON, XML mempunyai kemampuan untuk menampilkan data. XML juga lebih aman dari JSON yang cenderung rentan.
   HTML: merupakan markup language standar untuk file yang akan ditampilkan di browser. HTML cukup simpel dan mudah untuk dipelajari, tetapi memiliki fitur yang terbatas dibandingkan JSON yang dapat dipakai untuk membuat file yang lebih rumit.

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   Data delivery dibutuhkan dalam world wide web untuk komunikasi dari web client dan web server. Komunikasi ini dilakukan dengan mengirim HTTP requests dan menerima respon HTTP, untuk menampilkan website di browser.

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
   - membuat aplikasi baru mywatchlist dengan command: python manage.py startapp mywatchlist
   - Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
   - Membuat sebuah model MyWatchList di models.py di folder mywatchlist
   - Menambahkan minimal 10 data untuk objek MyWatchList di file initial_mywatchlist_data.json
   - Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam XML, JSON, dan HTML serta membuat routing  sehingga data di atas dapat diakses melalui URL: dengan menambahkan fungsi di views.py dan di urls.py, meng-import function yang telah dibuat dan menambahkan di urlpatterns
   - Melakukan deployment ke Heroku: menggunakan cara deploy yang sama dengan tugas 2

Sumber:
https://www.guru99.com/json-vs-xml-difference.html