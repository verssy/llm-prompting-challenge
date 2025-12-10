# LLM Prompting Challenge

## Сценарий использования

1. Изучите `.in`, `.out` файлы в директории `tests`
2. Измените `prompt.md` и используйте `Cline`, чтобы сгенерировать файл `solution.py`, в который будут переданы абсолютные пути до файлов `tests/translation/*.in`, ожидаемый вывод находится в файлах `tests/translation/*.out`, вывод должен происходить в stdout. Один запуск solution.py = один тестовый файл
3. `./run.sh`

## Ожидаемый вывод

```
running tests for: solution.py ...
-------
test_1: [PASS  ]
test_2: [PASS  ]
test_3L [PASS  ]
-------
Results: 3 passed, 0 failed
```
