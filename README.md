# Quartic Potential

## Requirements

* python 3
* numpy
* ipykernel

```shell
pip install -e .
```

## QDOs

![Two interecting Quantum Drude Oscillators](./assets/diagram-20220619.png "Two interecting Quantum Drude Oscillators")

## Usage

```shell
python src/main.py \
    --m1 1.0 2.0 \
    --m2 1.0 \
    --q1 1.0 \
    --q2 1.0 3.0 \
    --omega1 1.0 \
    --omega2 1.0 \
    --r 1.0 2.0 2.5 \
    --tau 1.0 10.0 \
    --epsilon0 1.0 \
    --S0 -1.0
```

## Citation

## License
[Apache License 2.0](https://github.com/MatthieuSarkis/Quartic-Potential/blob/master/LICENSE)