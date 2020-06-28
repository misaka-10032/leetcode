# Integer to English Words

* Go reversely
* Stages
  * thousands: `['Thousand', 'Million', 'Billion']` 
  * hundreds: `'Hundred'`
  * elevens: `['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
               'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']`
  * tens: `['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
            'Seventy', 'Eighty', 'Ninety']`
  * nines: `['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten']`
* Outer loop: loop through thousands
* Inside thousands, make hundreds then make tens.
* Hundreds can combine `nines` and `hundreds`.
* Tens can be either `elevens` or combination of `tens` and `nines`.
* Tricky: add empty `''` so that we can find English word quickly.
* Dilemma: add `thousands` or not
  * `x >= 1`: must
  * `x < 1000 or x % 1000 != 0`: options

```
1000 000
   ^ --> %1000==0, no
1001 234
   ^ --> %1000!=0, yes
 100 234
   ^ --> <1000, yes
   0 100
   ^ --> <1, no
```
