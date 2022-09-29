Maysha Haliza Kirana - NPM 2106751202 - Tugas 4
Link: https://mayshatugas2.herokuapp.com/todolist/login

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Jawab:
1. {% csrf_token %} diimplementasikan untuk CSRF protection, yaitu untuk melindungi data dari serangan yang ada. Syntax ini akan meng-generate sebuah token dan jika request yang datang tidak mempunyai token ini, request tersebut tidak akan di-execute.

2. 

3. 

4. - Membuat aplikasi baru bernama todolist dengan perintah python manage.py startapp todolist
   - Menambahkan todolist dalam settings.py di folder project_django
   - Membuat model Task di models.py di folder todolist sesuai ketentuan (user, title, date, description)
   - Melakukan migrations dengan perintah python manage.py makemigrations dan python manage.py migrate
   - Mengimplementasikan fungsi-fungsi yang diperlukan pada views.py di folder todolist
   - Membuat html todolist, register, login, dan create-task dan mengimplementasikan sesuai ketentuan (untuk todolist.html, memuat tabel task, username pengguna terlogin, dan tombol logout)