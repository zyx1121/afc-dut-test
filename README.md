# AFC DUT Test

AFC DUT 測試，使用 pytest 與 allure 為測試框架。

主元件分為三個部分：

1.  AFC Server Simulator

    用來模擬 AFC Server 的行為，主要提供 API 如下：

    - /availableSpectrumInquiry - 提供 DUT 請求的頻段、通道，回傳 AFC Server 的頻段、通道。
    - /setTestVector - 設定測試向量，提供 DUT Test 來選擇該測試項目所指定的測試頻段、通道。
    - /getLastRequest - 取得 DUT 最後一次的請求，提供 DUT Test 用來驗證 DUT 的回應是否正確。

2.  DUT Test

    測試腳本主體，包含 AFC Test Plan 的五個測試項目，分別為：

    - RSA - Successful Registration and Spectrum Access Request
    - USA - Unsuccessful Spectrum Access Request
    - SAU - Successful Spectrum Access Update
    - UAU - Unsuccessful Spectrum Access Update
    - USV - Unsuccessful Server Validation

3.  RF Test

    用來與 RF 測試設備進行通訊，並取得測試結果。

    （目前不確定 RF 測試設備的通訊協定，Serial Port 或 HTTP，但需要有下列 API 讓 DUT Test 來取得測試結果）

    - 取得現在 DUT 所執行的實際頻率
    - 取得現在 DUT 所執行的實際功率

## Structure

### AFC Server Simulator

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

### DUT Test

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
├── .gitignore                  # Git Ignore
├── conftest.py                 # pytest Fixtures
├── pyproject.toml              # Poetry
└── README.md                   # README
```

## Setup

1.  下載專案

    ```bash
    git clone https://github.com/zyx1121/afc-dut-test.git
    cd afc-dut-test
    ```

2.  安裝相依套件

    ```bash
    poetry install
    ```

    > 需要先安裝 Python 3.11 以上版本，並安裝 [Poetry](https://python-poetry.org)

3.  啟動 AFC Server Simulator

    ```bash
    python afc-server-simulator/main.py
    ```

    > vscode/cursor 會自動選擇 poetry 的 Python 環境，也可以使用 `poetry shell` 來進入 poetry 環境

## Run

1.  執行 DUT Test

    ```bash
    # 執行所有測試
    pytest -s -v

    # 執行 rsa 測試
    pytest -s -v tests/rsa

    # 執行 rsa 測試的 test_01_frequency.py 和 test_01_channel.py
    pytest -s -v tests/rsa/test_01_frequency.py tests/rsa/test_01_channel.py
    ```
    
    <img width="1186" alt="Screenshot 2025-02-03 at 11 00 48 AM" src="https://github.com/user-attachments/assets/5da72b43-e761-4110-9b0c-1bdcecc1b96c" />

## Report

1.  開啟 allure report

    ```bash
    allure serve reports/allure-results
    ```

    <img width="1651" alt="Screenshot 2025-02-03 at 11 05 25 AM" src="https://github.com/user-attachments/assets/5c0f1ac2-d20b-4e31-b62e-5448f3221ee7" />

    <img width="1651" alt="Screenshot 2025-02-03 at 11 05 43 AM" src="https://github.com/user-attachments/assets/18bd0809-7751-44a1-a56a-edf1b6ee473c" />

