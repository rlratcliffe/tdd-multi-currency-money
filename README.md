# tdd-multi-currency-money
Part 1 of 'Test-Driven Devlopment by Example' by Kent Beck

## TODOs (copied from book)

- ~~$5 + 10 CHF = $10 if rate is 2:1~~
- ~~$5 + $5 = $10~~
- ~~Return Money from $5 + $5~~
- ~~Bank.reduce(Money)~~
- ~~Reduce Money with conversion~~
- ~~Reduce(Bank, String)~~
- ~~Sum.plus~~
- ~~Expression.times~~

## Development

View the github workflow as it shows what is required for development. `mypy` is used for type checking and `pytest` is used for unit testing.

## Quotes

"If the defect density can be reduced enough, then quality assurance can shift from reactive work to proactive work."

"Test-driven development is a way of managing fear during programming"

"Failure is progress."

"TDD is not about taking teeny-tiny steps, it's about *being able* to take teeny-tiny steps."

"There is a fabulous sequence in *Crossing to Safety* in which author Wallace Stegner describes a character's workshop. Every item is perfectly in place, the floor is spotless, all is order and cleanliness. The character, however, has never made anything."

"If you have a big system, then the parts that you touch all the time should be absolutely rock solid, so you can make daily changes confidently."

"Defect insertion is another way of evaluating test quality. The idea is simple: change the meaning of a line of code and a test should break. You can do this manually, or with a tool such as Jester."

## Lessons Learned

If you're stuck, write lower tests to isolate the problem.