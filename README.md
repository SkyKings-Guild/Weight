# SkyKings Weight

A modified version of [Senither weight][1], kept up-to-date by the SkyKings team.

Currently up-to-date with SkyBlock version [0.19.84][2].

This project is in beta. All calculations may be subject to frequent changes.

## Installation

### Linux

```sh
python3 -m pip install -U git+https://github.com/SkyKings-Guild/Weight.git
```

### Windows

```bash
py -3 -m pip install -U git+https://github.com/SkyKings-Guild/Weight.git
```

You must have Git installed to run these commands, you can get it
at [git-scm.com/download](https://git-scm.com/download).

## Usage

```python
import skykings_weight

skykings_weight.slayer_weight("zombie", 500000)
```

[1]: https://github.com/Senither/hypixel-skyblock-facade/tree/master/src/generators

[2]: https://hypixel.net/threads/5439599
