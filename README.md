# goit-algo-hw-04
 Порівняльний аналіз алгоритмів сортування


- Тестування алгоритмів на масивах розміром 100, 1000 і 10 000 елементів
- Вимірювання продуктивності за допомогою модуля `timeit`





| Розмір масиву | Insertion Sort | Merge Sort | Timsort (`sorted`) |
|---------------|----------------|------------|--------------------|
| 100 елементів | ~0.001 сек     | ~0.0005 сек| ~0.0002 сек        |
| 1000 елементів| ~0.12 сек      | ~0.005 сек | ~0.0015 сек        |
| 10000 елементів| ~10+ сек      | ~0.06 сек  | ~0.015 сек         |

Висновки
- Сортування вставками повільне на великих масивах через складність O(n²)
- Сортування злиттям значно ефективніше, але не адаптивне
- Timsort поєднує вставки та злиття, досягаючи стабільної роботи і кращої адаптації до впорядкованих ділянок
- Вбудовані алгоритми Python є високопродуктивними і в більшості випадків перевершують ручну реалізацію


Використовуйте вбудовані засоби Python (`sorted`, `.sort()`), які реалізують ефективний та адаптивний Timsort, замість самостійного кодування алгоритмів сортування з нуля.