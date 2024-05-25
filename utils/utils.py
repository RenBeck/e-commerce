def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')

def formata_salario(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def cart_total_qtd(sacola):
    return sum([item['quantidade'] for item in sacola.values()])


def cart_totals(sacola):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item
            in sacola.values()
        ]
    )
