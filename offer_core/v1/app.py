class Cliente:

        def __init__(
                self, 
                tipo: str
        ) -> None:
                self.tipo = tipo

class Pedido:
       
        def __init__(
                self, 
                subtotal: float, 
                categoria: str
        ) -> None:
                self.subtotal = subtotal
                self.categoria = categoria


class DescuentoService:

    def calcularDescuento(
            pedido: Pedido,
            cliente: Cliente
    ) -> float:

        if cliente.tipo == "NUEVO":
                if pedido.categoria == "ELECTRONICA":
                       return pedido.subtotal * 0.05
                else:
                        return pedido.subtotal * 0.10
        elif cliente.tipo == "FRECUENTE":
                if pedido.categoria == "ELECTRONICA":
                        return pedido.subtotal * 0.08
                elif pedido.categoria == "HOGAR":
                        return pedido.subtotal * 0.15
                else: 
                        return pedido.subtotal * 0.12
        elif cliente.tipo == "VIP":
                return pedido.subtotal * 0.20
        else:
               return 0.0

class DescuentoServiceV2:

    def calcularDescuento(
            pedido: Pedido,
            cliente: Cliente
    ) -> float:

        if cliente.tipo == "NUEVO":
                if pedido.categoria == "ELECTRONICA":
                       return pedido.subtotal * 0.05
                else:
                        return pedido.subtotal * 0.10
        elif cliente.tipo == "FRECUENTE":
                if pedido.categoria == "ELECTRONICA":
                        return pedido.subtotal * 0.08
                elif pedido.categoria == "HOGAR":
                        return pedido.subtotal * 0.15
                elif pedido.categoria == "LIBRO":
                       pass # Logica nueva para clientes frecuentes con categoria libro
                else: 
                        return pedido.subtotal * 0.12
        elif cliente.tipo == "VIP":
                if pedido.categoria == "LIBRO":
                       pass # Logica nueva para clientes VIP con categoria libro
                return pedido.subtotal * 0.20
        elif cliente.tipo == "CORPORATIVO":
                if pedido.categoria == "LIBRO":
                       pass # Logica nueva para clientes corporativos con categoria libro
                pass # Logica nueva para clientes corporativos
        else:
               return 0.0