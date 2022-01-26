# Đồ án môn Lập trình với Python, đề tài: Game TETRIS

## Cài đặt python vào máy
Để có thể chạy được file chương trình thì ta sẽ phải cài python vào máy trước.

- [Hệ điều hành Windows](https://www.geeksforgeeks.org/how-to-install-python-on-windows/).

- [Hệ điều hành Linux](https://www.geeksforgeeks.org/how-to-install-python-on-linux/).

- [Hệ điều hành MacOS](https://www.geeksforgeeks.org/how-to-download-and-install-python-latest-version-on-macos-mac-os-x/).

Sau khi đã cài đặt và kiểm tra python đã được cài vào máy hay chưa thì ta sẽ tiến đến bước tiếp theo, đó là tải pygame về máy để có thể chạy được chương trình.

## Tải pygame về máy

Đây cũng chính là phần quan trọng nhất của chương trình, nên ta cần phải tải pygame về máy tương ứng với hệ điều hành theo các hướng dẫn sau:

- [Hệ điều hành Windows](https://www.geeksforgeeks.org/how-to-install-pygame-in-windows/)

- [Hệ điều hành Linux](https://www.geeksforgeeks.org/install-pygame-in-linux/)

- [Hệ điều hành MacOS](https://www.geeksforgeeks.org/install-pygame-in-macos/)

Sau khi đã hoàn thành các bước cài đặt cần thiết ở trên, ta sẽ tải toàn bộ source code về máy. Bằng cách tải theo file zip, ta sẽ giải nén file đó ra một folder và chuẩn bị cho bước tiếp theo.

## Chạy chương trình

Có thể sử dụng bất kỳ một IDE hay Text Editor nào có hỗ trợ việc chạy code, ở đây ta sẽ làm cách đơn giản nhất. Đó chính là sử dụng CMD của Windows và Terminal của MacOS và Linux.

Ta sẽ cd đến thư mục vừa giải nén lúc nãy, và gõ lệnh sau:

- Windows (giả sử thư mục giải nén ở ổ D, có thể ở ổ C hoặc bất kỳ ổ nào mà ta cảm thấy tiện): 
```cmd
D:\tetris_game-main> python main.py
```
- Linux (giả sử thư mục được giải nén ở Home, user và domain không nhất thiết phải giống hoàn toàn, tùy vào cài đặt của máy): 
```bash
user@ubuntu:~/tetris_game-main$ python3 main.py
```
- MacOS (giả sử thư mục được giải nén ở Home, user và domain không nhất thiết phải giống hoàn toàn, tùy vào cài đặt của máy):
```bash
MacBook-Pro:tetris_game-main user$ python3 main.py
```

Sau khi gõ lệnh xong thì ta ấn phím Enter, lúc đó chương trình sẽ chạy và ta có được màn hình game TETRIS.
