import unittest
# подключа код, который написали
import swagger_store

'''
Swagger API  test v0.3
'''

# функция просто возвращает статус-код
def status(r):
    return r.status_code

# класс для апи тестов
class SwaggerAPITest(unittest.TestCase):
    def test_get_petinfo01(self):
        "Получение информации о питомце, позитивный"
        # сначала функция pet(1) выполнется в swagger и вернет объект ответа, 
        # затем функция status примет объект ответа и вернет целое число - статус-код
        self.assertEqual(status(swagger.pet(1)), 200)

    def test_get_petinfo02(self):
        "Получение информации о питомце, негативный - не найден"
        self.assertEqual(status(swagger.pet(600)), 404)

    def test_get_petinfo03(self):
        "Получение информации о питомце, негативный - Invalid ID supplied"
        self.assertEqual(status(swagger.pet("2+2")), 400)

    # Тест обновлений питомца    
    def test_get_pet_upd01(self):
        "Обновление информации о питомце, позитивный"
        # сначала функция pet_upd(1,"dog") выполнется в swagger и вернет объект ответа, 
        # затем функция status примет объект ответа и вернет целое число - статус-код
        self.assertEqual(status(swagger.pet_upd(1,"dog")), 200) 

    def test_get_pet_upd02(self):
        "Обновление информации о питомце, негативный"
        self.assertEqual(status(swagger.pet_upd(0,"cat")), 405) 

    def test_get_pet_upd03(self):
        "Обновление информации о питомце, Invalid ID"
        self.assertEqual(status(swagger.pet_upd("abc","frog")), 405) 

    def test_get_store_info01(self):
        "Получение информации о магазине, позитивный"
        self.assertEqual(status(swagger.store(1, 3, 6)), 200)

    def test_get_store_info02(self):
        "Получение информации о магазине, негативный - не найден"
        self.assertEqual(status(swagger.store(999, 126, 4346)), 404)

    def test_get_store_info03(self):
        "Получение информации о магазине, негативный - Invalid ID supplied"
        self.assertEqual(status(swagger.store("sdfs", "124fgf", "34rdg")), 400)


if __name__ == '__main__':
    unittest.main(verbosity=2)
