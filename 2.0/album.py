def make_album(singer_name , album_name , album_number ="" ):
    if album_number:
        album = {"singer":singer_name ,"album":album_name , "number":album_number }
        
    else:
        album = {"singer":singer_name ,"album":album_name ,}
    return album

while True:
    print("\n 请输入歌手名称，专辑名称和专辑中的歌曲书目 ")
    print("在任何时候输入q退出")
    s_name = input("请输入歌曲名称：")
    if s_name ==  "q":
        break
    a_name = input("请输入专辑名称： ")
    if a_name ==  "q":
        break
    a_number = input("请输入专辑歌曲数目(可不输入)： ")
    if a_number ==  "q":
        break
    full_album = make_album(s_name ,a_name ,a_number)
    print(full_album)


