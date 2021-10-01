# HW01 Hadoop

[Описание заданий](https://github.com/netcitizenrus/MADE_BigData_2021/blob/0947eb3b8967dfe6e337e38b609330308d42ef08/HW1%20-%20Hadoop.pdf)

# Блок 1

[Скриншоты](images/Images.md)

# Блок 2

[Создание и удаление файлов, директория](reports/block2_1.txt)

`Trash` в некотором смысле это аналог корзины в Windows. Удалённые файлы сначала попадают в директорию `.Trash` и потом в зависимости от `TrashPolicyDefault` удаляются совсем. При случайном удалении файлов есть возможность их восстановить из `.Trash`. Для того чтобы файлы не попадали в `.Trash`, а сразу удалялись необходимо указать опцию `-skipTrash`.

[Просмотр и копирование файлов](reports/block2_2.txt)

[Изменение фактора репликации и получение информации по блокам](reports/block2_3.txt)

Время на уменьшение числа реплик было затрачено больше чем на увеличение.

# Блок 3

Результаты вычисления [хранятся в computed_stat.txt](output/computed_stat.txt)

[Стандартная реализация](scripts/standard_stat.py)

MapReduce:
* [Map](scripts/mapper.py)
* [Reduce](scripts/reducer.py)

## Как запустить

```
docker-compose up --build
```

Зайти в контейнер после запуска:
```
docker exec -it namednode bash
```

Выполнить для добавления файла в HDFS:
```bash
bash /mnt/input/put_hdfs.sh
```

Выполнить для запуска вычислений двумя способами:
```bash
bash /mnt/scripts/run_stream.sh
```
