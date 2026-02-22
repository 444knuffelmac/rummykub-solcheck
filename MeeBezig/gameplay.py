from MeeBezig.chqngesforfulllooper import ispossible
from pyscript import web, when
@when("click", "#translate-button")
def activate(event):
    input_value = web.page("#input").value
    numbers = list(map(int, input_value.split(',')))
    result = ispossible(numbers)
    output_div = web.page["output"]
    output_div.innerText  = f"Is it possible? {result}"