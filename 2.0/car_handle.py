def car_handle(car_brand ,car_model,**car_info):
    car_infor ={}
    car_infor["brand"] = car_brand
    car_infor["model"] = car_model
    for key,value in car_info.items():
        car_infor[key] = value
    return car_infor

car = car_handle("subaru", "putback",
                 color = "blue",
                 two_package ="True")
print(car)
        
