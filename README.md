# Quartic Potential

## Requirements

* python 3
* numpy

```shell
pip install -e .
```

## QDOs

![Two interecting Quantum Drude Oscillators](./assets/diagram-20220619.png "Two interecting Quantum Drude Oscillators")

## Usage

```shell
python src/main.py \
    --atom1 H \
    --atom2 H \
    --r 1.0 2.0 2.5 \
    --tau 1.0 2.0 \
    --energy_unit hartree
```

## Citation

## License
[Apache License 2.0](https://github.com/MatthieuSarkis/Quartic-Potential/blob/master/LICENSE)