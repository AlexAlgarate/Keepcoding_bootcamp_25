class GetterSetterClass:
    _mi_atributo_protegido = "This a static variable"
    __mi_atributo_privado = "This a static variable"

    def __init__(self, mi_atributo_protegido, mi_atributo_privado) -> None:
        self._mi_atributo_protegido = mi_atributo_protegido
        self.__mi_atributo_privado = mi_atributo_privado

    @property
    def mi_atributo_protegido(self):
        return self._mi_atributo_protegido

    @property
    def mi_atributo_privado(self):
        return self.__mi_atributo_privado

    @mi_atributo_privado.setter
    def mi_atributo_privado(self, value):
        if not isinstance(value, str):
            raise TypeError("El valor ha de ser una cadena.")
        self.__mi_atributo_privado = value

    @mi_atributo_privado.deleter
    def mi_atributo_privado(self):
        print("Eliminando el atributo")
        del self.__mi_atributo_privado


my_class = GetterSetterClass("Estoy protegido", "Soy privado")
print(my_class.mi_atributo_privado)
del my_class.mi_atributo_privado
my_class.mi_atributo_privado = "Vuelvo a ser privado."
print(my_class.mi_atributo_privado)
# Saltará excepción porque se está cumpliendo la validación del @property mi_atributo_privado
# my_class.mi_atributo_privado = 2
# print(my_class.mi_atributo_privado)
