# Стратегия rogue-like [![Build Status](https://travis-ci.com/terentyevalexey/TP_Project.svg?branch=master)](https://travis-ci.com/terentyevalexey/TP_Project)
Предположительно, игра будет чем-то похожей на The Binding of Isaac, 
но так как делать такое долго, то она будет обрубком (предположительно нелохим).

На текущий момент отсутствует всяческая графика, логика и так далее, но скоро
это будет исправлено

### Паттерны
Были использованы паттерны `singleton`, `abstract method`.

* `Singleton` использован, так как есть всего 1 главный персонаж.

* `Abstract method` был использован, так как есть множество врагов, для каждого
из них нужно своё создание

#### Юнит тесты
Запусктить тесты для проверки, создаются ли вражеские герои:
```
python3 -m unittest test_factory.py
```

