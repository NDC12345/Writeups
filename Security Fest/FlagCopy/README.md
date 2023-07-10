Challenge đầu tiên là flagcopy ok cùng vào trang web xem ta có gì nào 



![1](./1.png)




Ok khá đơn giản ta có hai nút là Copy flags here và Source code. Ta thử vào source code thấy được gì


![3](./3.png)



Yeah có vẻ như ta phải truyền tham số dest để ghi đè đường dẫn của tệp flag.php nếu vượt qua thành công filter thì ta chỉ cần truyền lại path mà chúng ta đã chèn và lấy được flag thôi. Ý tưởng là vậy, cùng thực hiện thôi 

![4](./4.png)


Có vẻ chúng ta đã truyền thành công bây giờ quay trở lại để xem thu hoạch được gì nào


![6](./6.png)



Ồ có vẻ nó chuyển hướng chúng ta tới trang web ban đầu nhưng có vẻ url đã thay đổi sau một hồi suy nghĩ thì có vẻ ta phải bypass qua lần lượt path nêu trên cũng với đường dẫn ta đã tạo

![7](./7.png)



It worked !!! Và nó tiếp tục đưa ta tới trang web ban đầu nhưng đường dẫn khác yeah có vẻ đây là cái cuối cùng, thực hiện lại nào


![8](./8.png)


![9](./9.png)


Và boom ta có được flag :>


![10](./5.png)



À thực ra bonus thêm là có vẻ như tác giả không set lại đường dẫn mà những người chơi khác đã thực hiện nên nếu dùng dirseach chúng ta cũng có thể lấy được flag 

![11](./2.png)

![12](./10.png)



Bật mí nhỏ là ban đầu mình làm thế này nhưng nó hacker lỏd quá nên viết WU phải ngầu cho có kiến thức :>