from behave import (
    when,
    then,
)


@when("我取得目前部位")
def step_when_get_current_position(context):
    context.position = context.manager.current_position()


@then("我可以看到以下持股")
def step_then_can_see_position(context):
    for row in context.table:
        symbol = row["股票代號"]
        amount = int(row["持股數量"])

        assert context.position[symbol] == amount
