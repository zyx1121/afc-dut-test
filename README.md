# AFC Server Simulator

```
afc-server-simulator/
│
├── test_vectors/
│   ├── rsa_1.json
│   ├── rsa_2.json
│   └── ...
│
└── main.py
```

# DUT Test

```
afc-dut-test/
│
├── tests/
│   ├── rsa/
│   │   ├── test_01_frequency.py
│   │   ├── test_02_channel.py
│   │   ├── test_03_channel_frequency.py
│   │   └── ...
│   │
│   ├── usa/
│   │   └── ...
│   │
│   ├── sau/
│   │   └── ...
│   │
│   ├── uau/
│   │   └── ...
│   │
│   └── usv/
│       └── ...
│
├── configs/
│   ├── test.toml               # Test Config
│   └── ...
│
├── utils/
│   ├── afc.py                  # AFC Server Helper
│   ├── dut.py                  # DUT Helper
│   ├── logger.py               # Logger Helper
│   └── rf.py                   # RF Test Tool Helper
│
├── reports/
│   └── allure-results/         # Allure Report
│       └── ...
│
├── .cursorrules                # Cursor Rules
├── .gitignore                  # Git Ignore
├── conftest.py                 # pytest Fixtures
├── pyproject.toml              # Poetry
└── README.md                   # README
```

# Run

```
pytest -s -v
```

```
allure serve reports/allure-results
```
