import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://thanhnp:FEiM0OT3GTVUuhgO@cluster0-cqmi3.mongodb.net/test?retryWrites=true&w=majority'
)
db = client.team2

def insert(name,link,recipe,keyword):
    db.ff.insert_one({"title":name, "pic": link,"content":recipe,"kw":keyword})



insert("Pasta Cá hồi xốt cà chua",
"https://img-global.cpcdn.com/005_recipes/790b852965cd0f76/751x532cq70/pasta%F0%9F%8D%9Dca-h%E1%BB%93i%F0%9F%8D%BDs%E1%BB%91t-ca-chua-recipe-main-photo.jpg",
"""Nguyên liệu chuẩn bị:
2 miếng cá hồi
Mì sợi tuỳ loại
Rau quế
1 tsp bột nêm
Chút tiêu
Chút muối
Chanh vàng
5 thìa canh sốt cà chua và cà chua bi
4 thìa canh nước lọc
Tỏi bằm
Bơ
1/2 củ hành tây

Cách làm:

Bước 1: Hành tây thái hột lựu 
Rau quế thái nhỏ 
Tỏi bằm nhỏ 
Cà chua bi cắt đôi không để đứt 
Cá hồi ướp với tiêu, bột nêm để yên 20 phút.

Bước 2: Chảo dầu nóng cho hành tây và tỏi vào phi thơm. 
Cho cà chua bi vào xào chín rồi cho sốt cà vào, thêm nước lọc rồi nêm đường, 
bột nêm, hạt tiêu cho vừa miệng. Đảo đều và nấu cho đến khi nó sôi. Sau đó giảm nhiệt lại và đun cho 
đến khi nước sốt đặc lại, thỉnh thoảng đảo đều. Lá rau quế thái nhỏ cho vào trộn đều lên rồi để qua một bên.

Bước 3: Chảo dầu nóng cho cá vào chiên chín vàng, chiên ở nhiệt vừa cho cá chín đều, cá chín gắp ra thấm vào giấy thấm dầu. 
Đặt nồi nước lên bếp, cho vào 1 chút muối và 1 tsp dầu ăn đun sôi. Sau đó thả mì sợi vào luộc, nếm thử thấy chín thì vớt mì ra cho ráo nước. 
Cho dầu vào khi luộc để sợi mì vừa bóng vừa dai lại không bị dính.Trộn đều lên là xong. Bày ra đĩa măm măm thôi

Bước 4:Đặt chảo sốt cà lên bếp cho sốt nóng lại. Gắp mì ra đĩa, múc sốt rưới lên mì rồi đặt miếng cá lên trên cùng, nặn vài giọt chanh lên cá và thưởng thức.



""",

["Pasta","Hành tây"] )