def print_models(unprinted_designs ,completed_models):
     """
         模拟打印每个设计，知道没有未打印的设计为止
         打印每个设计后，都将其移动到completed_models
                                                      """
     while unprinted_designs:
         current_design = unprinted_designs.pop()

         #模拟根据设计制作3d打印模型的过程
         print("Printing model: " + current_design)
         completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的设计列表"""
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["ipone case", "robot pendant", "dadecahedron" ]
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
