Maysha Haliza Kirana - PBP C - NPM 2106751202 - Tugas 6
Link: https://mayshatugas2.herokuapp.com/todolist/login

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
3. Jelaskan penerapan asynchronous programming pada AJAX.
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Jawab:
1. Synchronous: setiap task dilakukan satu-satu di suatu waktu. Sebuah task baru akan dijalankan setelah task sebelumnya selesai dijalankan.
Asynchronous: beberapa/banyak task dapat dilakukan di waktu yang bersamaan. Tidak harus menunggu task sebelumnya selesai dahulu untuk memulai mengerjakan task berikutnya. Hal ini memudahkan untuk kondisi di mana ada banyak request yang perlu dijalankan dalam waktu yang bersamaan/pendek.
2. Event-Driven Programming adalah paradigma pemrograman di mana program dieksekusi melalui event dari user, seperti meng-klik tombol, menggunakan keyboard, dan sebagainya.
3. AJAX sendiri merupakan singkatan dari Asynchronous JavaScript And XML. AJAX mengirimkan data ke server di belakang layar, sehingga dapat memperbarui tampilan web secara asynchronous tanpa harus dilakukannya reload.
4. - Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON dengan return http response
   - Membuat path /todolist/json yang mengarah ke view json di urls.py di folder todolist
   - Melakukan pengambilan task menggunakan AJAX GET dengan $.get dan membuat function getter data
   - Membuat sebuah tombol Add Task yang membuka sebuah form untuk menambahkan task baru
   - Membuat view baru untuk menambahkan task baru (add_task) ke dalam database
   - Membuat path /todolist/add yang mengarah ke view add_task di urls.py di folder todolist
   - Menghubungkan form yang telah dibuat ke path /todolist/add melalui $.post dan membuat function yang dibutuhkan
   - Menutup modal setelah penambahan task telah berhasil dilakukan
   - Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page

REFERENSI
https://www.outsystems.com/blog/posts/asynchronous-vs-synchronous-programming/
https://studybay.com/blog/event-driven-development-features/