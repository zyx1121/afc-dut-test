import time

import allure

from utils.logger import logger

pytestmark = [
    allure.parent_suite("RSA - Successful Registration and Spectrum Access Request"),
    allure.suite("Test 1 - Spectrum availability based on Inquired Frequency range"),
    allure.description("To verify the DUT can send frequency inquiry request."),
]


@allure.title("Test 1.0 - Initial Setup")
def test_1_0(dut, rf):
    with allure.step("DUT setup"):
        result = dut.setup()
        assert result, "DUT setup failed"

    with allure.step("Start RF monitoring"):
        result = rf.start_monitoring()
        assert result, "RF monitoring start failed"


@allure.title("Test 1.1 - Send Available Spectrum Inquiry Request")
def test_1_1(dut, afc):
    with allure.step("Set AFC response"):
        result = afc.set_test_vector("rsa_1")
        assert result, "Failed to set AFC response"

    with allure.step("Send frequency inquiry"):
        result = dut.send_available_spectrum_inquiry_request()
        assert result, "Send available spectrum inquiry request failed"

        last_request = afc.get_last_request()
        assert last_request, "AFC server did not receive the request"
        logger.debug(last_request)

        for inquiry_request in last_request.get("availableSpectrumInquiryRequests", []):
            assert (
                "inquiredFrequencyRange" in inquiry_request
            ), "Request body is missing frequency range information"


@allure.title("Test 1.2 - Check RF status")
def test_1_2(dut, rf):
    with allure.step("Wait for 6 seconds"):
        logger.info("Waiting for 6 seconds")
        time.sleep(6)

    with allure.step("Check RF status"):
        result = rf.check_status()
        assert result, "RF status check failed"
