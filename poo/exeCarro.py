class Carro:

    def __init__(self, marca, ano=2010):
        self.__marca = marca
        self.__ano = ano
        self.__motor=None

    #     Getter
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca=marca

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self,motor):
        self.__motor=motor


class MotorV8:

    def mensagem(self):
        print("Estou usando um motor V8")


class MotorV6:

    def mensagem(self):
        print("Estou usando um motor V6")



carro1= Carro("FIAT",2012)
motor1=MotorV6()
motor2=MotorV8()

carro1.motor=motor1

carro1.motor.mensagem()

carro1.motor=motor2

carro1.motor.mensagem()