from django import template
from django.utils.safestring import mark_safe
register = template.Library()

TABLE_HEAD = """
    <table class="table">
    <tbody>
"""

TABLE_TAIL = """
            </tbody>
</table>
"""

TABLE_CONTENT = """
    <tr>
        <td>{name}</td>
        <td>{value}</td>
    </tr>
"""

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работа аккамулятора': 'time_without_charge'
    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Разрешение экрана': 'resolution',
        'Объем батареи mhA': 'accum_volume',
        'Оперативная память': 'ram',
        'Слот для SD карты': 'sd',
        'Максимальный объем встраиваемой памяти GB': 'sd_volume',
        'Главная камера (МП)': 'main_cam_mp',
        'Фронтальная камера (МП)': 'frontal_cam_mp'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        if model_name == 'smartphone' and not product.sd and value == 'sd_volume':
            continue
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    if table_content.find("True") > 0:
        table_content = table_content.replace("True", "Есть")
    elif table_content.find("False") > 0:
        table_content = table_content.replace("False", "Нет")
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
