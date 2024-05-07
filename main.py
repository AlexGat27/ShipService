from src.controllers.system_security_ctrl import get_system_security, get_risks, get_recommedation

if __name__ == "__main__":
    print("Возможные показатели защищенности: ")
    print(get_system_security())
    id = int(input("Выберите id показателя защищенности: "))
    print("Возможные риски: ")
    print(get_risks(id))
    print("Рекомендации: ")
    print(get_recommedation(id))


            