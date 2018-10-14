def get_formatted_name(first ,last ,middle = ""):
    """合成一个完整的姓名"""
    if middle:
        full_name = first +" " +middle + " " +last
    else:
        full_name = first +" " +last
    return full_name.title()
