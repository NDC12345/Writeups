Challenge tiếp theo nào :>


![1](./1.png)


Vào trang web tác giả cung cấp thôi 

![2](./2.png)


Nó cho ta hai trường là name và grade mình nghĩ liệu có phải là SQLi không nhỉ, để xem ý tưởng đó có đúng không thì chúng ta vào source code tác giả cung cấp xem

![3](./3.png)

![4](./4.png)

![5](./5.png)

![6](./6.png)



Yeah có vẻ khi ta nhập vào hai trường name và grade server sẽ tạo ra cho chúng ta một đối tượng chứa name và grade tương ứng và khi ta nhập note vào nó sẽ chèn nội dung ta vừa nhập vào bảng notes sau đó in ra những gì chúng ta vừa nhập, và nếu chúng ta nhập vào trường name admin nó sẽ chuyển chúng ta về trang ban đầu. Để lấy được flag thì rõ ràng chúng ta phải đăng nhập với tư cách admin, tuy nhiên như tôi đã nói ở trên nó sẽ chặn chúng ta nhập admin vào vậy đơn giản là dùng SQLi thôi yeah khá là basic thôi

![8](./8.png)


Và boom ta đã có được flag :>

![9](./9.png)


